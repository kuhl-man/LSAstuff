package de.gsi.cs.co.ap.lsa.setup.spi;

import java.util.HashMap;

import cern.accsoft.commons.domain.Accelerator;
import cern.accsoft.commons.domain.particletransfers.ParticleTransfer;
import cern.accsoft.commons.util.Nameds;
import cern.lsa.client.AcceleratorService;
import cern.lsa.client.DeviceService;
import cern.lsa.client.ServiceLocator;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.InjectableValues;
import com.fasterxml.jackson.databind.JsonNode;

import de.gsi.cs.co.ap.lsa.setup.json.HierarchyObjectMapper;
import de.gsi.cs.co.ap.lsa.setup.json.JsonNodeNames;

/**
 * @author hhuether
 */
abstract class ImportBaseImpl {

    // LSA services
    private static final AcceleratorService acceleratorService = ServiceLocator.getService(AcceleratorService.class);
    private static final DeviceService deviceService = ServiceLocator.getService(DeviceService.class);

    // Domain objects needed in multiple Importer classes
    private final Accelerator accelerator;
    private final ParticleTransfer particleTransfer;

    private final HashMap<String, Object> valuesToInjectIntoDeserializer;

    public ImportBaseImpl(JsonNode root) {
        JsonNode hierarchyDetailsNode = root.get(JsonNodeNames.HIERARCHY_DETAILS);
        this.accelerator = this.readAndFindAccelerator(hierarchyDetailsNode);
        this.particleTransfer = this.readAndFindParticleTransfer(hierarchyDetailsNode);

        valuesToInjectIntoDeserializer = new HashMap<>();
        valuesToInjectIntoDeserializer.put(JsonNodeNames.PARTICLE_TRANSFER, this.getParticleTransfer());
        valuesToInjectIntoDeserializer.put(JsonNodeNames.ACCELERATOR, this.getAccelerator());
    }

    /**
     * An extending class must implement this method to check if the artifacts that were to be imported are actually
     * present in the database and their field values are set correctly. If the importer also deletes artifacts, it must
     * also check that these are not to be found in the database anymore.
     * 
     * @throws JsonProcessingException In case that something goes wrong with deserialization of the JSON file
     * @throws RuntimeException In case that the import did not achieve the expected results
     */
    abstract public void checkImport() throws JsonProcessingException;

    /**
     * Extending classes must write the artifacts that are to be imported to the database within this method.
     * 
     * @param printQuantities If true, a message stating how many instances of the specific artifact were imported shall
     *            be written to stdout.
     */
    abstract public void applyCreate(Boolean printQuantities);

    /**
     * Extending classes must delete the artifacts that are to be removed from the database during the import process
     * within this method. Even if an importer class does not delete artifacts by design, it should state so when
     * {@code printQuantities} is true.
     * 
     * @param printQuantities If true, a message stating how many instances of the specific artifact were deleted shall
     *            be written to stdout.
     */
    abstract public void applyDelete(Boolean printQuantities);

    abstract public void applyUpdate(Boolean printQuantities);

    /**
     * Importers shall compare the JSON file to be imported and the contents of the database within this method. They
     * must evaluate, which artifacts are to be created, kept, updated or deleted when the {@link #applyCreate},
     * {@link #applyUpdate} and {@link #applyDelete} methods are called.
     * 
     * @throws JsonProcessingException In case anything goes wrong during deserialization of the JSON file
     */
    abstract public void evaluate() throws JsonProcessingException;

    /**
     * Users of the importer want to compare what the importer intends to do with what they expect it to do. For this
     * reason, there is an evaluation mode which prints the JSON artifacts selected for create or update operation to
     * stdout. Consequently, the implementing class must return the intended changes it gathered during execution of the
     * {@link #evaluate} as a JSON string method here.
     * 
     * @param printArtifactsToBeKept If false, the names of artifacts that are changed (created, updated, removed) are
     *            printed to stdout. If true, <i>additionally</i> the names of artifacts that are not changed, but just
     *            kept, are written to stdout.
     * @return A JSON string containing the artifacts to be created or updated in the same format of the input JSON
     *         file.
     * @throws JsonProcessingException In case anything goes wrong during serialization of the artifacts
     */
    abstract public String retrieveChanges(Boolean printArtifactsToBeKept) throws JsonProcessingException;

    /**
     * @return A static {@link DeviceService} reference
     */
    public static DeviceService getDeviceservice() {
        return deviceService;
    }

    public void addValueToInjectIntoDeserializer(String key, Object value) {
        valuesToInjectIntoDeserializer.put(key, value);
    }

    public HierarchyObjectMapper getObjectMapper() {
        final HierarchyObjectMapper hierarchyObjectMapper = new HierarchyObjectMapper();
        InjectableValues injectableValues = new InjectableValues.Std(valuesToInjectIntoDeserializer);
        hierarchyObjectMapper.setInjectableValues(injectableValues);

        return hierarchyObjectMapper;
    }

    /**
     * Reads value for ACCELERATOR in HIERARCHY_DETAILS and returns matching {@link Accelerator} by finding it through
     * the LSA API using {@link AcceleratorService}.
     * 
     * @param hierarchyDetailsNode JSON node which contains the accelerator name
     * @return {@code Accelerator} with matching name as in value of ACCELERATOR node
     */
    private Accelerator readAndFindAccelerator(JsonNode hierarchyDetailsNode) {
        JsonNode jsonNode = hierarchyDetailsNode.get(JsonNodeNames.ACCELERATOR);
        if (jsonNode == null) {
            throw new RuntimeException("ACCELERATOR has not been set in HIERARCHY_DETAILS");
        } else {
            Accelerator accelerator = acceleratorService.findAccelerator(jsonNode.asText());

            if (accelerator == null) {
                throw new RuntimeException("Accelerator '" + jsonNode.asText() + "' was not found in database.");
            }

            return accelerator;
        }
    }

    /**
     * @return The {@link Accelerator} for which artifacts are to be imported.
     * @see ImportBaseImpl#readAndFindAccelerator
     */
    protected Accelerator getAccelerator() {
        return this.accelerator;
    }

    /**
     * Reads value for PARTICLE_TRANSFER in HIERARCHY_DETAILS and returns matching {@link ParticleTransfer} by finding
     * it through the LSA API using {@link AcceleratorService}.
     * 
     * @param hierarchyDetailsNode JSON node which contains the particle transfer name
     * @return {@code ParticleTransfer} with matching name as in value of PARTICLE_TRANSFER node
     */
    protected ParticleTransfer readAndFindParticleTransfer(JsonNode hierarchyDetailsNode) {
        JsonNode jsonNode = hierarchyDetailsNode.get(JsonNodeNames.PARTICLE_TRANSFER);
        if (jsonNode == null) {
            throw new RuntimeException("PARTICLE_TRANSFER has not been set in HIERARCHY_DETAILS");
        } else {
            ParticleTransfer particleTransfer = Nameds.findByName(this.getAccelerator().getParticleTransfers(),
                    jsonNode.asText());

            if (particleTransfer == null) {
                throw new RuntimeException("Particle transfer '" + jsonNode.asText() + "' was not found in database.");
            }

            return particleTransfer;
        }
    }

    /**
     * @return The {@link ParticleTransfer} for which artifacts are to be imported.
     * @see ImportBaseImpl#readAndFindParticleTransfer
     */
    protected ParticleTransfer getParticleTransfer() {
        return this.particleTransfer;
    }
}
