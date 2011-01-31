using System;
using Selenium;

namespace ddd9demo
{
	
	public class SeleniumXPathTutorial
	{
	    private readonly ISelenium _selenium;
	
	    public const string FirstInput = "number1";
	    public const string SecondInput = "number2";
	    public const string Total = "total";
	
	    public SeleniumXPathTutorial(ISelenium selenium)
	    {
	        this._selenium = selenium;
	    }
	
	    public bool IsInputOnScreen(string locator)
	    {
	        return _selenium.IsElementPresent(locator);
	    }

	}
}

