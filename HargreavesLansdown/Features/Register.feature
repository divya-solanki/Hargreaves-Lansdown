Feature: HomePage

  Scenario: Register
    Given Open the "https://www.hl.co.uk/" website in the Chrome browser.
    When Click on the "Register" button
    Then Verify Register for online access screen/page is displayed
    Then Click on "No" button in the field "Do you know your client number"
    Then Enter Lastname
    And Date Of birth
    And Email Address
    And Then click on button "Continue".
