import org.junit.Test;
import org.openqa.selenium.*;
import org.openqa.selenium.firefox.*;
import com.thoughtworks.selenium.*;
import org.openqa.selenium.ie.InternetExplorerDriver;

/**
 * Created by David Burns
 * Demo's for Selenium User Group London
 */
public class FileInput {

    @Test
    public void selenium1FileInputWithFirefox() throws InterruptedException {
        Selenium sel = new DefaultSelenium("localhost",4444,"*firefox","http://localhost:8084");
        sel.start();
        Thread.sleep(1000);
        sel.windowMaximize();
        sel.open("/");
        sel.type("fileUpload","Penguins.jpg");
        Thread.sleep(10000);
        sel.stop();
    }

    @Test
    public void selenium2FileInputWithFirefox() throws InterruptedException{
        WebDriver driver = new FirefoxDriver();
        driver.get("http://localhost:8084/");
        Thread.sleep(2000);
        WebElement fileUpload = driver.findElement(By.id("fileUpload"));
        fileUpload.sendKeys("Penguins.jpg");
        Thread.sleep(10000);
        driver.quit();
    }
}
