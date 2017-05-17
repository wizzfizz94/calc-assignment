var webdriver = require('selenium-webdriver');
var browser = new webdriver.Builder().usingServer()
	.withCapabilities({'browserName': 'chrome' }).build();
 
browser.get('http://localhost:8080/calculator.html');
browser.findElements(webdriver.By.css('[href^="/wiki/"]'))
.then(function(links){
    console.log('Found', links.length, 'Wiki links.' )
    browser.quit();
});