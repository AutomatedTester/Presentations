using System;
using Selenium;

namespace ddd9demo
{
	public class SeleniumTutorials
	{
		private ISelenium _selenium;
		const string xpathLink = "link=XPath Tutorial";
		
		public SeleniumTutorials (ISelenium selenium)
		{
			_selenium = selenium;
		}
		
		public SeleniumXPathTutorial ClickXpathTutorial()
		{
			_selenium.Click(xpathLink);
			_selenium.WaitForPageToLoad("30000");
			return new SeleniumXPathTutorial(_selenium);
		}
		
	}
}

