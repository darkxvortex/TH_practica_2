package th.ctf.alliespre.types;

import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonProperty;

public class Smartphone extends AlliespreItem {

    @JsonCreator
    public Smartphone(@JsonProperty String name, @JsonProperty String imageURL) {
        super(name, imageURL);
    }

    @Override
    public String getDescription() {
        return "unlimited screen repairs! (scratches not included)";
    }
}
