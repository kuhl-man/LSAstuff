package de.gsi.cs.co.ap.lsa.setup.json;

import java.io.IOException;

import cern.lsa.domain.settings.Parameter;
import cern.lsa.domain.settings.spi.ParameterImpl;

import com.fasterxml.jackson.core.JsonGenerator;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.JsonSerializer;
import com.fasterxml.jackson.databind.SerializerProvider;

/**
 * Custom serialization for {@link Parameter}s to ensure that the format of the JSON file is stable.
 * 
 * @author hhuether
 * @see JsonSerializer
 */
public class ParameterSerializer extends JsonSerializer<ParameterImpl> {

    @Override
    public void serialize(ParameterImpl value, JsonGenerator jgen, SerializerProvider provider) throws IOException,
            JsonProcessingException {
        jgen.writeStartObject();
        jgen.writeBooleanField(JsonNodeNames.BELONGS_TO_FUNCTION_BPROC, value.belongsToFunctionBeamProcess());
        jgen.writeStringField(JsonNodeNames.DEFAULT_HIERARCHY, value.getDefaultHierarchy());
        jgen.writeStringField(JsonNodeNames.DEVICE_NAME, value.getDevice().getName());
        jgen.writeBooleanField(JsonNodeNames.IS_RESERVED_FOR_OP_EXPERTS, value.isReservedForOpExperts());
        jgen.writeNumberField(JsonNodeNames.MAX_DELTA, value.getMaxDelta());
        // parameter type name also covers field name and property name, which are used for hardware parameters.
        jgen.writeStringField(JsonNodeNames.PARAMETER_TYPE_NAME, value.getType().getName());
        jgen.writeBooleanField(JsonNodeNames.TRIMABLE, value.isTrimable());

        if (value.getValueDescriptor().getXPrecision() != null) {
            jgen.writeNumberField(JsonNodeNames.X_PREC, value.getValueDescriptor().getXPrecision());
        } else {
            jgen.writeNullField(JsonNodeNames.X_PREC);
        }
        if (value.getValueDescriptor().getYPrecision() != null) {
            jgen.writeNumberField(JsonNodeNames.Y_PREC, value.getValueDescriptor().getYPrecision());
        } else {
            jgen.writeNullField(JsonNodeNames.Y_PREC);
        }

        jgen.writeEndObject();
    }
}
