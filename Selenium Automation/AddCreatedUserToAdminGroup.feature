Feature: Add created user into the Administrator group
  Background: Admin is Logged in

    Scenario Outline: Admin is able to add created new user into the Administrator group
      Given Chrome Browser is launched
      And The url http://localhost:3000/ is opened
      When I enter email as "<adminUser>" and password as "<adminPass>"
      And I click on Sign in
      And I should logged in
      And I click on the settings icon
      And I click on Admin Settings
      And I click on People
      And I click on Invite Someone button
      And I enter first name as "<firstname>" and I enter last name as "<lastname>" and I enter email as "<email>"
      And I click on Create
      And I click on Done button
      And New user will be created
      And I click on Groups
      And I click on Administrator Group
      And I click on Add Member button
      And I enter the name of the created user as "<firstname>" "<lastname>"
      And I click on the Add button
      Then New created user will be added to the Administrator Group



      Examples:
      |adminUser|adminPass|firstname|lastname|email|
      |abdullah@123.com|abdullah@123|muhammad|hashim|hashim@123456.com|
      |abdullah@123.com|abdullah@123|hassan|rehman|hassan@123456.com|
      |abdullah@123.com|abdullah@123|junaid|ahmed|junaid@123456.com|
      |abdullah@123.com|abdullah@123|irtaza|zulfiqar|irtaza@123456.com|
