package de.gsi.cs.co.ap.lsa.setup.spi;

import java.util.Date;
import java.util.HashMap;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;

import org.apache.commons.logging.Log;
import org.apache.commons.logging.LogFactory;

import cern.accsoft.commons.util.Nameds;
import cern.lsa.client.ParameterService;
import cern.lsa.client.ServiceLocator;
import cern.lsa.domain.devices.spi.ParameterGroupImpl;
import cern.lsa.domain.settings.ParameterGroup;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;

import de.gsi.cs.co.ap.lsa.setup.json.JsonNodeNames;

/**
 * @author hhuether
 */
public class ParameterGroupImportImpl extends ImportBaseImpl {

    private static final Log LOGGER = LogFactory.getLog(ParameterGroupImportImpl.class);

    // LSA services
    private final ParameterService parameterService;

    private JsonNode parameterGroupsNode;
    private final ObjectMapper mapper = new ObjectMapper();
    private final List<ParameterGroupImpl> parameterGroupsToKeep = new LinkedList<ParameterGroupImpl>();
    private final List<ParameterGroupImpl> parameterGroupsToCreate = new LinkedList<ParameterGroupImpl>();

    public ParameterGroupImportImpl(JsonNode root) {
        super(root);

        this.parameterGroupsNode = root.get(JsonNodeNames.SYSTEM_CONFIGS);

        parameterService = ServiceLocator.getService(ParameterService.class);
    }

    public void applyCreate(Boolean printQuantities) {
        if (printQuantities) {
            System.out.println("    Keeping " + parameterGroupsToKeep.size()
                    + " parameter groups (table PARAMETER_GROUPS)");
        }
        for (ParameterGroupImpl parameterGroupImpl : parameterGroupsToKeep) {
            LOGGER.debug("Keeping " + parameterGroupImpl.getName());
        }

        if (printQuantities) {
            System.out.println("    Creating " + parameterGroupsToCreate.size()
                    + " parameter groups (table PARAMETER_GROUPS)");
        }
        for (ParameterGroupImpl parameterGroupImpl : parameterGroupsToCreate) {
            LOGGER.debug("Creating " + parameterGroupImpl.getName());
            parameterService.saveParameterGroup(parameterGroupImpl);
        }
    }

    public void applyDelete(Boolean printQuantities) {
        // Parameter groups shall not be deleted for now because they "span" import scripts, i.e. a parameter group
        // could contain parameters from more than one import script.
        if (printQuantities) {
            System.out
                    .println("    Removing 0 parameter groups (table PARAMETER_GROUPS) since parameter groups are not deleted by design");
        }
    }

    @Override
    public void applyUpdate(Boolean printQuantities) {
        // Parameter groups are not updated since there is no data imported except the name of the group. They can just
        // be created, kept or deleted.
    }

    /**
     * Checks that all {@link ParameterGroup}s specified in the JSON file actually are present in the database. If this
     * is not the case, e.g. one more {@code ParameterGroup}s were not imported correctly, a {@link RuntimeException} is
     * thrown.
     * 
     * @throws RuntimeException In case that the import did not achieve the expected results
     */
    public void checkImport() {
        System.out.println("    Checking import of parameter groups...");

        if (parameterGroupsNode != null) {
            Iterator<String> parameterNames = parameterGroupsNode.fieldNames();
            while (parameterNames.hasNext()) {
                final String parameterName = parameterNames.next();

                // One parameter can be in more than one group
                Iterator<String> parameterGroupNames = parameterGroupsNode.get(parameterName).fieldNames();
                while (parameterGroupNames.hasNext()) {
                    final String parameterGroupName = parameterGroupNames.next();

                    ParameterGroup parameterGroup = Nameds.findByName(
                            parameterService.findParameterGroupsByAccelerator(this.getAccelerator()),
                            parameterGroupName);

                    if (parameterGroup == null) {
                        throw new RuntimeException("Error while checking import: Parameter group '"
                                + parameterGroupName + "' was not imported correctly.");
                    }
                }
            }

            System.out.println("    ...Parameter groups were imported correctly.");
        } else {
            System.out.println("    ...There were no parameter groups to be imported.");
        }
    }

    public void evaluate() throws JsonProcessingException {
        if (parameterGroupsNode != null) {
            Iterator<String> parameterNames = parameterGroupsNode.fieldNames();
            while (parameterNames.hasNext()) {
                final String parameterName = parameterNames.next();

                // One parameter can be in more than one group
                Iterator<String> parameterGroupNames = parameterGroupsNode.get(parameterName).fieldNames();
                while (parameterGroupNames.hasNext()) {
                    final String parameterGroupName = parameterGroupNames.next();

                    // Determine if group already exists
                    ParameterGroupImpl parameterGroupImpl = (ParameterGroupImpl) Nameds.findByName(
                            parameterService.findParameterGroupsByAccelerator(this.getAccelerator()),
                            parameterGroupName);

                    if (parameterGroupImpl == null) {
                        // parameter group does not exist and will have to be created
                        parameterGroupImpl = new ParameterGroupImpl();
                        parameterGroupImpl.setId(-1);
                        parameterGroupImpl.setName(parameterGroupName);
                        parameterGroupImpl.setAccelerator(this.getAccelerator());
                        parameterGroupImpl.setCreateDate(new Date());
                        if (!parameterGroupsToCreate.contains(parameterGroupImpl)) {
                            parameterGroupsToCreate.add(parameterGroupImpl);
                        }
                    } else {
                        // parameter group already exists and will be kept
                        if (!parameterGroupsToKeep.contains(parameterGroupImpl)) {
                            parameterGroupsToKeep.add(parameterGroupImpl);
                        }
                    }
                }
            }
        }
    }

    public String retrieveChanges(Boolean printArtifactsToBeKept) throws JsonProcessingException {

        Map<String, Map<String, ParameterGroupImpl>> all = new HashMap<String, Map<String, ParameterGroupImpl>>();

        all.put("CREATE", new HashMap<String, ParameterGroupImpl>());
        for (ParameterGroupImpl parameterGroupImpl : parameterGroupsToCreate) {
            all.get("CREATE").put(parameterGroupImpl.getName(), parameterGroupImpl);
        }

        if (printArtifactsToBeKept) {
            all.put("KEEP", new HashMap<String, ParameterGroupImpl>());
            for (ParameterGroupImpl parameterGroupImpl : parameterGroupsToKeep) {
                all.get("KEEP").put(parameterGroupImpl.getName(), parameterGroupImpl);
            }
        }

        return "\"PARAMETER_GROUPS\":" + mapper.writer().withDefaultPrettyPrinter().writeValueAsString(all);
    }
}
