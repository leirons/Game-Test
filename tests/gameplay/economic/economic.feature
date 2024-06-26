# Created by Ivan at 29.01.2023
Feature: Economic
  Checking the correct payment of coins

  Background:
    Given Random numbers of houses on the game table

  @positive
  Scenario: Getting n coins for placing a house
    When User puts the house of random lvl on cell
    Then User gets n coins

  @positive
  Scenario: Getting n*20 coins for destroying a house
    When User destroys a random house
    Then User gets n*20 coins

  @positive
  Scenario: Getting n+1 coins for using crystal
    Given Crystal
    When User use crystal on a house
    Then User gets n+1 coins

  @positive
  Scenario: Getting n*x coins for merging x houses of n lvl
    When User merges x houses of n lvl
    Then User gets n*x coins
