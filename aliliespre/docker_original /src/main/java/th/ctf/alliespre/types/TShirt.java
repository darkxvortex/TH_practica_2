package th.ctf.alliespre.types;

import com.fasterxml.jackson.annotation.JsonCreator;

public class TShirt extends AlliespreItem {

    @JsonCreator
    public TShirt(String name, String imageURL) {
        super(name, imageURL);
    }

    @Override
    public String getDescription() {
        return "Like kuerty, but cheaper!";
    }
}
