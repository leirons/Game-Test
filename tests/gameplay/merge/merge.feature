# Created by Ivan at 29.01.2023
Feature: Merge
  Combining n-level houses with n-1 level houses


  @positive
  Scenario: Simple merge
    Given Game board with default preset houses boards/give/merge_board/positive/default.yml
    Then User have in board queue [1,1,1,1]
    When User place on [3,0]
    Then A new boards/give/merge_board/positive/result_board.yml will be generated by user with the result of the merging

  @negative
  Scenario: Negative test to check the impossibility of merging houses in different parts of the game board
    Given Game board with default preset houses boards/give/merge_board/negative/first/default.yml
    Then User have in board queue [1,1,1,1]
    When User place on [4,0]
    Then A new boards/then/merge_board/negative/first/result_board.yml should not be generated by user as the result of the merging


  @negative
  Scenario: Negative test to check the impossibility of merging houses of different lvl
    Given Game board with default preset houses boards/give/merge_board/negative/second/default.yml
    Then User have in board queue [1,1,1,3]
    When User place on [3,0]
    Then A new boards/then/merge_board/negative/second/result_board.yml should not be generated by user as the result of the merging
