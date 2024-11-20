package th.ctf.alliespre.service.json;

import com.fasterxml.jackson.databind.DeserializationFeature;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.jsontype.BasicPolymorphicTypeValidator;
import com.fasterxml.jackson.databind.jsontype.PolymorphicTypeValidator;
import com.fasterxml.jackson.module.paramnames.ParameterNamesModule;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.Primary;

@Configuration
public class JSONConfiguration {

    /**
     * Override default JSON deserialization config available in Spring Boot with our own
     * @return custom JSON Parser
     */
    @Bean
    @Primary
    public ObjectMapper customJSONParser(){
        var objectMapper = new ObjectMapper();

        // Enable polymorphic deserialization, using a custom type validator for improved security
        objectMapper.activateDefaultTyping(getTypeValidator());

        // Do not fail if Java object does not have a JSON property
        objectMapper.disable(DeserializationFeature.FAIL_ON_UNKNOWN_PROPERTIES);

        // Transforms JSON Arrays to Java arrays, instead of Collection<?>
        objectMapper.enable(DeserializationFeature.USE_JAVA_ARRAY_FOR_JSON_ARRAY);

        // If a property has a type like: String[] data, accept JSON 'data: "hello"' as equivalent to 'data: ["hello"]'
        objectMapper.enable(DeserializationFeature.ACCEPT_SINGLE_VALUE_AS_ARRAY);

        // Deserialize json properties to Java parameter/field names
        // without needing explicit annotations for each property
        objectMapper.registerModule(new ParameterNamesModule());

        return objectMapper;
    }

    /**
     * Restrict which types can be deserialized for security reasons
     * @return Type validator, only allows deserialization of classes in package "rmartin.ctf.alliespre"
     */
    public PolymorphicTypeValidator getTypeValidator() {
        return BasicPolymorphicTypeValidator.builder()
                .allowIfSubType("rmartin.ctf.alliespre")
                .build();
    }
}
