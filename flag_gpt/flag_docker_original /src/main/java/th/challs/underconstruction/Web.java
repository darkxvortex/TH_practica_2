package th.challs.underconstruction;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;

@Controller
public class Web {
    public static final String STATIC_PATH = "/app/src/main/resources/static/";
    private static Logger logger = LoggerFactory.getLogger(Web.class);

    @GetMapping("/")
    @ResponseBody
    public byte[] index() throws IOException {
        // https://media.giphy.com/media/ANbD1CCdA3iI8/giphy.gif
        return Files.readAllBytes(Path.of(STATIC_PATH, "index.html"));
    }

    @GetMapping("/healthcheck")
    @ResponseBody
    public String healthcheck(){
        logger.info("Health ok");
        return "Health ok";
    }

    @GetMapping("/file")
    @ResponseBody
    public byte[] serveFile(@RequestParam String filename) throws IOException {
        logger.info("Serving file: {}", filename);
        return Files.readAllBytes(Path.of(STATIC_PATH, filename));
    }
}
