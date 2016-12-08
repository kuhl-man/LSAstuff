package de.gsi.cs.co.ap.lsa.setup.json;

import java.io.IOException;

import cern.lsa.domain.optics.LogicalHardware;
import cern.lsa.domain.optics.spi.LogicalHardwareImpl;

import com.fasterxml.jackson.core.JsonParser;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.core.JsonToken;
import com.fasterxml.jackson.databind.DeserializationContext;
import com.fasterxml.jackson.databind.deser.std.StdDeserializer;

import de.gsi.cs.co.ap.lsa.setup.spi.ImportMessages;

public class LogicalHardwareDeserializer extends StdDeserializer<LogicalHardware> {

    private static final long serialVersionUID = 4472587484706660613L;

    public LogicalHardwareDeserializer() {
        super(LogicalHardware.class);
    }

    @Override
    public LogicalHardware deserialize(JsonParser jp, DeserializationContext ctxt, LogicalHardware intoValue)
            throws IOException, JsonProcessingException {

        // Iterate through all values in JSON node
        while (jp.nextToken() != JsonToken.END_OBJECT) {
            String name = jp.getCurrentName();
            jp.nextToken();

            if (name.equals(JsonNodeNames.TRIM_LINKRULE)) {
                ((LogicalHardwareImpl) intoValue).setLinkRuleName(jp.getText());
            }
        }

        if ((intoValue.getLinkRuleName() == null) || ("".equals(intoValue.getLinkRuleName()))) {
            throw new RuntimeException(String.format(ImportMessages.ERROR_DATA_ENTRY_LINK_RULE_NAME_NOT_SPECIFIED,
                    intoValue.getName()));
        }

        return intoValue;
    }

    @Override
    public LogicalHardware deserialize(JsonParser jp, DeserializationContext ctxt) throws IOException,
            JsonProcessingException {
        // Create LogicalHardware
        LogicalHardwareImpl logicalHardwareImpl = new LogicalHardwareImpl(-1, jp.getCurrentName());

        return deserialize(jp, ctxt, logicalHardwareImpl);
    }
}
