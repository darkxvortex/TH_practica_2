package th.ctf.alliespre.service.state;

import org.springframework.stereotype.Service;
import th.ctf.alliespre.types.AlliespreItem;
import th.ctf.alliespre.types.Furniture;
import th.ctf.alliespre.types.Smartphone;
import th.ctf.alliespre.types.TShirt;

import javax.servlet.http.HttpSession;
import java.util.List;
import java.util.Map;
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.CopyOnWriteArrayList;

/**
 * Stores information for each user currently attempting to solve the challenge.
 * Como una base de datos, pero cutre, para que aunque la gente esté en el mismo contenedor no vea los objetos que envían el resto.
 */
@Service
public class ItemStorage {
    private final Map<String, List<AlliespreItem>> userRequestsById = new ConcurrentHashMap<>();

    public Iterable<AlliespreItem> getItems(HttpSession session) {
        String id = session.getId();
        userRequestsById.computeIfAbsent(id, this::initialize);
        return userRequestsById.get(id);
    }

    public void setItems(HttpSession session, List<AlliespreItem> items) {
        String id = session.getId();
        userRequestsById.computeIfAbsent(id, this::initialize);
        userRequestsById.put(id, new CopyOnWriteArrayList<>(items));
    }

    public Iterable<AlliespreItem> addItem(HttpSession session, AlliespreItem item) {
        String id = session.getId();
        userRequestsById.computeIfAbsent(id, this::initialize);
        var userItems = userRequestsById.get(id);
        userItems.add(item);
        return userItems;
    }

    private List<AlliespreItem> initialize(String userId){
        var list = new CopyOnWriteArrayList<AlliespreItem>();
        list.add(new Furniture("Cutrus", "img/item/furniture1.png"));
        list.add(new TShirt("To the sky", "img/item/tshirt1.png"));
        list.add(new Smartphone("ifone 15", "img/item/smartphone1.png"));
        list.add(new Furniture("Builkus", "img/item/furniture2.png"));
        list.add(new TShirt("Wiiii", "img/item/tshirt2.png"));

        return list;
    }
}
