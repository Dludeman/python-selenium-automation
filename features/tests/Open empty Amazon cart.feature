# Created by Daniel at 7/20/22
Feature: Verify logged-out user opening cart will see empty cart
  # Enter feature description here

  Scenario: Logged-out user sees empty cart
    Given Open Amazon page
    When Click on cart icon
    Then Verify cart is empty