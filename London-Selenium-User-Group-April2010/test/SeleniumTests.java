import com.thoughtworks.selenium.*;
import org.junit.Test;

/**
 * Created by David Burns
 * Demo's for Selenium User Group London
 */
public class SeleniumTests {

    @Test
    public void ShouldRunANormalSeleniumTest() throws InterruptedException {
        Selenium sel = new DefaultSelenium("localhost",4444,"*firefox","http://localhost:8084");
        sel.start();
        sel.windowMaximize();
        sel.open("/");
        sel.type("editable","typing in a contentEditable area");
        Thread.sleep(10000);
        sel.stop();

    }
}
