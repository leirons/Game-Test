# Created by Ivan at 29.01.2023
Feature: Economic
  Checking the correct payment of coins

  Background:
    Given The game is in progress


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

  @positive
  Scenario: Getting ( (x1*n1) + (x2*n2)+ ... +(хN*nN) ) * N coins for combo-merge
    When User merges multiple x houses of multiple n lvl
    Then User gets ( (x1*n1) + (x2*n2)+ ... +(хN*nN) ) * N coins
