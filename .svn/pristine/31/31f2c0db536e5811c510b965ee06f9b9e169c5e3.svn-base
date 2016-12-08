package de.gsi.cs.co.ap.lsa.setup.spi;

import java.util.HashMap;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Set;

import org.apache.commons.logging.Log;
import org.apache.commons.logging.LogFactory;
import org.springframework.transaction.TransactionDefinition;
import org.springframework.transaction.TransactionStatus;

import cern.lsa.client.ServiceLocator;
import cern.lsa.domain.devices.Device;
import cern.lsa.domain.devices.DeviceMetaTypeEnum;
import cern.lsa.domain.devices.factory.DevicesRequestBuilder;
import cern.lsa.domain.devices.spi.DeviceImpl;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.JsonNode;

import de.gsi.cs.co.ap.lsa.setup.json.JsonNodeNames;

/**
 * @author Raphael Mueller
 * @author Hanno Huether
 */
public class DeviceImportImpl extends ImportBaseImpl {

    private static final Log LOGGER = LogFactory.getLog(DeviceImportImpl.class);

    private final List<DeviceImpl> devicesToKeep = new LinkedList<>();
    private final List<DeviceImpl> devicesToRemove = new LinkedList<>();
    private final List<DeviceImpl> devicesToUpdate = new LinkedList<>();
    private final List<DeviceImpl> devicesToCreate = new LinkedList<>();

    private JsonNode devicesNode;

    /**
     * Constructor. Gets database access and devices node ready for import.
     * 
     * @param root Root node of JSON-file to import
     */
    public DeviceImportImpl(JsonNode root) {
        super(root);

        this.devicesNode = root.get(JsonNodeNames.DEVICES);
    }

    /**
     * The importer has to decide whether a {@link Device} that is already present in the database has to be updated.
     * Therefore, a method that calculates a hash code is needed. For {@link Device}s, equality (in the sense of an
     * "equals" method) is defined as value equality of the ID. So it is not possible to use a hash code method that is
     * already present. A completely generalized version that uses reflection or another equivalent approach would not
     * necessarily work as only specific attributes (i.e. those that are actually imported) shall be considered here.
     * 
     * @param device {@link Device} which the hash code shall be calculated for. May be null.
     * @return Hash code for the {@link Device} specified
     */
    private int hashCodeForImport(Device device) {
        final int prime = 31;
        int result = 1;
        result = prime * result + ((device.getName() == null) ? 0 : device.getName().hashCode());
        result = prime * result
                + ((device.getAcceleratorZone() == null) ? 0 : device.getAcceleratorZone().getName().hashCode());
        result = prime * result + ((device.getDescription() == null) ? 0 : device.getDescription().hashCode());
        result = prime * result + ((device.getAlias() == null) ? 0 : device.getAlias().hashCode());
        result = prime * result + ((device.getDeviceType() == null) ? 0 : device.getDeviceType().getName().hashCode());
        result = prime * result + new Boolean(device.isMultiplexed()).hashCode();

        return result;
    }

    /**
     * Checks that all {@link Device}s specified in the JSON file actually are present in the database. If this is not
     * the case, e.g. one more {@code Device}s were not imported correctly, a {@link RuntimeException} is thrown.
     * 
     * @throws JsonProcessingException In case that something goes wrong with deserialization of the JSON file
     * @throws RuntimeException In case that the import did not achieve the expected results
     */
    @Override
    public void checkImport() throws JsonProcessingException {
        System.out.println("    Checking import of devices...");

        Iterator<String> deviceNames = devicesNode.fieldNames();
        while (deviceNames.hasNext()) {
            String deviceName = deviceNames.next();
            JsonNode deviceNode = devicesNode.get(deviceName);

            this.addValueToInjectIntoDeserializer(JsonNodeNames.DEVICE_NAME, deviceName);
            DeviceImpl deviceWithTargetValues = this.getObjectMapper().treeToValue(deviceNode, DeviceImpl.class);

            Device deviceWithDatabaseValues = ImportBaseImpl.getDeviceservice().findDevice(deviceName);

            if (hashCodeForImport(deviceWithTargetValues) != hashCodeForImport(deviceWithDatabaseValues)) {
                throw new RuntimeException(
                        String.format(ImportMessages.ERROR_NOT_IMPORTED_CORRECTLY_DEVICE, deviceName));
            }
        }

        System.out.println("    ...Devices were imported correctly.");
    }

    @Override
    public void evaluate() throws JsonProcessingException {
        Set<Device> devicesList = ImportBaseImpl.getDeviceservice().findDevices(
                DevicesRequestBuilder.byParticleTransfer(this.getParticleTransfer()));

        Iterator<String> deviceNames = devicesNode.fieldNames();

        while (deviceNames.hasNext()) {
            String deviceName = deviceNames.next();
            JsonNode deviceNode = devicesNode.get(deviceName);

            // Inject the device name into the deserialization context. This is needed since we cannot access the parent
            // node within the deserializer.
            this.addValueToInjectIntoDeserializer(JsonNodeNames.DEVICE_NAME, deviceName);

            DeviceImpl deviceImpl = (DeviceImpl) ImportBaseImpl.getDeviceservice().findDevice(deviceName);
            if (deviceImpl != null) {
                // Device is present in database, check if it needs to be updated
                int dbHashCode = hashCodeForImport(deviceImpl);

                deviceImpl = this.getObjectMapper().readerForUpdating(deviceImpl)
                        .treeToValue(deviceNode, DeviceImpl.class);

                int jsonHashCode = hashCodeForImport(deviceImpl);

                if (dbHashCode != jsonHashCode) {
                    // Device has changed
                    devicesToUpdate.add(deviceImpl);
                } else {
                    devicesToKeep.add(deviceImpl);
                }
            } else {
                // Device is not present in database yet and will have to be created
                devicesToCreate.add(this.getObjectMapper().treeToValue(deviceNode, DeviceImpl.class));
            }
        }

        // Actual hardware devices are always kept, virtual devices may be deleted. This is because DeviceImportImpl
        // can only import virtual devices, so consequently, it may only delete virtual devices. To import actual
        // hardware devices, de.gsi.cs.co.ap.lsa.setup.dbimport.devices.DeviceImport is used.
        for (Device device : devicesList) {
            if (!devicesToUpdate.contains(device) && !devicesToCreate.contains(device)
                    && !devicesToKeep.contains(device)) {
                if (device.getDeviceType().getMetaType().equals(DeviceMetaTypeEnum.ACTUAL)) {
                    devicesToKeep.add((DeviceImpl) device);
                } else {
                    devicesToRemove.add((DeviceImpl) device);
                }
            }
        }
    }

    @Override
    public String retrieveChanges(Boolean printArtifactsToBeKept) throws JsonProcessingException {

        Map<String, Map<String, DeviceImpl>> all = new HashMap<>();

        all.put("CREATE", new HashMap<String, DeviceImpl>());
        for (DeviceImpl device : devicesToCreate) {
            all.get("CREATE").put(device.getName(), device);
        }

        if (printArtifactsToBeKept) {
            all.put("KEEP", new HashMap<String, DeviceImpl>());
            for (DeviceImpl device : devicesToKeep) {
                all.get("KEEP").put(device.getName(), device);
            }
        }

        all.put("UPDATE", new HashMap<String, DeviceImpl>());
        for (DeviceImpl device : devicesToUpdate) {
            all.get("UPDATE").put(device.getName(), device);
        }

        all.put("REMOVE", new HashMap<String, DeviceImpl>());
        for (DeviceImpl device : devicesToRemove) {
            all.get("REMOVE").put(device.getName(), device);
        }

        return "\"DEVICES\":" + this.getObjectMapper().writer().withDefaultPrettyPrinter().writeValueAsString(all);
    }

    @Override
    public void applyDelete(Boolean printQuantities) {
        if (printQuantities) {
            System.out.println("    Removing " + devicesToRemove.size() + " devices (table DEVICES)");
        }
        for (DeviceImpl device : devicesToRemove) {
            LOGGER.debug("Removing " + device.getName());

            // Not being able to delete a device shall not affect the whole transaction, so it gets its own (nested)
            // one. Otherwise, the whole transaction would be marked as "rollback only" and we could not persist
            // everything else.
            TransactionStatus transactionStatus = ServiceLocator
                    .getTransaction(TransactionDefinition.PROPAGATION_NESTED);
            // It's necessary to tell the transaction manager that when a nested transaction fails, that shall not
            // affect the parent transaction.
            ServiceLocator.setTransactionGlobalRollbackOnParticipationFailure(false);
            try {
                ImportBaseImpl.getDeviceservice().deleteDevice(device);
                ServiceLocator.commitTransaction(transactionStatus);
            } catch (Exception e) {
                System.out.println("    Warning: Device " + device.getName()
                        + " could not be removed! Error message was: '" + e.getMessage() + "'.");
                ServiceLocator.rollBackTransaction(transactionStatus);
            }
            ServiceLocator.setTransactionGlobalRollbackOnParticipationFailure(true);
        }
    }

    @Override
    public void applyCreate(Boolean printQuantities) {
        if (printQuantities) {
            System.out.println("    Keeping " + devicesToKeep.size() + " devices (table DEVICES)");
        }
        for (DeviceImpl deviceImpl : devicesToKeep) {
            LOGGER.debug("Keeping " + deviceImpl.getName());
        }

        if (printQuantities) {
            System.out.println("    Creating " + devicesToCreate.size() + " devices (table DEVICES)");
        }
        for (DeviceImpl deviceImpl : devicesToCreate) {
            LOGGER.debug("Creating " + deviceImpl.getName());

            ImportBaseImpl.getDeviceservice().saveDevice(deviceImpl);
        }
    }

    @Override
    public void applyUpdate(Boolean printQuantities) {
        if (printQuantities) {
            System.out.println("    Updating " + devicesToUpdate.size() + " devices (table DEVICES)");
        }
        for (DeviceImpl deviceImpl : devicesToUpdate) {
            LOGGER.debug("Updating " + deviceImpl.getName());

            ImportBaseImpl.getDeviceservice().saveDevice(deviceImpl);
        }
    }

}
