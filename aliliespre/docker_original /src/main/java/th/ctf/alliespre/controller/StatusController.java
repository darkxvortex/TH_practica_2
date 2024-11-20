package th.ctf.alliespre.controller;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.servlet.ModelAndView;
import th.ctf.alliespre.service.ping.ServerStatus;

import javax.servlet.http.HttpServletRequest;

@Controller
public class StatusController {

    private static final Logger log = LoggerFactory.getLogger(StatusController.class);
    private final ServerStatus serverStatus;


    public StatusController(ServerStatus serverStatus) {
        this.serverStatus = serverStatus;
    }

    @GetMapping("/debug")
    public String showPing(){
        return "debug";
    }

    @PostMapping("/debug")
    public ModelAndView doPing(HttpServletRequest request, @RequestParam String target){
        String userIP = request.getRemoteAddr();
        log.info("User {} requested ping to {}", userIP, target);
        String pingResult = this.serverStatus.doPing(target);

        var mv = new ModelAndView();
        mv.setViewName("debug");
        mv.addObject("output", pingResult);
        return mv;
    }

    @PostMapping("/usage")
    public ModelAndView showUsage(HttpServletRequest request){
        String userIP = request.getRemoteAddr();
        log.info("User {} requested /usage", userIP);
        String usageResult = this.serverStatus.usageStats();

        var mv = new ModelAndView();
        mv.setViewName("debug");
        mv.addObject("output", usageResult);
        return mv;
    }
}
