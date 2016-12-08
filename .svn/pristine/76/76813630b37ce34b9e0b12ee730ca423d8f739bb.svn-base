package de.gsi.cs.co.ap.lsa.setup.json;

import java.io.IOException;
import java.math.BigInteger;
import java.util.Set;

import org.apache.commons.logging.Log;
import org.apache.commons.logging.LogFactory;

import cern.accsoft.commons.value.spi.ValueDescriptorImpl;
import cern.lsa.client.DeviceService;
import cern.lsa.client.ParameterService;
import cern.lsa.client.ServiceLocator;
import cern.lsa.domain.devices.Device;
import cern.lsa.domain.settings.ParameterType;
import cern.lsa.domain.settings.factory.ParameterTypesRequestBuilder;
import cern.lsa.domain.settings.spi.ParameterImpl;

import com.fasterxml.jackson.core.JsonParser;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.core.JsonToken;
import com.fasterxml.jackson.databind.DeserializationContext;
import com.fasterxml.jackson.databind.deser.std.StdDeserializer;

import de.gsi.cs.co.ap.lsa.setup.spi.ImportMessages;

public class ParameterDeserializer extends StdDeserializer<ParameterImpl> {

    private static final long serialVersionUID = 754817277382852011L;

    private static final Log LOGGER = LogFactory.getLog(ParameterDeserializer.class);

    private final ParameterService parameterService;
    private final DeviceService deviceService;

    public ParameterDeserializer() {
        super(ParameterImpl.class);

        this.parameterService = ServiceLocator.getService(ParameterService.class);
        this.deviceService = ServiceLocator.getService(DeviceService.class);
    }

    @Override
    public ParameterImpl deserialize(JsonParser jp, DeserializationContext ctxt, ParameterImpl intoValue)
            throws IOException, JsonProcessingException {
        String deviceName = null;
        String propertyName = null;
        String fieldName = null;
        String parameterTypeName = null;
        Double maxDelta = Double.NaN;
        BigInteger xPrec = null;
        BigInteger yPrec = null;

        // Get the info if a physics (virtual) or a hardware parameter is to be deserialized from the context
        Boolean isVirtual = (Boolean) ctxt.findInjectableValue("isVirtual", null, null);

        // Get device name from DeserializationContext (since we cannot access the parent node)
        intoValue.setName((String) ctxt.findInjectableValue(JsonNodeNames.PARAMETER_NAME, null, null));

        // Iterate through all values in JSON node
        while (jp.nextToken() != JsonToken.END_OBJECT) {
            String name = jp.getCurrentName();
            jp.nextToken();

            if (jp.getCurrentToken() != JsonToken.VALUE_NULL) {
                switch (name) {
                case JsonNodeNames.BELONGS_TO_FUNCTION_BPROC:
                    intoValue.setBelongsToFunctionBeamProcess(jp.getBooleanValue());
                    break;

                case JsonNodeNames.DEFAULT_HIERARCHY:
                    intoValue.setDefaultHierarchy(jp.getText());
                    break;

                case JsonNodeNames.DEVICE_NAME:
                    deviceName = jp.getText();
                    Device device = deviceService.findDevice(deviceName);
                    if (device == null) {
                        throw new RuntimeException(String.format(ImportMessages.ERROR_NOT_FOUND_DEVICE, deviceName));
                    }
                    intoValue.setDevice(device);
                    break;

                case JsonNodeNames.FIELD_NAME:
                    fieldName = jp.getText();
                    break;

                case JsonNodeNames.IS_RESERVED_FOR_OP_EXPERTS:
                    intoValue.setReservedForOpExperts(jp.getBooleanValue());
                    break;

                case JsonNodeNames.MAX_DELTA:
                    maxDelta = jp.getDoubleValue();
                    break;

                case JsonNodeNames.PROPERTY_NAME:
                    propertyName = jp.getText();
                    break;

                case JsonNodeNames.PARAMETER_TYPE_NAME:
                    parameterTypeName = jp.getText();
                    break;

                case JsonNodeNames.TRIMABLE:
                    intoValue.setTrimable(jp.getBooleanValue());
                    break;

                case JsonNodeNames.USERGROUP:
                    LOGGER.warn(ImportMessages.WARNING_UNSUPPORTED_USERGROUP);
                    break;

                case JsonNodeNames.X_PREC: {
                    xPrec = jp.getBigIntegerValue();

                    break;
                }

                case JsonNodeNames.Y_PREC: {
                    yPrec = jp.getBigIntegerValue();
                    break;
                }

                default:
                    LOGGER.warn(String.format(ImportMessages.WARNING_UNSUPPORTED_UNKNOWN_FIELD, name,
                            intoValue.getName()));
                    break;
                }
            }
        }

        // Find device that the parameter belongs to. The device has to be present in the database.
        Device device = deviceService.findDevice(deviceName);
        if (device == null) {
            throw new RuntimeException(String.format(ImportMessages.ERROR_NOT_FOUND_DEVICE, deviceName));
        }

        // If the parameter type name has to be explicitly specified physics parameters. It will be constructed from
        // device name, property name and field name for hardware parameters.
        if (isVirtual) {
            if (parameterTypeName == null) {
                String.format(ImportMessages.ERROR_NOT_SPECIFIED_PARAMETER_TYPE_NAME, intoValue.getName());
            }
        } else {
            // Construct the parameter type name
            if (propertyName == null) {
                throw new RuntimeException(String.format(ImportMessages.ERROR_NOT_SPECIFIED_PROPERTY_NAME,
                        intoValue.getName()));
            }
            if (fieldName == null) {
                throw new RuntimeException(String.format(ImportMessages.ERROR_NOT_SPECIFIED_FIELD_NAME,
                        intoValue.getName()));
            }
            parameterTypeName = deviceName + "/" + propertyName + "#" + fieldName;
        }

        // Parameter type name is unique, so we can just search for that.
        Set<ParameterType> parameterTypesFoundInDatabase = parameterService
                .findParameterTypes(ParameterTypesRequestBuilder.byParameterTypeName(parameterTypeName));

        // If the set of found parameters is empty, the parameter type does not exist.
        if (parameterTypesFoundInDatabase.size() == 0) {
            throw new RuntimeException(String.format(ImportMessages.ERROR_NOT_FOUND_PARAMETER_TYPE, parameterTypeName));
        }

        intoValue.setType(parameterTypesFoundInDatabase.iterator().next());

        // Max delta needs a little bit of special treatment because of NaN handling. That's why it is set via a
        // preinitialized local variable.
        intoValue.setMaxDelta(maxDelta);

        // Set x and y precisions
        ValueDescriptorImpl valueDescriptorImpl = (ValueDescriptorImpl) intoValue.getValueDescriptor();
        // xPrec may be null
        if (valueDescriptorImpl == null) {
            valueDescriptorImpl = new ValueDescriptorImpl();
        }
        if (xPrec == null) {
            valueDescriptorImpl.setYPrecision(null);
        } else {
            valueDescriptorImpl.setYPrecision(xPrec.intValue());
        }
        // yPrec may be null
        if (yPrec == null) {
            valueDescriptorImpl.setYPrecision(null);
        } else {
            valueDescriptorImpl.setYPrecision(yPrec.intValue());
        }
        intoValue.setValueDescriptor(valueDescriptorImpl);

        return intoValue;
    }

    @Override
    public ParameterImpl deserialize(JsonParser jp, DeserializationContext ctxt) throws IOException,
            JsonProcessingException {
        // Create parameter
        ParameterImpl parameterImpl = new ParameterImpl();
        parameterImpl.setId(-1);

        return deserialize(jp, ctxt, parameterImpl);
    }
}