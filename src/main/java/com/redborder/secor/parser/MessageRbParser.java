package com.redborder.secor.parser;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.pinterest.secor.common.SecorConfig;
import com.pinterest.secor.message.Message;
import com.pinterest.secor.parser.JsonMessageParser;
import com.pinterest.secor.parser.MessageParser;
import org.apache.commons.lang.ArrayUtils;

import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;

public class MessageRbParser extends JsonMessageParser {
    ObjectMapper mapper = new ObjectMapper();

    public MessageRbParser(SecorConfig config) {
        super(config);
    }

    @Override
    public String[] extractPartitions(Message message) throws Exception {
        String[] toAppend = super.extractPartitions(message);
        Map<String, Object> messageJson = mapper.readValue(message.getPayload(), Map.class);
        String namespace = (String) messageJson.get("namespace_uuid");

        if(namespace == null){
            namespace = "default";
        }

        return (String[]) ArrayUtils.addAll(new String[]{namespace}, toAppend);
    }
}
