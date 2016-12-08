package de.gsi.cs.co.ap.lsa.setup.spi;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;

import org.apache.commons.logging.Log;
import org.apache.commons.logging.LogFactory;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.JsonNode;

import cern.lsa.client.ParameterService;
import cern.lsa.client.ServiceLocator;
import cern.lsa.domain.settings.Parameter;
import cern.lsa.domain.settings.spi.ParameterImpl;
import de.gsi.cs.co.ap.lsa.setup.json.JsonNodeNames;

abstract public class ParameterBaseImportImpl extends ImportBaseImpl {

    private static final Log LOGGER = LogFactory.getLog(ParameterBaseImportImpl.class);

    // LSA services
    private final ParameterService parameterService;

    private final JsonNode parametersNode;
    private final List<ParameterImpl> parametersToKeep = new LinkedList<>();
    private final List<ParameterImpl> parametersToUpdate = new LinkedList<>();
    private final List<ParameterImpl> parametersToCreate = new LinkedList<>();

    ParameterBaseImportImpl(JsonNode root, Boolean isVirtual) {
        super(root);

        // Inject the information if a parameter is a physics (virtual) or hardware (!virtual) parameter. This
        // is needed since parameter type names are handled differently between the two.
        this.addValueToInjectIntoDeserializer("isVirtual", isVirtual);

        if (isVirtual) {
            this.parametersNode = root.get(JsonNodeNames.PARAMETERS_PHYSICS);
        } else {
            this.parametersNode = root.get(JsonNodeNames.PARAMETERS_HARDWARE);
        }

        parameterService = ServiceLocator.getService(ParameterService.class);
    }

    /**
     * The importer has to decide whether a {@link Parameter} that is already present in the database has to be updated.
     * Therefore, a method that calculates a hash code is needed. For {@link Parameter}s, equality (in the sense of an
     * "equals" method) is defined as value equality of the ID. So it is not possible to use a hash code method that is
     * already present. A completely generalized version that uses reflection or another equivalent approach would not
     * necessarily work as only specific attributes (i.e. those that are actually imported) shall be considered here.
     * 
     * @param parameter {@link Parameter} which the hash code shall be calculated for. May be null.
     * @return Hash code for the {@link Parameter} specified
     */
    private int hashCodeForImport(Parameter parameter) {
        final int prime = 31;
        int result = 1;
        result = prime * result + ((parameter.getName() == null) ? 0 : parameter.getName().hashCode());
        result = prime * result + (Boolean.valueOf(parameter.belongsToFunctionBeamProcess()).hashCode());
        result = prime * result
                + ((parameter.getDefaultHierarchy() == null) ? 0 : parameter.getDefaultHierarchy().hashCode());
        result = prime * result
                + ((parameter.getDevice().getName() == null) ? 0 : parameter.getDevice().getName().hashCode());
        result = prime * result + (parameter.isReservedForOpExperts() ? 1231 : 1237);
        result = prime * result + (Double.valueOf(parameter.getMaxDelta()).hashCode());
        // parameter type name also covers field name and property name, which are used for hardware parameters.
        result = prime * result
                + ((parameter.getType().getName() == null) ? 0 : parameter.getType().getName().hashCode());
        result = prime * result + (Boolean.valueOf(parameter.isTrimable()).hashCode());
        result = prime
                * result
                + ((parameter.getValueDescriptor().getXPrecision() == null) ? 0 : parameter.getValueDescriptor()
                        .getXPrecision().hashCode());
        result = prime
                * result
                + ((parameter.getValueDescriptor().getYPrecision() == null) ? 0 : parameter.getValueDescriptor()
                        .getYPrecision().hashCode());
        return result;
    }

    /**
     * Checks that all {@link Parameter}s specified in the JSON file actually are present in the database. If this is
     * not the case, e.g. one more {@code Parameters}s were not imported correctly, a {@link RuntimeException} is
     * thrown.
     * 
     * @throws JsonProcessingException In case that something goes wrong with deserialization of the JSON file
     * @throws RuntimeException In case that the import did not achieve the expected results
     */
    protected void checkImport(Boolean isVirtual) throws JsonProcessingException {
        System.out.println("    Checking import of " + (isVirtual ? "physics" : "hardware") + " parameters...");

        Iterator<String> parameterNames = this.parametersNode.fieldNames();
        while (parameterNames.hasNext()) {
            String parameterName = parameterNames.next();
            JsonNode parameterNode = this.parametersNode.get(parameterName);

            // Inject the parameter name into the deserialization context. This is needed since we cannot access the
            // parent node within the deserializer.
            this.addValueToInjectIntoDeserializer(JsonNodeNames.PARAMETER_NAME, parameterName);
            ParameterImpl parameterWithTargetValues = this.getObjectMapper().treeToValue(parameterNode,
                    ParameterImpl.class);

            Parameter parameterWithDatabaseValues = parameterService.findParameterByName(parameterName);

            if (hashCodeForImport(parameterWithTargetValues) != hashCodeForImport(parameterWithDatabaseValues)) {
                throw new RuntimeException(String.format(
                        (isVirtual ? ImportMessages.ERROR_NOT_IMPORTED_CORRECTLY_PARAMETER_PHYSICS
                                : ImportMessages.ERROR_NOT_IMPORTED_CORRECTLY_PARAMETER_HARDWARE), parameterName));
            }
        }

        System.out.println("    ..." + (isVirtual ? "Physics" : "Hardware") + " parameters were imported correctly.");
    }

    protected void evaluate(Boolean isVirtual) throws JsonProcessingException {
        if (parametersNode != null) {
            Iterator<String> parameterNames = parametersNode.fieldNames();
            while (parameterNames.hasNext()) {
                String parameterName = parameterNames.next();
                JsonNode parameterNode = parametersNode.get(parameterName);

                // Inject the parameter name into the deserialization context. This is needed since we cannot access the
                // parent node within the deserializer.
                this.addValueToInjectIntoDeserializer(JsonNodeNames.PARAMETER_NAME, parameterName);

                ParameterImpl parameterImpl = (ParameterImpl) parameterService.findParameterByName(parameterName);
                if (parameterImpl != null) {
                    // Parameter is already present in database
                    int dbHashCode = hashCodeForImport(parameterImpl);

                    this.getObjectMapper().readerForUpdating(parameterImpl)
                            .treeToValue(parameterNode, ParameterImpl.class);

                    int jsonHashCode = hashCodeForImport(parameterImpl);
                    if (dbHashCode != jsonHashCode) {
                        parametersToUpdate.add(parameterImpl);
                    } else {
                        parametersToKeep.add(parameterImpl);
                    }
                } else {
                    // Parameter is not yet present in database yet and will have to be created
                    parameterImpl = this.getObjectMapper().treeToValue(parameterNode, ParameterImpl.class);
                    parametersToCreate.add(parameterImpl);
                }
            }
        }
    }

    protected String retrieveChanges(Boolean printArtifactsToBeKept, String JsonNodeName)
            throws JsonProcessingException {

        Map<String, Map<String, ParameterImpl>> all = new HashMap<>();

        all.put("CREATE", new HashMap<String, ParameterImpl>());
        for (ParameterImpl parameterImpl : parametersToCreate) {
            all.get("CREATE").put(parameterImpl.getName(), parameterImpl);
        }
        
        if (printArtifactsToBeKept) {
            all.put("KEEP", new HashMap<String, ParameterImpl>());
            for (ParameterImpl parameterImpl : parametersToKeep) {
                all.get("KEEP").put(parameterImpl.getName(), parameterImpl);
            }
        }

        all.put("UPDATE", new HashMap<String, ParameterImpl>());
        for (ParameterImpl parameterImpl : parametersToUpdate) {
            all.get("UPDATE").put(parameterImpl.getName(), parameterImpl);
        }

        return "\"" + JsonNodeName + "\":"
                + this.getObjectMapper().writer().withDefaultPrettyPrinter().writeValueAsString(all);
    }

    protected void applyCreate(Boolean printQuantities, Boolean isVirtual) {
        if (printQuantities) {
            System.out.println("    Keeping " + parametersToKeep.size() + " " + (isVirtual ? "physics" : "hardware")
                    + " parameters (table PARAMETERS)");
        }
        for (Parameter parameter : parametersToKeep) {
            LOGGER.debug("Keeping " + parameter.getName());
        }

        if (printQuantities) {
            System.out.println("    Creating " + parametersToCreate.size() + " " + (isVirtual ? "physics" : "hardware")
                    + " parameters (table PARAMETERS)");
        }
        for (Parameter parameter : parametersToCreate) {
            LOGGER.debug("Creating " + parameter.getName());

            // Save parameter to database
            ArrayList<Parameter> parameters = new ArrayList<>();
            parameters.add(parameter);
            parameterService.saveParameters(parameters);
        }
    }

    protected void applyDelete(Boolean printQuantities, Boolean isVirtual) {
        if (printQuantities) {
            System.out.println("    Removing 0 " + (isVirtual ? "physics" : "hardware")
                    + " parameters (table PARAMETERS) since this has not been implemented");
        }
    }

    protected void applyUpdate(Boolean printQuantities, Boolean isVirtual) {
        if (printQuantities) {
            System.out.println("    Updating " + parametersToUpdate.size() + " " + (isVirtual ? "physics" : "hardware")
                    + " parameters (table PARAMETERS)");
        }
        for (Parameter parameter : parametersToUpdate) {
            LOGGER.debug("Updating " + parameter.getName());

            // Update parameter in database
            ArrayList<Parameter> parameters = new ArrayList<>();
            parameters.add(parameter);
            parameterService.saveParameters(parameters);
        }
    }
}