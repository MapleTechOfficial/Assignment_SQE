Feature: metabase login
  Scenario:Login to the metabase
    Given I launch chrome browser
    When i go to the url http://localhost:3000/
    And enter email as "hassan210302@gmail.com" and password "hassan210302" and click on login
    Then metabase home page opens