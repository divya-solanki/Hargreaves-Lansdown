Feature: Pension

Scenario: Drawdown Calculator
    Given Open the "https://www.hl.co.uk/" website in the Chrome browser.
    When Hover the mouse on "Pensions" menu
    Then Select "Drawdown calculator" under the "Drawdown" section
    Then "Enter the data in the fields below under the ""Your detail"" section.
    Then Enter Date of birth
    Then Enter Your existing pension fund
    Then Enter Required monthly income(before tax)
    Then Enter Tax free cash
    Then select the gender"
    Then Click on the "Calculate" button
    Then Verify "Your drawdown forecast" screen/page is displayed
    Then Verify the "Investement Growth" and "Average Fund Charge" fields values.
    Then Verify whether the graph is visible then, hover the mouse on the graph and capture the tooltip.


