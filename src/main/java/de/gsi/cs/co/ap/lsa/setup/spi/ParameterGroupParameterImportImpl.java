package de.gsi.cs.co.ap.lsa.setup.spi;

import java.util.ArrayList;
import java.util.Collection;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Set;

import org.apache.commons.logging.Log;
import org.apache.commons.logging.LogFactory;

import cern.accsoft.commons.util.Nameds;
import cern.lsa.client.ParameterService;
import cern.lsa.client.ServiceLocator;
import cern.lsa.domain.settings.Parameter;
import cern.lsa.domain.settings.ParameterGroup;
import cern.lsa.domain.settings.spi.ParameterImpl;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.JsonNode;

import de.gsi.cs.co.ap.lsa.setup.json.JsonNodeNames;

/**
 * This class is used to import the relation between the tables PARAMETERS and PARAMETER_GROUPS, that is to say which
 * parameters are in which groups. The relation is saved in the table PARAMETER_GROUP_PARAMETERS.
 * 
 * @author hhuether
 */
public class ParameterGroupParameterImportImpl extends ImportBaseImpl {

    private static final Log LOGGER = LogFactory.getLog(ParameterGroupParameterImportImpl.class);

    // LSA services
    private final ParameterService parameterService;

    private JsonNode parameterGroupsNode;
    private final List<ParameterImpl> parameterGroupParametersToKeep = new LinkedList<ParameterImpl>();
    private final List<ParameterImpl> parameterGroupParametersToCreate = new LinkedList<ParameterImpl>();
    private final List<ParameterImpl> parameterGroupParametersToRemove = new LinkedList<ParameterImpl>();

    public ParameterGroupParameterImportImpl(JsonNode root) {
        super(root);

        this.parameterGroupsNode = root.get(JsonNodeNames.SYSTEM_CONFIGS);

        parameterService = ServiceLocator.getService(ParameterService.class);
    }

    public void applyCreate(Boolean printQuantities) {
        if (printQuantities) {
            System.out.println(String.format(ImportMessages.STATUS_PARAMETER_GROUP_PARAMETER_KEEP_QUANTITY,
                    parameterGroupParametersToKeep.size()));
        }
        for (Parameter parameter : parameterGroupParametersToKeep) {
            LOGGER.debug(String.format(ImportMessages.DEBUG_PARAMETER_GROUP_PARAMETER_KEEP, parameter.getName(),
                    parameter.getParameterGroups().iterator().next()));
        }

        if (printQuantities) {
            System.out.println(String.format(ImportMessages.STATUS_PARAMETER_GROUP_PARAMETER_CREATE_QUANTITY,
                    parameterGroupParametersToCreate.size()));
        }

        for (Parameter parameter : parameterGroupParametersToCreate) {
            LOGGER.debug(String.format(ImportMessages.DEBUG_PARAMETER_GROUP_PARAMETER_CREATE, parameter.getName(),
                    parameter.getParameterGroups().iterator().next()));

            // Get parameter group object for creation (and checking that it exists) through the service method
            ParameterGroup parameterGroup = Nameds.findByName(
                    parameterService.findParameterGroupsByAccelerator(this.getAccelerator()), parameter
                            .getParameterGroups().iterator().next());

            // Parameter group must exist in database
            if (parameterGroup == null) {
                throw new RuntimeException(String.format(ImportMessages.ERROR_NOT_FOUND_PARAMETER_GROUP, parameter
                        .getParameterGroups().iterator().next()));
            }

            // Call service method
            Collection<String> parameterNames = new ArrayList<>();
            parameterNames.add(parameter.getName());
            parameterService.addParametersToParameterGroup(parameterGroup, parameterNames);
        }
    }

    public void applyDelete(Boolean printQuantities) {
        if (printQuantities) {
            System.out.println(String.format(ImportMessages.STATUS_PARAMETER_GROUP_PARAMETER_REMOVE_QUANTITY,
                    parameterGroupParametersToRemove.size()));
        }

        for (Parameter parameter : parameterGroupParametersToRemove) {
            LOGGER.debug(String.format(ImportMessages.DEBUG_PARAMETER_GROUP_PARAMETER_REMOVE, parameter.getName(),
                    parameter.getParameterGroups().iterator().next()));

            // Get parameter group object for creation (and checking that it exists) through the service method
            ParameterGroup parameterGroup = Nameds.findByName(
                    parameterService.findParameterGroupsByAccelerator(this.getAccelerator()), parameter
                            .getParameterGroups().iterator().next());

            // Parameter group must exist in database
            if (parameterGroup == null) {
                throw new RuntimeException(String.format(ImportMessages.ERROR_NOT_FOUND_PARAMETER_GROUP, parameter
                        .getParameterGroups().iterator().next()));
            }

            // Call service method
            Collection<String> parameterNames = new ArrayList<>();
            parameterNames.add(parameter.getName());
            parameterService.removeParametersFromParameterGroup(parameterGroup, parameterNames);
        }
    }

    /**
     * Checks that all {@link ParameterGroup}s specified in the JSON file actually are present in the database. If this
     * is not the case, e.g. one more {@code ParameterGroup}s were not imported correctly, a {@link RuntimeException} is
     * thrown.
     * 
     * @throws RuntimeException In case that the import did not achieve the expected results
     */
    public void checkImport() {
        System.out.println(ImportMessages.STATUS_CHECK_IMPORT_PARAMETER_GROUP_PARAMETER_STARTED);

        if (parameterGroupsNode != null) {
            Iterator<String> parameterNames = parameterGroupsNode.fieldNames();
            while (parameterNames.hasNext()) {
                final String parameterName = parameterNames.next();

                // One parameter can be in more than one group
                Iterator<String> parameterGroupNames = parameterGroupsNode.get(parameterName).fieldNames();
                HashSet<String> parameterGroupNamesFromJson = new HashSet<>();
                while (parameterGroupNames.hasNext()) {
                    parameterGroupNamesFromJson.add(parameterGroupNames.next());
                }

                while (parameterGroupNames.hasNext()) {
                    final String parameterGroupName = parameterGroupNames.next();

                    // Parameter group assignment not found
                    Parameter parameter = parameterService.findParameterByName(parameterName);
                    if (!parameter.getParameterGroups().contains(parameterGroupName)) {
                        throw new RuntimeException(String.format(
                                ImportMessages.ERROR_NOT_IMPORTED_CORRECTLY_PARAMETER_GROUP_PARAMETER_NOT_FOUND,
                                parameterName, parameterGroupName));
                    }

                    // Parameter is assigned to more or less groups than expected, which should mostly mean that a
                    // delete failed
                    if (parameter.getParameterGroups().size() != parameterGroupNamesFromJson.size()) {
                        throw new RuntimeException(
                                String.format(
                                        ImportMessages.ERROR_NOT_IMPORTED_CORRECTLY_PARAMETER_GROUP_PARAMETER_WRONG_NUMBER_OF_ASSIGNMENTS,
                                        parameterName, parameterGroupNamesFromJson.size(), parameter
                                                .getParameterGroups().size()));
                    }
                }
            }
            System.out.println(ImportMessages.STATUS_CHECK_IMPORT_PARAMETER_GROUP_PARAMETER_SUCCESSFUL);
        } else {
            System.out.println(ImportMessages.STATUS_CHECK_IMPORT_PARAMETER_GROUP_NOTHING_TO_IMPORT);
        }
    }

    public void evaluate() throws JsonProcessingException {
        if (parameterGroupsNode != null) {
            // Parameter names are on the first level
            Iterator<String> parameterNames = parameterGroupsNode.fieldNames();
            while (parameterNames.hasNext()) {
                String parameterName = parameterNames.next();

                // Find the parameter concerned. It has to exist in the database, since it should have been created
                // during parameter groups import
                Parameter parameter = parameterService.findParameterByName(parameterName);
                if (parameter == null) {
                    throw new RuntimeException(String.format(ImportMessages.ERROR_NOT_FOUND_PARAMETER, parameterName));
                }

                // Store which parameter groups the parameter is in
                Set<String> parameterGroupNamesFromDB = parameter.getParameterGroups();

                // One parameter can be in more than one group. Groups are on the second level of the JSON subtree.
                Iterator<String> parameterGroupsNodeIterator = parameterGroupsNode.get(parameterName).fieldNames();
                Set<String> parameterGroupNamesFromJson = new HashSet<>();
                while (parameterGroupsNodeIterator.hasNext()) {
                    parameterGroupNamesFromJson.add(parameterGroupsNodeIterator.next());
                }

                for (String parameterGroupNameFromJson : parameterGroupNamesFromJson) {
                    // Misuse a parameter object as a container to store which parameter and parameter group is
                    // concerned
                    Set<String> parameterGroupNameSet = new HashSet<String>();
                    parameterGroupNameSet.add(parameterGroupNameFromJson);
                    ParameterImpl parameterImpl = new ParameterImpl();
                    parameterImpl.setName(parameter.getName());
                    parameterImpl.setParameterGroups(parameterGroupNameSet);

                    if (!parameterGroupNamesFromDB.contains(parameterGroupNameFromJson)) {
                        // relation between parameter group and parameter does not exist yet and will have to be created
                        parameterGroupParametersToCreate.add(parameterImpl);
                    } else {
                        // parameter group already exists and will be kept
                        parameterGroupParametersToKeep.add(parameterImpl);
                    }
                }

                // For all parameter groups the parameter at hand is assigned to in the database
                for (String parameterGroupNameFromDB : parameterGroupNamesFromDB) {

                    // If a relation is present in the database, but not in the JSON file, it shall be removed.
                    if (!parameterGroupNamesFromJson.contains(parameterGroupNameFromDB)) {

                        // Build a set of parameter group names to hold the name of the group with which the relation
                        // shall be removed
                        HashSet<String> parameterGroupToRemove = new HashSet<>();
                        parameterGroupToRemove.add(parameterGroupNameFromDB);

                        // Misuse a parameter object to store the information which relation shall be removed
                        ParameterImpl parameterGroupParameterToRemove = new ParameterImpl();
                        parameterGroupParameterToRemove.setName(parameter.getName());
                        parameterGroupParameterToRemove.setParameterGroups(parameterGroupToRemove);
                        parameterGroupParametersToRemove.add(parameterGroupParameterToRemove);
                    }
                }
            }
        }
    }

    public String retrieveChanges(Boolean printArtifactsToBeKept) throws JsonProcessingException {
        // The last of the maps (<Object, Object>) does not do anything but make the standard JSON serializer generate
        // the output wanted. This way it is not necessary to write another custom serializer.
        Map<String, Map<String, Map<String, Map<Object, Object>>>> all = new HashMap<String, Map<String, Map<String, Map<Object, Object>>>>();

        all.put("CREATE", new HashMap<String, Map<String, Map<Object, Object>>>());
        for (ParameterImpl parameterImpl : parameterGroupParametersToCreate) {
            if (!all.get("CREATE").containsKey(parameterImpl.getName())) {
                all.get("CREATE").put(parameterImpl.getName(), new HashMap<String, Map<Object, Object>>());
            }
            all.get("CREATE").get(parameterImpl.getName())
                    .put(parameterImpl.getParameterGroups().iterator().next(), new HashMap<Object, Object>());
        }

        if (printArtifactsToBeKept) {
            all.put("KEEP", new HashMap<String, Map<String, Map<Object, Object>>>());
            for (ParameterImpl parameterImpl : parameterGroupParametersToKeep) {
                if (!all.get("KEEP").containsKey(parameterImpl.getName())) {
                    all.get("KEEP").put(parameterImpl.getName(), new HashMap<String, Map<Object, Object>>());
                }
                all.get("KEEP").get(parameterImpl.getName())
                        .put(parameterImpl.getParameterGroups().iterator().next(), new HashMap<Object, Object>());
            }
        }

        all.put("REMOVE", new HashMap<String, Map<String, Map<Object, Object>>>());
        for (ParameterImpl parameterImpl : parameterGroupParametersToRemove) {
            if (!all.get("REMOVE").containsKey(parameterImpl.getName())) {
                all.get("REMOVE").put(parameterImpl.getName(), new HashMap<String, Map<Object, Object>>());
            }
            all.get("REMOVE").get(parameterImpl.getName())
                    .put(parameterImpl.getParameterGroups().iterator().next(), new HashMap<Object, Object>());
        }

        return "\"" + JsonNodeNames.SYSTEM_CONFIGS + "\": "
                + this.getObjectMapper().writer().withDefaultPrettyPrinter().writeValueAsString(all);
    }

    @Override
    public void applyUpdate(Boolean printQuantities) {
        // Since relations do not contain any data, they cannot be updated. They are just created, kept or deleted.
    }
}
