package de.gsi.cs.co.ap.lsa.setup.json;

import java.io.IOException;

import cern.lsa.domain.optics.LogicalHardware;

import com.fasterxml.jackson.core.JsonGenerator;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.JsonSerializer;
import com.fasterxml.jackson.databind.SerializerProvider;

/**
 * Custom serialization for {@link LogicalHardware} to ensure that the format of the JSON file is stable.
 * 
 * @author hhuether
 * @see JsonSerializer
 */
public class LogicalHardwareSerializer extends JsonSerializer<LogicalHardware> {

    @Override
    public void serialize(LogicalHardware value, JsonGenerator jgen, SerializerProvider provider) throws IOException,
            JsonProcessingException {
        jgen.writeStartObject();
        jgen.writeStringField(JsonNodeNames.TRIM_LINKRULE, value.getLinkRuleName());
        jgen.writeEndObject();
    }

}
