package de.gsi.cs.co.ap.lsa.setup;

import java.util.Set;

import org.junit.Assert;
import org.junit.Test;

import cern.accsoft.commons.domain.Accelerator;
import cern.accsoft.commons.domain.particletransfers.ParticleTransfer;
import cern.accsoft.commons.domain.zones.AcceleratorZone;
import cern.accsoft.commons.value.Type;
import cern.accsoft.commons.value.spi.ValueDescriptorImpl;
import cern.lsa.domain.devices.DeviceTypeImplementation;
import cern.lsa.domain.devices.spi.DeviceImpl;
import cern.lsa.domain.devices.spi.DeviceTypeImpl;
import cern.lsa.domain.devices.spi.DeviceTypeVersionImpl;
import cern.lsa.domain.devices.spi.DeviceTypeVersionNumberImpl;
import cern.lsa.domain.settings.spi.ParameterImpl;
import cern.lsa.domain.settings.spi.ParameterTreeNodeImpl;
import cern.lsa.domain.settings.spi.ParameterTypeImpl;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.core.Version;
import com.fasterxml.jackson.databind.module.SimpleModule;

import de.gsi.cs.co.ap.lsa.setup.data.ParameterTreeNodeWithPositions;
import de.gsi.cs.co.ap.lsa.setup.json.DeviceDeserializer;
import de.gsi.cs.co.ap.lsa.setup.json.DeviceSerializer;
import de.gsi.cs.co.ap.lsa.setup.json.HierarchyObjectMapper;
import de.gsi.cs.co.ap.lsa.setup.json.ParameterDeserializer;
import de.gsi.cs.co.ap.lsa.setup.json.ParameterRelationDeserializer;
import de.gsi.cs.co.ap.lsa.setup.json.ParameterRelationSerializer;
import de.gsi.cs.co.ap.lsa.setup.json.ParameterSerializer;

/**
 * @author hhuether
 */
public class LsaHierarchyImportSerializationDeserializationTest {

    private class TestAcceleratorZone implements AcceleratorZone {

        @Override
        public String getName() {
            return "acceleratorZone";
        }

        @Override
        public Accelerator getAccelerator() {
            return null;
        }

        @Override
        public Set<ParticleTransfer> getParticleTransfers() {
            return null;
        }

    }

    public static String SERIALIZED_PARAMETER = "" //
            + "{\n" //
            + "  \"BELONGS_TO_FUNCTION_BPROC\" : true,\n" //
            + "  \"DEFAULT_HIERARCHY\" : \"defaultHierarchy\",\n" //
            + "  \"DEVICE_NAME\" : \"deviceName\",\n" //
            + "  \"IS_RESERVED_FOR_OP_EXPERTS\" : true,\n" //
            + "  \"MAX_DELTA\" : 1245.6789,\n" //
            + "  \"PARAMETER_TYPE_NAME\" : \"parameterTypeName\",\n" //
            + "  \"TRIMABLE\" : true,\n" //
            + "  \"X_PREC\" : 10,\n" //
            + "  \"Y_PREC\" : 5\n" //
            + "}";

    public static String SERIALIZED_PARAMETER_RELATION = "" //
            + "{\n" //
            + "  \"parent1\" : {\n" //
            + "    \"POSITION\" : 1\n" //
            + "  },\n" //
            + "  \"parent2\" : {\n" //
            + "    \"POSITION\" : null\n" //
            + "  }\n" //
            + "}";

    public static String SERIALIZED_DEVICE = "" //
            + "{\n" //
            + "  \"ACCELERATOR_ZONE\" : \"acceleratorZone\",\n" //
            + "  \"DESCRIPTION\" : \"description\",\n" //
            + "  \"DEVICE_ALIAS\" : \"deviceAlias\",\n" //
            + "  \"DEVICE_TYPE\" : \"deviceType\",\n" //
            + "  \"IS_MULTIPLEXED\" : true\n" //
            + "}";

    @Test
    public void testDeviceSerializer() throws JsonProcessingException {
        // Accelerator zone for device
        TestAcceleratorZone testAcceleratorZone = new TestAcceleratorZone();

        // Device type for device type version
        DeviceTypeImpl deviceTypeImpl = new DeviceTypeImpl(1, "deviceType");

        // Device type version for device
        DeviceTypeVersionImpl deviceTypeVersionImpl = new DeviceTypeVersionImpl(-1, deviceTypeImpl,
                DeviceTypeImplementation.LSA, new DeviceTypeVersionNumberImpl(1, 0));

        DeviceImpl deviceImpl = new DeviceImpl(-1, "deviceName");
        deviceImpl.setAcceleratorZone(testAcceleratorZone);
        deviceImpl.setDescription("description");
        deviceImpl.setAlias("deviceAlias");
        deviceImpl.setDeviceTypeVersion(deviceTypeVersionImpl);
        deviceImpl.setMultiplexed(true);

        // Serialize
        HierarchyObjectMapper hierarchyObjectMapper = new HierarchyObjectMapper();
        SimpleModule hierarchyModule = new SimpleModule("TestHierarchyModule", Version.unknownVersion());
        hierarchyModule.addSerializer(DeviceImpl.class, new DeviceSerializer());
        hierarchyModule.addDeserializer(DeviceImpl.class, new DeviceDeserializer());
        String serializedDevice = hierarchyObjectMapper.writer().withDefaultPrettyPrinter()
                .writeValueAsString(deviceImpl);

        // Check serialization result
        Assert.assertEquals(LsaHierarchyImportSerializationDeserializationTest.SERIALIZED_DEVICE, serializedDevice);
    }

    @Test
    public void testParameterSerializer() throws JsonProcessingException {
        // Device for parameter
        DeviceImpl deviceImpl = new DeviceImpl(-1, "deviceName");

        // Value type for parameter type
        Type type = Type.DOUBLE;

        // Parameter type for parameter
        ParameterTypeImpl parameterTypeImpl = new ParameterTypeImpl();
        parameterTypeImpl.setName("parameterTypeName");
        parameterTypeImpl.setValueType(type);

        // Value descriptor for parameter
        ValueDescriptorImpl valueDescriptorImpl = new ValueDescriptorImpl();
        valueDescriptorImpl.setXPrecision(10);
        valueDescriptorImpl.setYPrecision(5);

        // Parameter to serialize
        ParameterImpl parameterImpl = new ParameterImpl();
        parameterImpl.setName("parameterName");

        parameterImpl.setBelongsToFunctionBeamProcess(true);
        parameterImpl.setDefaultHierarchy("defaultHierarchy");
        parameterImpl.setDevice(deviceImpl);
        parameterImpl.setReservedForOpExperts(true);
        parameterImpl.setMaxDelta(1245.6789);
        parameterImpl.setType(parameterTypeImpl);
        parameterImpl.setTrimable(true);
        parameterImpl.setValueDescriptor(valueDescriptorImpl);

        // Serialize
        HierarchyObjectMapper hierarchyObjectMapper = new HierarchyObjectMapper();
        SimpleModule hierarchyModule = new SimpleModule("TestHierarchyModule", Version.unknownVersion());
        hierarchyModule.addSerializer(ParameterImpl.class, new ParameterSerializer());
        hierarchyModule.addDeserializer(ParameterImpl.class, new ParameterDeserializer());
        String serializedParameter = hierarchyObjectMapper.writer().withDefaultPrettyPrinter()
                .writeValueAsString(parameterImpl);

        // Check serialization result
        Assert.assertEquals(LsaHierarchyImportSerializationDeserializationTest.SERIALIZED_PARAMETER,
                serializedParameter);
    }

    @Test
    public void testParameterRelationSerializer() throws JsonProcessingException {
        // One child
        ParameterImpl parameterChild = new ParameterImpl();
        parameterChild.setName("child");

        // With two parents
        ParameterImpl parameterParent1 = new ParameterImpl();
        parameterParent1.setName("parent1");
        ParameterImpl parameterParent2 = new ParameterImpl();
        parameterParent2.setName("parent2");

        // Create tree nodes
        ParameterTreeNodeImpl parameterTreeNodeChild = new ParameterTreeNodeImpl(parameterChild, false);
        ParameterTreeNodeImpl parameterTreeNodeParent1 = new ParameterTreeNodeImpl(parameterParent1, false);
        ParameterTreeNodeImpl parameterTreeNodeParent2 = new ParameterTreeNodeImpl(parameterParent2, false);

        // Connect tree nodes
        parameterTreeNodeParent1.addChild(parameterTreeNodeChild);
        parameterTreeNodeParent2.addChild(parameterTreeNodeChild);

        // Create wrapper that stores priority of relations
        ParameterTreeNodeWithPositions parameterTreeNodeWithPositionsChild = new ParameterTreeNodeWithPositions(
                parameterTreeNodeChild);
        parameterTreeNodeWithPositionsChild.putPosition(parameterTreeNodeParent1.getName(), 1);
        parameterTreeNodeWithPositionsChild.putPosition(parameterTreeNodeParent2.getName(), null);

        // Serialize
        HierarchyObjectMapper hierarchyObjectMapper = new HierarchyObjectMapper();
        SimpleModule hierarchyModule = new SimpleModule("TestHierarchyModule", Version.unknownVersion());
        hierarchyModule.addSerializer(ParameterTreeNodeWithPositions.class, new ParameterRelationSerializer());
        hierarchyModule.addDeserializer(ParameterTreeNodeWithPositions.class, new ParameterRelationDeserializer());
        String serializedParameterRelation = hierarchyObjectMapper.writer().withDefaultPrettyPrinter()
                .writeValueAsString(parameterTreeNodeWithPositionsChild);

        // Check serialization result
        Assert.assertEquals(LsaHierarchyImportSerializationDeserializationTest.SERIALIZED_PARAMETER_RELATION,
                serializedParameterRelation);
    }
}
