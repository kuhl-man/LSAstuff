package de.gsi.cs.co.ap.lsa.setup.spi;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.JsonNode;

import de.gsi.cs.co.ap.lsa.setup.json.JsonNodeNames;

/**
 * @author rmueller
 * @author hhuether
 */
public class ParameterPhysicsImportImpl extends ParameterBaseImportImpl {

    public ParameterPhysicsImportImpl(JsonNode root) {
        super(root, Boolean.TRUE);
    }

    @Override
    public String retrieveChanges(Boolean printArtifactsToBeKept) throws JsonProcessingException {
        return super.retrieveChanges(printArtifactsToBeKept, JsonNodeNames.PARAMETERS_PHYSICS);
    }

    @Override
    public void checkImport() throws JsonProcessingException {
        super.checkImport(Boolean.TRUE);
    }

    @Override
    public void applyCreate(Boolean printQuantities) {
        super.applyCreate(printQuantities, Boolean.TRUE);
    }

    @Override
    public void applyDelete(Boolean printQuantities) {
        super.applyDelete(printQuantities, Boolean.TRUE);
    }

    @Override
    public void applyUpdate(Boolean printQuantities) {
        super.applyUpdate(printQuantities, Boolean.TRUE);
    }

    @Override
    public void evaluate() throws JsonProcessingException {
        super.evaluate(Boolean.TRUE);
    }
}
