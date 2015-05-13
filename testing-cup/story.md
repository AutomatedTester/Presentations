# Selenium Carol

Hello all, I hope everyone has a good lunch and that you are ready for my talk.

My name is David Burns for those who don’t know me and I work on  test automation tools. I have been working on Selenium browser automation framework for around 6 years. I believe in the web so want to be able to help people make high quality sites because high quality sites mean that people will return to it!

So today I am going to be walking through how things have changed and how things will continue to change.

## Past

So I am going to start by talking about the ancient times! About 15 or so years ago. I technology terms that is really old! Back then the internet was a fledgling concept. There weren’t many people who used the internet on a daily basis and there were 2  browsers of note but really there was only one. And that one was Internet Explorer. They had 99% of the market and essentially stopped development of IE. Netscape was on it’s last legs and looking for a new owner (AOL jumped at this opportunity). According to Microsoft, the war was over. 

The one good thing, at least from the stance of a quality engineer is that if something needed to be released you only needed to make sure that it worked in one browser. Imagine how much simpler our lives were back then. A developer would create a feature and they could test it locally and when you got it, you didn’t have to do permuations of platforms and browsers. You had 100 test cases you only needed to do those 100 tests.

And then what happened was a phoenix was rising out of the ashes  of netscape. A group, led by Mitchell Baker, managed to get Netscape to release it’s code and from there they went on to build Firefox the browser. Firefox was going to compete against Microsoft, who at this point didn’t care about the web anymore. With 99% of the market, why should they?

This reignited the browser wars, well it was more of a feud at this point. Firefox wanted people to have a choice. Choice is a good thing because you use what you want. The bad part comes if you are a web developer or if you are a quality engineer. Now we need to make sure that our web application works in 2 browsers. Oh and since microsoft had ignored standards bodies and Mozilla were following standards bodies making sure that applications worked was a lot of work.

QA would receive a build and now instead of having to do 100 tests they now had to do 200 tests. 2 browsers multiplied by the amount of tests. So when QA got something to test it was a lot like this, because as we know the amount of time to do QA wouldn’t have doubled. You were expected to do twice the tests in the same amount of time… and there was no continuous integration or test automation… It was really infuriating.

And when you found one bug it normally meant that you found a whole swathe of different bugs just lurking around. And they do like to bite.

Well, this was until Selenium was created. People could now write some form of tests that could be run over and over and you could see what is wrong. It was the future! All of this awesomeness to test an application.

People thought they had their own person robot for testing their applications and that it would be super human. Bugs? That’s a thing of the past. Where we are going it will be amazing… and bug free.

So let’s see a **demo** of this!

Here I am going to show you how Selenium RC works by starting Firefox and then we visit a page and click a button

One thing you’ll notice is that it looks like I want to start Chrome. Actually… Firefox had described the visible parts of firefox that are no in the web page Chrome and it has special privileges, but I digress.

But as time went on it became very rusty and it wasn’t keeping up with the web.

## The Present

During the growth of Selenum there was another project that was being created. This project was called WebDriver and it was doing things in a different way but it didn’t have the community . Selenium was becoming rusty and web driver wasn’t complete so the creators of both these projects decided to have a “Steel Cage Knife Fight”. The fought it out, figuratively, and then we the projects started the mammoth task of merging these two code bases.

WebDriver, from an API point of view was completely different and had quite a few nice things that we can use

