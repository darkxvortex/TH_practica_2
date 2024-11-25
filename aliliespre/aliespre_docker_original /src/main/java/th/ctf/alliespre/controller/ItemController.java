package th.ctf.alliespre.controller;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.servlet.ModelAndView;
import th.ctf.alliespre.service.state.ItemStorage;
import th.ctf.alliespre.types.AlliespreItem;

import javax.servlet.http.HttpServletRequest;

@Controller
public class ItemController {

    private static final Logger log = LoggerFactory.getLogger(ItemController.class);
    private final ItemStorage itemStorage;

    public ItemController(ItemStorage itemStorage) {
        this.itemStorage = itemStorage;
    }

    @GetMapping("/items")
    public ModelAndView getItems(HttpServletRequest request){
        String ip = request.getRemoteAddr();
        log.info("User {} called ItemController::getItems()", ip);

        var mv = new ModelAndView();
        mv.setViewName("items");
        var items = itemStorage.getItems(request.getSession());
        mv.addObject("items", items);
        return mv;
    }

    @PostMapping("/items")
    public ResponseEntity<?> requestItem(@RequestBody AlliespreItem item, HttpServletRequest request){
        String ip = request.getRemoteAddr();
        log.info("User {} called ItemController::requestItem()", ip);

        itemStorage.addItem(request.getSession(), item);
        return ResponseEntity.ok().build();
    }
}
