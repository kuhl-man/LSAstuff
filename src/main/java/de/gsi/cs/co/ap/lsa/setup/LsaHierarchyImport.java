package de.gsi.cs.co.ap.lsa.setup;

import java.io.File;
import java.io.IOException;
import java.net.URISyntaxException;
import java.net.URL;

import org.springframework.transaction.TransactionStatus;

import cern.lsa.client.ServiceLocator;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;

import de.gsi.cs.co.ap.lsa.setup.spi.DeviceImportImpl;
import de.gsi.cs.co.ap.lsa.setup.spi.LinkRuleConfigImportImpl;
import de.gsi.cs.co.ap.lsa.setup.spi.ParameterGroupImportImpl;
import de.gsi.cs.co.ap.lsa.setup.spi.ParameterGroupParameterImportImpl;
import de.gsi.cs.co.ap.lsa.setup.spi.ParameterHardwareImportImpl;
import de.gsi.cs.co.ap.lsa.setup.spi.ParameterPhysicsImportImpl;
import de.gsi.cs.co.ap.lsa.setup.spi.ParameterRelationImportImpl;

/**
 * This class is used to import different artifacts from a JSON file into the LSA database. Where applicable, these
 * artifacts are valid for the particle transfer specified in the "HIERARCHY_DETAILS" node.
 * <p>
 * As of 2014-04-22, the following artifact types may be imported:
 * <ul>
 * <li>Virtual (non-hardware) devices (node "DEVICES")</li>
 * <li>Hardware parameters (node "PARAMETERS_HARDWARE")</li>
 * <li>Physics parameters (node "PARAMETERS_PHYSICS")</li>
 * <li>Parameter groups and assignments of parameters to them (node "SYSTEM_CONFIGS")</li>
 * <li>Parameter relations (node "PARAMETER_RELATIONS")</li>
 * <li>Link rule configurations (node "LINKRULES_CONFIGS")</li>
 * </ul>
 * <p>
 * For an example of what the JSON node structure is supposed to look like, please see an existing file in the resources
 * folder.
 * </p>
 *
 * @author rmueller
 * @author hhuether
 */
public class LsaHierarchyImport {

    /**
     * Defines what is being done during import. "EVALUATE" mode reads the database and prints proposed changes to the
     * standard output stream. Everything is done just like the real import process, but changes aren't committed to the
     * database. Instead, a rollback is done. "APPLY" is the real thing and actually makes changes to the database.
     */
    public static enum OperationMode {
        EVALUATE,
        APPLY
    }

    /**
     * Usage advice printed to standard output stream in case of missing or too many arguments
     */
    private static final String HOW_TO_USE = "\nLsaHierarchyImport\n" //
            + "------------------\n\n" //
            + "Arguments:\n\n" //
            + "'-e': Evaluate and print proposed changes to hierarchy in database\n"
            + "'-ek': Like -e, but also print which artifacts would be kept (not just those to be changed)\n"
            + "'-a': Apply changes to database\n" + "<filename> name of the JSON file to import\n\n"
            + "Example: '-a /home/bel/hhuether/lnx/temp/lh-CRYRINGTEST-CRYRING_RING-1.0.0.json'\n";

    /**
     * Does a complete import run from a JSON file
     *
     * @param operationMode The {@link OperationMode operation mode} to be used during import
     * @param printArtifactsToBeKept If true, artifacts that will be kept (= no changes) during import are output to
     *            stdout when in evaluation mode.
     * @param filename The name of the JSON file to be imported
     * @return True if the import was successful, otherwise false.
     */
    public static boolean importFromJson(final OperationMode operationMode, final boolean printArtifactsToBeKept,
            final String filename) {
        boolean importRunSuccessful = false;

        System.out.println("  START importFromJson()");

        // Begin transaction on LSA application context
        final TransactionStatus transactionStatus = ServiceLocator.getTransaction();

        try {
            final JsonNode root = readJsonFile(filename);

            System.out.println();

            final DeviceImportImpl deviceImportImpl = new DeviceImportImpl(root);
            deviceImportImpl.evaluate();
            if (operationMode == OperationMode.EVALUATE) {
                System.out.println(deviceImportImpl.retrieveChanges(printArtifactsToBeKept));
            }
            // Import devices, don't delete devices yet because of dependent records
            deviceImportImpl.applyCreate(operationMode == OperationMode.APPLY);
            deviceImportImpl.applyUpdate(operationMode == OperationMode.APPLY);

            System.out.println();

            final ParameterGroupImportImpl parameterGroupsImportImpl = new ParameterGroupImportImpl(root);
            parameterGroupsImportImpl.evaluate();
            if (operationMode == OperationMode.EVALUATE) {
                System.out.println(parameterGroupsImportImpl.retrieveChanges(printArtifactsToBeKept));
            }
            parameterGroupsImportImpl.applyCreate(operationMode == OperationMode.APPLY);
            parameterGroupsImportImpl.applyDelete(operationMode == OperationMode.APPLY);

            System.out.println();

            final ParameterPhysicsImportImpl parameterPhysicsImportImpl = new ParameterPhysicsImportImpl(root);
            parameterPhysicsImportImpl.evaluate();
            if (operationMode == OperationMode.EVALUATE) {
                System.out.println(parameterPhysicsImportImpl.retrieveChanges(printArtifactsToBeKept));
            }
            parameterPhysicsImportImpl.applyCreate(operationMode == OperationMode.APPLY);
            parameterPhysicsImportImpl.applyUpdate(operationMode == OperationMode.APPLY);
            parameterPhysicsImportImpl.applyDelete(operationMode == OperationMode.APPLY);

            System.out.println();

            final ParameterHardwareImportImpl parameterHardwareImportImpl = new ParameterHardwareImportImpl(root);
            parameterHardwareImportImpl.evaluate();
            if (operationMode == OperationMode.EVALUATE) {
                System.out.println(parameterHardwareImportImpl.retrieveChanges(printArtifactsToBeKept));
            }
            parameterHardwareImportImpl.applyCreate(operationMode == OperationMode.APPLY);
            parameterHardwareImportImpl.applyUpdate(operationMode == OperationMode.APPLY);
            parameterHardwareImportImpl.applyDelete(operationMode == OperationMode.APPLY);

            System.out.println();

            // Now that parameters are cleaned up, go and delete devices that are not needed anymore
            deviceImportImpl.applyDelete(operationMode == OperationMode.APPLY);

            System.out.println();

            final ParameterRelationImportImpl parameterRelationImportImpl = new ParameterRelationImportImpl(root);
            parameterRelationImportImpl.evaluate();
            if (operationMode == OperationMode.EVALUATE) {
                System.out.println(parameterRelationImportImpl.retrieveChanges(printArtifactsToBeKept));
            }
            parameterRelationImportImpl.applyCreate(operationMode == OperationMode.APPLY);
            parameterRelationImportImpl.applyUpdate(operationMode == OperationMode.APPLY);
            parameterRelationImportImpl.applyDelete(operationMode == OperationMode.APPLY);

            System.out.println();

            final ParameterGroupParameterImportImpl parameterGroupParameterImportImpl = new ParameterGroupParameterImportImpl(
                    root);
            parameterGroupParameterImportImpl.evaluate();
            if (operationMode == OperationMode.EVALUATE) {
                System.out.println(parameterGroupParameterImportImpl.retrieveChanges(printArtifactsToBeKept));
            }
            parameterGroupParameterImportImpl.applyCreate(operationMode == OperationMode.APPLY);
            parameterGroupParameterImportImpl.applyDelete(operationMode == OperationMode.APPLY);

            System.out.println();

            final LinkRuleConfigImportImpl linkRuleConfigImportImpl = new LinkRuleConfigImportImpl(root);
            linkRuleConfigImportImpl.evaluate();
            if (operationMode == OperationMode.EVALUATE) {
                System.out.println(linkRuleConfigImportImpl.retrieveChanges(printArtifactsToBeKept));
            }
            linkRuleConfigImportImpl.applyCreate(operationMode == OperationMode.APPLY);
            linkRuleConfigImportImpl.applyUpdate(operationMode == OperationMode.APPLY);
            linkRuleConfigImportImpl.applyDelete(operationMode == OperationMode.APPLY);

            System.out.println();

            deviceImportImpl.checkImport();
            parameterGroupsImportImpl.checkImport();
            parameterPhysicsImportImpl.checkImport();
            parameterHardwareImportImpl.checkImport();
            parameterRelationImportImpl.checkImport();
            parameterGroupParameterImportImpl.checkImport();
            linkRuleConfigImportImpl.checkImport();

            if (operationMode == OperationMode.APPLY) {
                ServiceLocator.commitTransaction(transactionStatus);
                System.out.println("    COMMIT completed.");
            }

            // Import run successful
            System.out.println("    SUCCESSFUL importFromJson()");
            importRunSuccessful = true;
        } catch (final Exception e) {
            e.printStackTrace();

            ServiceLocator.rollBackTransaction(transactionStatus);
            System.out.println("    ROLLBACK completed. Database has NOT been changed.");
        } finally {
            if (operationMode == OperationMode.EVALUATE
                    // Transaction may already have been rolled back because of an exception
                    && !transactionStatus.isCompleted()) {
                ServiceLocator.rollBackTransaction(transactionStatus);
                System.out.println("    ROLLBACK completed. Database has NOT been changed.");
            }
        }

        System.out.println("  STOP importFromJson()");
        return importRunSuccessful;
    }

    /**
     * @param deviceImportImpl The instance of {@link DeviceImportImpl} that has been used to perform the import
     * @throws JsonProcessingException In case that something goes wrong with deserialization of the JSON file
     * @see DeviceImportImpl
     */
    public static void checkDevicesImport(final DeviceImportImpl deviceImportImpl) throws JsonProcessingException {
        deviceImportImpl.checkImport();
    }

    /**
     * @param args Used to set operation mode and source file. See contents of {@link LsaHierarchyImport#HOW_TO_USE}.
     */
    public static void main(final String[] args) {
        System.out.println("START main()");

        if (args.length == 2) {
            final String filename = args[1];

            if (args[0].equals("-e") || args[0].equals("-ek")) {
                final OperationMode operationMode = OperationMode.EVALUATE;
                System.out
                        .println("  MODE set to EVALUATE and output proposed changes. Database is not being updated.");

                final boolean printArtifactsToBeKept = args[0].equals("-ek");

                importFromJson(operationMode, printArtifactsToBeKept, filename);
            } else if (args[0].equals("-a")) {
                final OperationMode operationMode = OperationMode.APPLY;
                System.out.println("  MODE set to evaluate and APPLY changes. DATABASE WILL BE CHANGED.");
                importFromJson(operationMode, false, filename);
            }
        } else {
            System.out.println(HOW_TO_USE);
        }

        System.out.println("STOP main()");
    }

    /**
     * Reads a JSON file and returns a JSON node so it can be further processed. The file to be imported may either be a
     * resource of the java project or a located somewhere in the file system.
     *
     * @param filename name of the JSON file to be imported
     * @return JSON node to be further processed
     * @throws URISyntaxException In case something goes wrong with accessing resources
     * @throws JsonProcessingException In case JSON in the file specified cannot be parsed
     * @throws IOException In case the file specified cannot be accessed
     */
    private static JsonNode readJsonFile(final String filename)
            throws URISyntaxException, JsonProcessingException, IOException {
        File jsonFile = null;

        // try to find file within resources
        final URL url = LsaHierarchyImport.class.getClassLoader().getResource(filename);
        if (url != null) {
            jsonFile = new File(url.toURI());
        }

        // try to find file with absolute file path
        if (jsonFile == null) {
            jsonFile = new File(filename);
        }

        final ObjectMapper mapper = new ObjectMapper();
        return mapper.readTree(jsonFile);
    }
}
