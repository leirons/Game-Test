# Created by User at 31.01.2023
Feature: Combo Merge Reward
  Testing getting reward after combo merge

  Background:
    Given The game is in progress
    Given A crystal after combo-merge case


  @positive
  Scenario: Increase house level by +1 with crystal
    Given Board with houses up to level 9
    When User drags the crystal to any house up to level 9
    Then User gets house with current level +1

  @positive
  Scenario: Checking house returns to initial position at spawn place after using crystal
    Given Board with houses up to level 9
    Given Spawn queue [8,7,8,crystal] with 8 in cache
    When User drags the crystal to any house up to level 9
    Then User gets house with lvl 8 from cache

  @negative
  Scenario: Try to use crystal at empty cell
    Given Board with empty cell
    When User drags the crystal to any empy cell
    Then Nothing will happen

  @negative
  Scenario: Try to use crystal at lvl 10 house
    Given Board with level 10 house
    When User drags the crystal to any house level 10
    Then Nothing will happen

  @negative
  Scenario: Try to use crystal at spawn place
    When User drags the crystal to any house at spawn place
    Then Nothing will happen
