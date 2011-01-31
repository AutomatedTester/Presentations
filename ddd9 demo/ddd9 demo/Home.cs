using System;
using Selenium;

namespace ddd9demo
{
	public class Home
	{
		private readonly ISelenium _selenium;
    
	    /// <summary>
	    /// Instantiates a new Home Page object. Pass in the Selenium object created in the test SetUp(). 
	    /// When the object in instantiated it will navigate to the root
	    /// </summary>
	    /// Selenium Object created in the tests
	    public Home(ISelenium selenium)
	    {
	        this._selenium = selenium;
	        if (!selenium.GetTitle().Contains("home"))
	        {
	            selenium.Open("/");
	        }
			selenium.WindowMaximize();
	    }
	
	    /// <summary>
	    /// Navigates to Selenium Tutorials Page. Selenium object wll be passed through
	    /// </summary>
	    /// <returns>SeleniumTutorials representing the selenium_training.htm</returns>
	    public SeleniumTutorials ClickSelenium()
	    {
	        _selenium.Click("link=selenium");
	        _selenium.WaitForPageToLoad("30000");
	        return new SeleniumTutorials(_selenium);
	    }
	
	    /// <summary>
	    /// Click on the blog or blog year and then wait for the page to load
	    /// </summary>
	    /// blog or blog year
	    /// <returns>Object representing /blog.* pages</returns>
	    public Blog ClickBlogYear(string year)
	    {
	        _selenium.Click("link=" + year);
	        _selenium.WaitForPageToLoad("30000");
	        return new Blog(_selenium);
	    }
	    // Add more methods as you need them	
	}
}

