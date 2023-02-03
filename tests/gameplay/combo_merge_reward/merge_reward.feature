# Created by User at 31.01.2023
Feature: Combo Merge Reward
  Testing getting reward after combo merge



  @positive
  Scenario: Increase house level by +1 with crystal
    Given A crystal after combo-merge case
    Given Board with houses up to level 9
    When User drags the crystal to any house up to level 9
    Then User gets house with current level +1

  @positive
  Scenario: Checking house returns to initial position at spawn place after using crystal
    Given A crystal after combo-merge case
    Given Board with houses up to level 9
    Given Spawn queue [8,7,8,crystal] with 8 in cache
    When User drags the crystal to any house up to level 9
    Then User gets house with lvl 8 from cache

  @negative
  Scenario: Try to use crystal at empty cell
    Given A crystal after combo-merge case
    Given Board with empty cell
    When User drags the crystal to any empy cell
    Then Nothing will happen

  @negative
  Scenario: Try to use crystal at lvl 10 house
    Given A crystal after combo-merge case
    Given Board with level 10 house
    When User drags the crystal to any house level 10
    Then Nothing will happen

  @negative
  Scenario: Try to use crystal at spawn place
    Given A crystal after combo-merge case
    When User drags the crystal to any house at spawn place
    Then Nothing will happen


  @negative
  Scenario: The user is trying to place the crystal that does not exists in queue
    Given Given Random numbers of houses on the game table
    Given Сrystal in the state of selecting an object to use
    Given A spawn queue without crystal
    When User try to use the crystal on random house
    Then Nothing will happen
