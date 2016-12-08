package de.gsi.cs.co.ap.lsa.setup.json;

import cern.lsa.domain.devices.spi.DeviceImpl;
import cern.lsa.domain.optics.LogicalHardware;
import cern.lsa.domain.settings.spi.ParameterImpl;

import com.fasterxml.jackson.core.Version;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.module.SimpleModule;

import de.gsi.cs.co.ap.lsa.setup.data.ParameterTreeNodeWithPositions;

public class HierarchyObjectMapper extends ObjectMapper {

    private static final long serialVersionUID = 7300354352742812254L;

    public HierarchyObjectMapper() {
        super();

        SimpleModule hierarchyModule = new SimpleModule("HierarchyModule", Version.unknownVersion());

        // for devices
        hierarchyModule.addSerializer(DeviceImpl.class, new DeviceSerializer());
        hierarchyModule.addDeserializer(DeviceImpl.class, new DeviceDeserializer());

        // for parameters
        hierarchyModule.addSerializer(ParameterImpl.class, new ParameterSerializer());
        hierarchyModule.addDeserializer(ParameterImpl.class, new ParameterDeserializer());

        // for parameter relations
        hierarchyModule.addSerializer(ParameterTreeNodeWithPositions.class, new ParameterRelationSerializer());
        hierarchyModule.addDeserializer(ParameterTreeNodeWithPositions.class, new ParameterRelationDeserializer());

        // for link rule configurations
        hierarchyModule.addSerializer(LogicalHardware.class, new LogicalHardwareSerializer());
        hierarchyModule.addDeserializer(LogicalHardware.class, new LogicalHardwareDeserializer());
        
        this.registerModule(hierarchyModule);
    }
}
