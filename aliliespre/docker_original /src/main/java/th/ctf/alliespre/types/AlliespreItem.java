package th.ctf.alliespre.types;

import com.fasterxml.jackson.annotation.JsonTypeInfo;

import java.util.concurrent.atomic.AtomicInteger;

@JsonTypeInfo(use = JsonTypeInfo.Id.CLASS)
public abstract class AlliespreItem {
    private static AtomicInteger lastId = new AtomicInteger(1);

    private final String name;
    private final String imageURL;
    private final int id;

    public AlliespreItem(String name, String imageURL) {
        this.name = name;
        this.imageURL = imageURL;
        this.id = lastId.getAndIncrement();
    }

    public String getName() {
        return name;
    }

    public int getId() {
        return id;
    }

    public String getImageURL() {
        return imageURL;
    }

    public abstract String getDescription();
}
