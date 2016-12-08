package de.gsi.cs.co.ap.lsa.setup.json;

import java.io.IOException;

import cern.lsa.domain.devices.Device;
import cern.lsa.domain.devices.spi.DeviceImpl;

import com.fasterxml.jackson.core.JsonGenerator;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.JsonSerializer;
import com.fasterxml.jackson.databind.SerializerProvider;

/**
 * Custom serialization for {@link Device}s to ensure that the format of the JSON file is stable.
 * 
 * @author hhuether
 * @see JsonSerializer
 */
public class DeviceSerializer extends JsonSerializer<DeviceImpl> {

    @Override
    public void serialize(DeviceImpl value, JsonGenerator jgen, SerializerProvider provider) throws IOException,
            JsonProcessingException {
        jgen.writeStartObject();
        jgen.writeStringField(JsonNodeNames.ACCELERATOR_ZONE, value.getAcceleratorZone().getName());
        jgen.writeStringField(JsonNodeNames.DESCRIPTION, value.getDescription());
        jgen.writeStringField(JsonNodeNames.DEVICE_ALIAS, value.getAlias());
        jgen.writeStringField(JsonNodeNames.DEVICE_TYPE, value.getDeviceType().getName());
        jgen.writeBooleanField(JsonNodeNames.IS_MULTIPLEXED, value.isMultiplexed());
        jgen.writeEndObject();
    }

}
