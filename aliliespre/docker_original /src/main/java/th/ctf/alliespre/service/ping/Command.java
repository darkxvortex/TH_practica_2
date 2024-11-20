package th.ctf.alliespre.service.ping;

import java.util.Scanner;

public class Command {

    private String command;

    protected Command() {
    }

    public Command(String command) {
        this.command = command;
    }

    public String doCommand() {
        try {
            var process = Runtime.getRuntime().exec(new String[]{"/bin/bash", "-c", command});
            return getCommandOutput(process);
        } catch (Exception e) {
            return "Error: " + e.getMessage();
        }
    }


    protected String getCommandOutput(Process process) {
        var normal = new Scanner(process.getInputStream()).useDelimiter("\\A");
        var error = new Scanner(process.getErrorStream()).useDelimiter("\\A");

        String result = normal.hasNext() ? normal.next() : "";
        result += "\n";

        result += error.hasNext() ? error.next() : "";
        result += "\n";

        return result;
    }

    public void setCommand(String command) {
        this.command = command;
    }
}
