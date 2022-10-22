Feature: Connect to mySQL Database
Background: Admin is able to connect to a mySQL Database

Scenario: Admin is able to connect to an existing mySQL Database
    Given I launch the chrome browser
    And go to the url http://localhost:3000/
    And enter email as "admin@metabase.com" and password "admin@99" and click on login
