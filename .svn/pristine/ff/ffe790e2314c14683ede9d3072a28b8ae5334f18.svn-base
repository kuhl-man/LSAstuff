package de.gsi.cs.co.ap.lsa.setup.spi;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.JsonNode;

import de.gsi.cs.co.ap.lsa.setup.json.JsonNodeNames;

/**
 * @author rmueller
 * @author hhuether
 */
public class ParameterHardwareImportImpl extends ParameterBaseImportImpl {

    public ParameterHardwareImportImpl(JsonNode root) {
        super(root, Boolean.FALSE);
    }

    @Override
    public String retrieveChanges(Boolean printArtifactsToBeKept) throws JsonProcessingException {
        return super.retrieveChanges(printArtifactsToBeKept, JsonNodeNames.PARAMETERS_HARDWARE);
    }

    @Override
    public void checkImport() throws JsonProcessingException {
        super.checkImport(Boolean.FALSE);
    }

    @Override
    public void applyCreate(Boolean printQuantities) {
        super.applyCreate(printQuantities, Boolean.FALSE);
    }

    @Override
    public void applyDelete(Boolean printQuantities) {
        super.applyDelete(printQuantities, Boolean.FALSE);
    }

    @Override
    public void applyUpdate(Boolean printQuantities) {
        super.applyUpdate(printQuantities, Boolean.FALSE);
    }

    @Override
    public void evaluate() throws JsonProcessingException {
        super.evaluate(Boolean.FALSE);
    }
}
