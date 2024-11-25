package th.ctf.alliespre.service.ping;

import org.springframework.stereotype.Service;

@Service
public class ServerStatus {
    public String doPing(String target){
        String args = "ping -c 4 " + target;
        var command = new Command(args);
        return command.doCommand();
    }

    public String usageStats(){
        String args = "free -h";
        var command = new Command(args);
        return command.doCommand();
    }
}
