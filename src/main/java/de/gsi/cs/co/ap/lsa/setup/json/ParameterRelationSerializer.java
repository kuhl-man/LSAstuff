package de.gsi.cs.co.ap.lsa.setup.json;

import java.io.IOException;

import cern.lsa.domain.settings.ParameterTreeNode;

import com.fasterxml.jackson.core.JsonGenerator;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.JsonSerializer;
import com.fasterxml.jackson.databind.SerializerProvider;

import de.gsi.cs.co.ap.lsa.setup.data.ParameterTreeNodeWithPositions;

/**
 * Custom serialization for {@link ParameterTreeNode}s to ensure that the format of the JSON file is stable.
 * 
 * @author hhuether
 * @see JsonSerializer
 */
public class ParameterRelationSerializer extends JsonSerializer<ParameterTreeNodeWithPositions> {

    @Override
    public void serialize(ParameterTreeNodeWithPositions value, JsonGenerator jgen, SerializerProvider provider)
            throws IOException, JsonProcessingException {
        jgen.writeStartObject();

        for (ParameterTreeNode parentParameterTreeNode : value.getParameterTreeNodeImpl().getParents()) {
            jgen.writeObjectFieldStart(parentParameterTreeNode.getName());
            if (value.getPosition(parentParameterTreeNode.getParameter().getName()) != null) {
                jgen.writeNumberField(JsonNodeNames.POSITION,
                        value.getPosition(parentParameterTreeNode.getParameter().getName()));
            } else {
                jgen.writeNullField(JsonNodeNames.POSITION);
            }
            jgen.writeEndObject();
        }

        jgen.writeEndObject();
    }
}
