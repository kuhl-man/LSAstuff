package de.gsi.cs.co.ap.lsa.setup.json;

import java.io.IOException;

import cern.lsa.client.ParameterService;
import cern.lsa.client.ServiceLocator;
import cern.lsa.domain.settings.Parameter;
import cern.lsa.domain.settings.ParameterTreeNode;
import cern.lsa.domain.settings.spi.ParameterImpl;
import cern.lsa.domain.settings.spi.ParameterTreeNodeImpl;

import com.fasterxml.jackson.core.JsonParser;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.core.JsonToken;
import com.fasterxml.jackson.databind.DeserializationContext;
import com.fasterxml.jackson.databind.deser.std.StdDeserializer;

import de.gsi.cs.co.ap.lsa.setup.data.ParameterTreeNodeWithPositions;
import de.gsi.cs.co.ap.lsa.setup.spi.ImportMessages;

public class ParameterRelationDeserializer extends StdDeserializer<ParameterTreeNodeWithPositions> {

    private static final long serialVersionUID = 3769647763699276403L;

    // LSA services
    private final ParameterService parameterService;

    public ParameterRelationDeserializer() {
        super(ParameterTreeNode.class);

        parameterService = ServiceLocator.getService(ParameterService.class);
    }

    @Override
    public ParameterTreeNodeWithPositions deserialize(JsonParser jp, DeserializationContext ctxt) throws IOException,
            JsonProcessingException {

        // Get hierarchy name and child parameter name from DeserializationContext (since we cannot access the parent
        // node)
        String hierarchyName = (String) ctxt.findInjectableValue(JsonNodeNames.HIERARCHY_NAME, null, null);
        String childParameterName = (String) ctxt.findInjectableValue(JsonNodeNames.CHILD_NAME, null, null);

        // Child parameter has to be present in database
        ParameterImpl childParameter = (ParameterImpl) parameterService.findParameterByName(childParameterName);
        if (childParameter == null) {
            throw new RuntimeException(String.format(ImportMessages.ERROR_NOT_FOUND_PARAMETER, childParameterName));
        }

        // This is not actually written to the database. The field is just misused to store which hierarchy
        // the relations belong to for output to the user and creation of relationships later.
        childParameter.setDefaultHierarchy(hierarchyName);

        ParameterTreeNodeWithPositions childParameterTreeNode = new ParameterTreeNodeWithPositions(
                new ParameterTreeNodeImpl(childParameter, Boolean.FALSE));

        // Iterate through all values in JSON node
        while (jp.nextToken() != JsonToken.END_OBJECT) {

            // We should find a parent
            String parentParameterName = jp.getText();
            Parameter parentParameter = parameterService.findParameterByName(parentParameterName);
            // Parent parameter has to be present in database
            if (parentParameter == null) {
                throw new RuntimeException(String.format(ImportMessages.ERROR_NOT_FOUND_PARAMETER, parentParameterName));
            }

            // Store the relation by adding the child node. This should automatically be done for child(parent) as
            // well. The method "addParent" is private and not accessible.
            ParameterTreeNodeImpl parentParameterTreeNode = new ParameterTreeNodeImpl(parentParameter, Boolean.TRUE);
            parentParameterTreeNode.addChild(childParameterTreeNode.getParameterTreeNodeImpl());

            // Look for a position node and store the value for possibly writing it to the database later
            while (jp.nextToken() != JsonToken.END_OBJECT) {
                if (jp.getCurrentName() == JsonNodeNames.POSITION) {
                    jp.nextToken();

                    Integer position = jp.readValueAs(Integer.class);

                    childParameterTreeNode.putPosition(parentParameterTreeNode.getParameter().getName(), position);
                }
            }
        }

        return childParameterTreeNode;
    }
}
