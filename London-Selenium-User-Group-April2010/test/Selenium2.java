import org.junit.Test;
import org.openqa.selenium.*;
import org.openqa.selenium.firefox.*;

/**
 * Created by David Burns
 * Demo's for Selenium User Group London
 */
public class Selenium2 {

    @Test
    public void shouldLoadBrowserAndDoASeachWithGoogle() throws InterruptedException {
        WebDriver driver = new FirefoxDriver();
        driver.get("http://www.google.co.uk");

        //Find the Query and type into it
        WebElement query = driver.findElement(By.name("q"));
        query.sendKeys("The Automated Tester");

        //Find the search button and click it
        WebElement searchButton = driver.findElement(By.name("btnG"));
        searchButton.click();
        Thread.sleep(1000);
        driver.close();
    }

    @Test
    public void shouldLoadLocalAndTypeInContentEditable() throws InterruptedException {
        WebDriver driver = new FirefoxDriver();

        // Load the Site
        driver.get("http://localhost:8084/");

        //Find the contentEditable area and then type in it
        WebElement editable = driver.findElement(By.id("editable"));
        editable.sendKeys("I can type in contentEditable areas");
        Thread.sleep(10000);

        //Clean up the driver
        driver.quit();
    }
}
