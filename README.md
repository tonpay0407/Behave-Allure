# Behave-Allure
 Behave is an agile software development technique to improve collab between QA, Devs and Business side people

Operates on directories containing feature files and step definition. Behave is a BDD (Behavior Driven Development) approach for python like Cucumber is for Java.

Feature File - For every feature of app we can create a feature file. Extension is .feature. While writing feature file we use Gherkin language which support certain keywords like Given, When , Then etc 

    Scenario - We will have multiple scenarios in a feature file.

        Steps -  Each scenario will have multiple steps

Examples are present in https://pypi.org/project/behave/

Working with Behave:

1. Install Python

2. Install an IDE

3. Install Selenium

4. Behave

Some useful commands -

python --version

pip list : Given the packages which are installed

pip install selenium 

pip install behave

After installing selenium and behave - gave a pip list

Once the installation is done, Open your IDE (Pycharm) and create a new project.

Go to project settings and in Project Interpreter install Selenium and Behave, which means now we can use features of selenium and behave in our project
 




New behave allure project
Behave : Python BDD framework

BDD 3 components:

1. Feature File: For every feature in application 1 file is created. extension" .feature
2. Scenarios : In every feature file, multiple scenarios will be present. Scenarios are written using gherkin keywords like : Given, When , Then.
	Scenario: title
		Given: A Precondition
		When: Some Event
		Then: Some Outcome
3. Step definition: For each scenario, multiple steps will be present.
4. Scenario outline is used when multiple parameters are to be passed. It is followed by Examples keyword
5. Background feature - When we want to execute a set of steps before each scenario in feature file.
6. To run behave feature file - behave ./Features/orangehrmlogin.feature
7. Command for allure report : behave -f allure_behave.formatter:AllureFormatter -o reports/ features/orangeHRM.feature
8. to render the report : allure serve reports/


Example:
Feature: OrangeHRM Login
Scenario: Logo presence on HRM homepage
	Given | launch chrome browser
	When |	open orange HRM homepage
	Then | verify that the logo is present on homepage

Scenario: Login to HRM homepage
	Given | launch chrome browser
	When |	open orange HRM homepage
	And | Enter user-name and password
	And | Click on login button
	Then| User must be able to login
	

Scenario Outline: Login to orange HRM with multiple parameters
    Given I launch chrome browser
    When I open orange HRM Homepage
    And Enter username "<username>" and password "<password>"
    And Click on login button
    Then User must successfully login to the Dashboard page

    Examples:
      | username  | password |
      | admin     | admin123 |
      | admin123  | admin |
      | adminxyz  | admin123 |
      | admin     | adminxyz |	
	  
	  
	  
	  
	  behave -f allure_behave.formatter:AllureFormatter -o %allure_result_folder% ./Features
