Feature: Funds

Scenario: Search Funds
    Given Open the "https://www.hl.co.uk/" website in the Chrome browser.
    When Click on Funds
    Then Select "UK Gilt" checkbox from the  Dropdown "sector".
    Then Select the checkbox "Income" from the Dropdown "Unit type"
    Then Select the checkbox "Tracker" from the Dropdown "Fund type"
    Then Select the Ongoing charge(OCF/TER)  and Yield fields from the ""More filters"" Dropdown
    Then Click on the "Show Results" button.
    Then Verify results are displayed
    Then  From the results displayed below, click on "VIEW FUND" button
    Then  Verify Fund page/screen is displayed

