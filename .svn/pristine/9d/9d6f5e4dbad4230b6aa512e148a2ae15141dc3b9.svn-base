package de.gsi.cs.co.ap.lsa.setup.spi;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Set;

import org.apache.commons.logging.Log;
import org.apache.commons.logging.LogFactory;

import cern.lsa.domain.devices.Device;
import cern.lsa.domain.devices.factory.DevicesRequestBuilder;
import cern.lsa.domain.optics.LogicalHardware;
import cern.lsa.domain.optics.spi.LogicalHardwareImpl;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.JsonNode;

import de.gsi.cs.co.ap.lsa.setup.json.JsonNodeNames;

/**
 * @author rmueller
 * @author hhuether
 */
public class LinkRuleConfigImportImpl extends ImportBaseImpl {

    private static final Log LOGGER = LogFactory.getLog(LinkRuleConfigImportImpl.class);

    private final List<LogicalHardware> logicalHardwareToCreate = new LinkedList<>();
    private final List<LogicalHardware> logicalHardwareToKeep = new LinkedList<>();
    private final List<LogicalHardware> logicalHardwareToUpdate = new LinkedList<>();

    private JsonNode linkRuleConfigsNode;

    /**
     * Constructor. Gets database access and link rule configurations node ready for import.
     * 
     * @param root Root node of JSON-file to import
     */
    public LinkRuleConfigImportImpl(JsonNode root) {
        super(root);

        this.linkRuleConfigsNode = root.get(JsonNodeNames.LINKRULES_CONFIGS);
    }

    private boolean equalsForImport(LogicalHardware logicalHardware1, LogicalHardware logicalHardware2) {

        if (!logicalHardware1.getLinkRuleName().equals(logicalHardware2.getLinkRuleName())) {
            return false;
        }

        return true;
    }

    /**
     * Checks that all link rule configurations specified in the JSON file were correctly written to the database. If
     * this is not the case, a {@link RuntimeException} is thrown.
     * 
     * @throws JsonProcessingException In case that something goes wrong with deserialization of the JSON file
     * @throws RuntimeException In case that the import did not achieve the expected results
     */
    public void checkImport() throws JsonProcessingException {
        System.out.println("    Checking import of link rule configurations...");

        Iterator<String> logicalHardwareNames = linkRuleConfigsNode.fieldNames();
        while (logicalHardwareNames.hasNext()) {
            String logicalHardwareName = logicalHardwareNames.next();
            JsonNode linkRuleConfigNode = linkRuleConfigsNode.get(logicalHardwareName);

            LogicalHardware logicalHardwareWithDatabaseValues = ImportBaseImpl
                    .getDeviceservice()
                    .findLogicalHardware(
                    		DevicesRequestBuilder.byDeviceNames(Arrays.asList(logicalHardwareName)))
                    .iterator().next();

            if (logicalHardwareWithDatabaseValues == null) {
                throw new RuntimeException(String.format(
                        ImportMessages.ERROR_NOT_IMPORTED_CORRECTLY_LINKRULES_CONFIG_LOGICAL_HARDWARE_NOT_FOUND,
                        logicalHardwareName));
            }

            LogicalHardware logicalHardwareWithTargetValues = this.getObjectMapper()
                    .readerForUpdating(logicalHardwareWithDatabaseValues)
                    .treeToValue(linkRuleConfigNode, LogicalHardware.class);

            if (!this.equalsForImport(logicalHardwareWithTargetValues, logicalHardwareWithDatabaseValues)) {
                throw new RuntimeException(String.format(ImportMessages.ERROR_NOT_IMPORTED_CORRECTLY_LINKRULES_CONFIG,
                        logicalHardwareName));
            }
        }

        System.out.println("    ...Link rule configurations were imported correctly.");
    }

    public void evaluate() throws JsonProcessingException {
        Iterator<String> linkRuleConfigs = linkRuleConfigsNode.fieldNames();

        while (linkRuleConfigs.hasNext()) {
            String logicalHardwareName = linkRuleConfigs.next();
            JsonNode logicalHardwareNode = linkRuleConfigsNode.get(logicalHardwareName);

            // Try to read logical hardware to be imported from DB (might already be present)
            LogicalHardware logicalHardwareFromDB = null;
            Set<LogicalHardware> logicalHardwaresFromDB = ImportBaseImpl.getDeviceservice().findLogicalHardware(
                    DevicesRequestBuilder.byDeviceNames(Arrays.asList(logicalHardwareName)));
            if (logicalHardwaresFromDB.size() > 0) {
                logicalHardwareFromDB = logicalHardwaresFromDB.iterator().next();
            }

            if (logicalHardwareFromDB != null) {
                // LogicalHardware is present in database, check if it needs to be updated
                LogicalHardware logicalHardwareFromJson = this.getObjectMapper()
                        .readerForUpdating(logicalHardwareFromDB)
                        .treeToValue(logicalHardwareNode, LogicalHardware.class);

                if (!this.equalsForImport(logicalHardwareFromDB, logicalHardwareFromJson)) {
                    // LogicalHardware has changed
                    logicalHardwareToUpdate.add(logicalHardwareFromJson);
                } else {
                    logicalHardwareToKeep.add(logicalHardwareFromJson);
                }
            } else {
                // LogicalHardware is not present in the database yet and will have to be created. There has to be a
                // Device present in the database that the additional attributes that a LogicalHardware has can be
                // related to.
                Device device = ImportBaseImpl.getDeviceservice().findDevice(logicalHardwareName);
                if (device == null) {
                    throw new RuntimeException(
                            String.format(ImportMessages.ERROR_NOT_FOUND_DEVICE, logicalHardwareName));
                }

                // Create a new LogicalHardware based on the Device that was found.
                LogicalHardwareImpl logicalHardwareImpl = new LogicalHardwareImpl(device);

                // Set default values for non-nullable columns
                logicalHardwareImpl.setLength(1);

                logicalHardwareToCreate.add(this.getObjectMapper().readerForUpdating(logicalHardwareImpl)
                        .treeToValue(logicalHardwareNode, LogicalHardware.class));
            }
        }
    }

    public String retrieveChanges(Boolean printArtifactsToBeKept) throws JsonProcessingException {

        Map<String, Map<String, LogicalHardware>> all = new HashMap<String, Map<String, LogicalHardware>>();

        all.put("CREATE", new HashMap<String, LogicalHardware>());
        for (LogicalHardware logicalHardware : logicalHardwareToCreate) {
            all.get("CREATE").put(logicalHardware.getName(), logicalHardware);
        }

        if (printArtifactsToBeKept) {
            all.put("KEEP", new HashMap<String, LogicalHardware>());
            for (LogicalHardware logicalHardware : logicalHardwareToKeep) {
                all.get("KEEP").put(logicalHardware.getName(), logicalHardware);
            }
        }

        all.put("UPDATE", new HashMap<String, LogicalHardware>());
        for (LogicalHardware logicalHardware : logicalHardwareToUpdate) {
            all.get("UPDATE").put(logicalHardware.getName(), logicalHardware);
        }

        return "\"" + JsonNodeNames.LINKRULES_CONFIGS + "\":"
                + this.getObjectMapper().writer().withDefaultPrettyPrinter().writeValueAsString(all);
    }

    public void applyDelete(Boolean printQuantities) {
        // Since link rule configuration is a mandatory column within the LSA database, it cannot be deleted,
        // but only created (i.e. a whole row in table "LOGICAL_HARDWARE_INFO" is created then), kept or updated.
        if (printQuantities) {
            System.out
                    .println("    Removing 0 link rule configurations (table LOGICAL_HARDWARE_INFO) since linkrule configurations are not deleted by design");
        }
    }

    public void applyCreate(Boolean printQuantities) {
        if (printQuantities) {
            System.out.println("    Keeping " + logicalHardwareToKeep.size()
                    + " link rule configurations (table LOGICAL_HARDWARE_INFO)");
        }
        for (LogicalHardware logicalHardware : logicalHardwareToKeep) {
            LOGGER.debug("Keeping link rule configuration for " + logicalHardware.getName());
        }

        if (printQuantities) {
            System.out.println("    Creating " + logicalHardwareToCreate.size()
                    + " link rule configurations (table LOGICAL_HARDWARE_INFO)");
        }
        for (LogicalHardware logicalHardware : logicalHardwareToCreate) {
            LOGGER.debug("Creating " + logicalHardware.getName());

            ImportBaseImpl.getDeviceservice().saveLogicalHardware(logicalHardware);
        }
    }

    public void applyUpdate(Boolean printQuantities) {
        if (printQuantities) {
            System.out.println("    Updating " + logicalHardwareToUpdate.size()
                    + " link rule configurations (table LOGICAL_HARDWARE_INFO)");
        }
        for (LogicalHardware logicalHardware : logicalHardwareToUpdate) {
            LOGGER.debug("Updating " + logicalHardware.getName());

            ImportBaseImpl.getDeviceservice().saveLogicalHardware(logicalHardware);
        }
    }
}
