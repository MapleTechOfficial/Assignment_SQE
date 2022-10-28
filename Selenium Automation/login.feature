Feature: Run query
  Background: Login to the metabase
    Given I launch chrome browser
    When i go to the url http://localhost:3000/
    And enter email as "admin@metabase.com" and password "admin@123" and click on login


    Scenario Outline: Run Query
      When I click on New button
      And I click SQL Query
      And select "<database>"
      And write "<query>"
      Then Query result is displayed


      Examples:
        |database|query|
        |Sample Database|select * from temp|

