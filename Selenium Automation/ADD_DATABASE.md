# Feature: Connect to mySQL Database
## Background: Admin is able to connect to a mySQL Database

## Scenario Outline: Admin is able to connect to an existing mySQL Database
    Given I launch the chrome browser
    And go to the url http://localhost:3000/
    And enter email as "<adminUser>" and password "<adminPass>" and click on login
    And I click on the settings icon
    And I click on Admin Settings
    And I click on Databases
    And I click on Add Database
    And I select MySQL Database
    And I enter Display Name as "<dispName>" and I enter Host as "<host>" and I enter Port as "<port>" and I enter Database Name as "<dbname>" and I enter Username as "<dbuser>" and I enter Password as "<dbpass>"
    When I click Save
    Then I get the database "<dispName>" created`

    Examples:
        | adminUser | adminPass | dispName | host | port | dbname | dbuser | dbpass |
        #Valid Case
        | admin@metabase.com | admin@99 | mapletech | qvti2nukhfiig51b.cbetxkdyhwsb.us-east-1.rds.amazonaws.com | 3306 | j0uf2qniu2pa8oo4 | g87uxt2ng0i5bnlg | jqszjdxvgdcotq9a |
        #InValid Account Case
        | invalid@metabase.com | random | dispName | host | port | dbname | dbuser | dbpass |
        #Invalid Database Case
        | admin@metabase.com | admin@99 | mapletech | 192.168.10.1 | 3306 | samplename | sampleuser | rand |`

## How to Configure?
- Open project through pyCharm
- Download jar file of [metabase](https://www.metabase.com/start/oss/jar) and run the following command in terminal: `$   java -jar metabase.jar`
- Run the following command in pyCharm terminal: `behave connectDB.feature`

