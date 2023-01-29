# Created by Ivan at 29.01.2023
Feature: Game Board
  The user at the beginning of the game must see the game board

  Scenario: Checking the generation of the game board with positive values
    Given Game board with positive generated values
    Then User must see the game board

  Scenario: Checking the generation of the game board with negative values
    Given Game board with negative generated values
    Then The game board should be recreated
    # TODO Then User must see the game board

  Scenario: Checking the generation of the game board with different number of houses from 0 to 36
    Given Game board with positive random preset of different number of houses from 0 to 36
    Then The game board must have a generated number of houses
    Then User must see the game board

