using System;
using NUnit.Framework;
using Selenium;
using System.Threading;

namespace ddd9demo
{
	[TestFixture]
	public class SiteTests
	{
	    private ISelenium selenium;
	    [SetUp]
	    public void Setup()
	    {
	        selenium = new DefaultSelenium("localhost", 4444, "*firefox", "http://www.theautomatedtester.co.uk");
	        selenium.Start();
	    }
	
	    [TearDown]
	    public void Teardown()
	    {
	        selenium.Stop();
	    }
	
	    [Test]
	    public void ShouldLoadHomeThenGoToXpathTutorial()
	    {
	        Home home = new Home(selenium);
	        SeleniumTutorials seleniumTutorials = home.ClickSelenium();
	        SeleniumXPathTutorial seleniumXPathTutorial = seleniumTutorials.ClickXpathTutorial();
	        Assert.IsTrue(seleniumXPathTutorial.
						IsInputOnScreen(SeleniumXPathTutorial.FirstInput));
	        Assert.IsTrue(seleniumXPathTutorial
						.IsInputOnScreen(SeleniumXPathTutorial.SecondInput));
	        Assert.IsTrue(seleniumXPathTutorial
						.IsInputOnScreen(SeleniumXPathTutorial.Total));
			Thread.Sleep(10000);
	    }
	}
}