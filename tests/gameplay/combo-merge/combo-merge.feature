# Created by User at 1.02.2023
Feature: Combo-Merge
  Checking for merge of a multiple of houses

  @positive
  Scenario: Combo-merge function
    Given Game board with default preset houses tests/fixtures/boards/give/combo_merge_board/positive/default.yml
    Given User have in board queue [1,1,1,1]
    When User place on [1,1]
    Then From house lvl 1 should be generated a new tests/fixtures/boards/give/combo_merge_board/positive/result_board.yml with combo-merge result lvl 3 house
    Then User gets a crystal


  @negative
  Scenario: Negative test to check the impossibility of combo-merging houses of different lvl
    Given Game board with default preset houses tests/fixtures/boards/give/combo_merge_board/negative/default.yml
    Given User have in board queue [1,1,1,3]
    When User place on [1,1]
    Then From house lvl 3 should not be generated a new tests/fixtures/boards/give/combo_merge_board/negative/result_board.yml with combo-merge result lvl 4 house
