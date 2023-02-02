# Created by User at 1.02.2023
Feature: Combo-Merge
  Checking the installation of elements from the queue to the board

  Background:
    Given The game is in progress


  @positive
  Scenario: Combo-merge function
    Given Game board with default preset houses board/positive/first/default.yml
    Given User have in board queue [1,1,1,1]
    When User place on board/positive/first/user_place.yml
    Then From house lvl 1 should be generated a new board/positive/first/result_board.yml with combo-merge result lvl 3 house
    Then User gets a crystal


  @negative
  Scenario: Negative test to check the impossibility of combo-merging houses of different lvl
    Given Game board with default preset houses board/negative/first/default.yml
    Given User have in board queue [1,1,1,3]
    When User place on board/negative/first/user_place.yml
    Then From house lvl 3 should not be generated a new board/negative/first/result_board.yml with combo-merge result lvl 4 house
