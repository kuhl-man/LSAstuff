package de.gsi.cs.co.ap.lsa.setup.json;

import java.io.IOException;

import cern.accsoft.commons.domain.Accelerator;
import cern.accsoft.commons.domain.zones.AcceleratorZone;
import cern.accsoft.commons.util.Nameds;
import cern.lsa.client.DeviceService;
import cern.lsa.client.ServiceLocator;
import cern.lsa.domain.devices.DeviceType;
import cern.lsa.domain.devices.DeviceTypeVersion;
import cern.lsa.domain.devices.DeviceTypes;
import cern.lsa.domain.devices.spi.DeviceImpl;

import com.fasterxml.jackson.core.JsonParser;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.core.JsonToken;
import com.fasterxml.jackson.databind.DeserializationContext;
import com.fasterxml.jackson.databind.deser.std.StdDeserializer;

public class DeviceDeserializer extends StdDeserializer<DeviceImpl> {

    private static final long serialVersionUID = -3055703764004227540L;

    private final DeviceService deviceService;

    public DeviceDeserializer() {
        super(DeviceImpl.class);

        this.deviceService = ServiceLocator.getService(DeviceService.class);
    }

    @Override
    public DeviceImpl deserialize(JsonParser jp, DeserializationContext ctxt, DeviceImpl intoValue) throws IOException,
            JsonProcessingException {
        // Get device name from DeserializationContext (since we cannot access the parent node)
        intoValue.setName((String) ctxt.findInjectableValue(JsonNodeNames.DEVICE_NAME, null, null));

        // Iterate through all values in JSON node
        while (jp.nextToken() != JsonToken.END_OBJECT) {
            String name = jp.getCurrentName();
            jp.nextToken();

            if (name.equals(JsonNodeNames.ACCELERATOR_ZONE)) {
                // Get accelerator from DeserializationContext
                Accelerator accelerator = (Accelerator) ctxt.findInjectableValue(JsonNodeNames.ACCELERATOR, null, null);

                AcceleratorZone acceleratorZone = Nameds.findByName(accelerator.getAcceleratorZones(), jp.getText());
                if (acceleratorZone == null) {
                    throw new RuntimeException("Accelerator zone '" + jp.getText() + "' was not found in database.'");
                }
                intoValue.setAcceleratorZone(acceleratorZone);
            }

            if (name.equals(JsonNodeNames.DEVICE_TYPE)) {
                DeviceType deviceType = deviceService.findDeviceType(jp.getText());
                if (deviceType == null) {
                    throw new RuntimeException("Device type '" + jp.getText() + "' was not found in database.");
                }

                // TODO HH: When doing the import, which device type version should be used? Do we need to include a
                // version number in the JSON file, or can / shall that be set hard coded? Should we check that
                // really just virtual devices can be imported?
                DeviceTypeVersion deviceTypeVersion = DeviceTypes.getLatestVersion(deviceType);
                if (deviceTypeVersion == null) {
                    throw new RuntimeException("No device type version found for device type '" + jp.getText() + "'.");
                }
                intoValue.setDeviceTypeVersion(deviceTypeVersion);
            }

            if (name.equals(JsonNodeNames.DESCRIPTION)) {
                intoValue.setDescription(jp.getText());
            }

            if (name.equals(JsonNodeNames.DEVICE_ALIAS)) {
                intoValue.setAlias(jp.getText());
            }

            if (name.equals(JsonNodeNames.IS_MULTIPLEXED)) {
                intoValue.setMultiplexed(jp.getBooleanValue());
            }
        }

        return intoValue;
    }

    @Override
    public DeviceImpl deserialize(JsonParser jp, DeserializationContext ctxt) throws IOException,
            JsonProcessingException {
        // Create device
        DeviceImpl deviceImpl = new DeviceImpl(-1, (String) ctxt.findInjectableValue(JsonNodeNames.DEVICE_NAME, null,
                null));

        return deserialize(jp, ctxt, deviceImpl);
    }
}
