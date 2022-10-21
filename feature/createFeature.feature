Feature: Create a new Feature
Background: User is able to create a new feature in the application

Scenario Outline: User is unable to create a new feature in the application if it already exists
    Given I launch the chrome browser
    And go to the url http://localhost:8085/
    And enter email as "admin@featurehub.com" and password "admin123"
    And click on Features
    And I enter feature name as <name>
    And I enter feature key as <key>
    And I enter feature description as <desc>
    And I enter feature Reference Link as <link>
    And I select feature type as <type>
    When I click Create Feature Button
    Then the feature is <isCreated>
    And the message saying <message> is displayed

    Examples:
        | name | key  | desc | link | type   | isCreated | message                 |
        | abcd | efgh | xyza | defg | String | Created   | Feature 'abcd' created! |