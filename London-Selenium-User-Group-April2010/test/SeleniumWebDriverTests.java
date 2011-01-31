import com.thoughtworks.selenium.*;
import org.junit.Test;
import org.openqa.selenium.*;
import org.openqa.selenium.firefox.*;

/**
 * Created by David Burns
 * Demo's for Selenium User Group London
 */
public class SeleniumWebDriverTests{

    @Test
    public void ShouldRunATestWithWebDriverButWithSeleniumMethods() throws InterruptedException {
        WebDriver driver = new FirefoxDriver();
        Selenium sel = new WebDriverBackedSelenium(driver,"http://localhost:8084/");
        sel.open("/");
        sel.type("editable","The Automated Tester");
        Thread.sleep(10000);
        sel.stop();
    }
}
