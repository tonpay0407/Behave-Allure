Feature: OrangeHRM Logo
  Scenario: Logo presence on HRM homepage
    Given launch chrome browser
	When open orange HRM homepage
	Then verify that the logo is present on homepage
	And close browser
