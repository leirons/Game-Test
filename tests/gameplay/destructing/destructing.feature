# Created by User at 30.01.2023
Feature: Destructing
  Checking the interaction of the destruction function with the board

  @positive
  Scenario: Using the destruction function at home
    Given Random numbers of houses on the game table
    Given One possibility to use the destruction function
    When User destroys a random house
    Then The house disappears from the game table
    Then From user takes one possibility to destruction

  @negative
  Scenario: Using the destruction function at empty cell
    Given Random numbers of houses on the game table
    Given One possibility to use the destruction function
    When User try to destroy an empty cell
    Then Nothing will happen
    Then From user wont take one possibility to destruction

  @positive
  Scenario: Getting the destroy function  after receiving coins
    Given Random numbers of houses on the game table
    Given One possibility to use the destruction function
    Given User gets 200 coins
    Then User gets possibility to use the destruction function


  @positive
  Scenario: Canceling the destroy function after clicking on it
    Given Random numbers of houses on the game table
    Given One possibility to use the destruction function
    When User clicks on destroy button
    Then There will be an option to cancel the destruction
    When User presses on the button to stop the destruction
    Then The state of choosing a house to destroy disappears

  @positive
  Scenario: Getting the destroy function after starting a game
    When User starts a game
    Then User gets one destroy function

  @negative
  Scenario: Using the destruction function at spawn place
    Given Random numbers of houses on the game table
    Given One possibility to use the destruction function
    Given Spawn board with random lvl of houses
    When User try to destroy a house on spawn cell
    Then Nothing will happen
    Then From user wont take one possibility to destruction

  @positive
  Scenario: Trying to destroy a house with 0 coins and no destruction function
    Given Random numbers of houses on the game table
    When User tries to destroy a random house
    Then Nothing will happen
