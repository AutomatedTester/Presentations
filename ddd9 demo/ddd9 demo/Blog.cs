using System;
using Selenium;

namespace ddd9demo
{
	public class Blog
	{
		private ISelenium _selenium;
		
		public Blog (ISelenium selenium)
		{
			_selenium = selenium;
		}
	}
}

