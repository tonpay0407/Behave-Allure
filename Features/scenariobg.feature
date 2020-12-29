Feature: OrangeHRM Login

  Background: Login to orange HRM with valid parameters
    Given I launch browser
    When I open application
    And Enter valid username and password
    And Click on login


  Scenario: Login to HRM App
    Then User must login

  Scenario: Search User
    When navigate to search page
    Then search page should display


  Scenario: Advanced Search User
    When navigate to advanced search page
    Then advanced search page should display