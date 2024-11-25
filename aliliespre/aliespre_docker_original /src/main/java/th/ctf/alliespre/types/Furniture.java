package th.ctf.alliespre.types;

import com.fasterxml.jackson.annotation.JsonCreator;

public class Furniture extends AlliespreItem {

    @JsonCreator
    public Furniture(String name, String imageURL) {
        super(name, imageURL);
    }

    @Override
    public String getDescription() {
        return "Better than IQUEA";
    }
}
