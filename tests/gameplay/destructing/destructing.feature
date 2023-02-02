# Created by User at 30.01.2023
Feature: Destructing

  @positive
  Scenario: Using the destruction function at home
    Given The game is in progress
    Given Random numbers of houses on the game table
    Given One possibility to use the destruction function
    When User destroys a random house
    Then The house disappears from the game table
    Then From user takes one possibility to destruction

  @negative
  Scenario: Using the destruction function at empty cell
    Given The game is in progress
    Given Random numbers of houses on the game table
    Given One possibility to use the destruction function
    When User try to destroy an empty cell
    Then Nothing will happen
    Then From user wont take one possibility to destruction

  @positive
  Scenario: Getting the destroy function  after receiving 200 coins
    Given The game is in progress
    Given Random numbers of houses on the game table
    Given One possibility to use the destruction function
    Given 200 coins
    Then User gets one possibility to use the destruction function


  @positive
  Scenario: Canceling the destroy function after clicking on it
    Given The game is in progress
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
    Given The game is in progress
    Given Random numbers of houses on the game table
    Given One possibility to use the destruction function
    Given Spawn board with random lvl of houses
    When User try to destroy a house on spawn cell
    Then Nothing will happen
    Then From user wont take one possibility to destruction

  # destruction negative: no coins to use
