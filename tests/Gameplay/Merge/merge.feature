# Created by Ivan at 29.01.2023
Feature: Merge
  Combining n-level houses with n-1 level houses

  Scenario Outline: Simple Merge
    Given Game board with default preset houses <- "<initial_board>"
    Then User have in board queue "<user_queue>"
    When User place on "<initial_board>"
    Then A new "<result_board>" will be generated by user with the result of the merging 3 house lvl 1 into 1 house lvl 2
    Examples:
     | initial_board | result_board |user_queue|
     | [0,0,0,0,0,0],[0,0,0,0,0,0],[1,1,0,0,0,0],[1,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0] |  [0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[2,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0] | [1,1,1,1] |

  Scenario: Simple merge
    Given Game board with default preset houses <- "[0,0,0,0,0,0],[0,0,0,0,0,0],[1,1,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]"
    Then User have in board queue "[1,1,1,1]"
    When User place on "[0,0,0,0,0,0],[0,0,0,0,0,0],[1,1,0,0,0,0],[1,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]"
    Then A new "[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[2,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]" will be generated by user with the result of the merging 3 house lvl 1 into 1 house lvl 2


#
#      When User place on board "[0,0,0,0,0,0],[0,0,0,0,0,0],[1,1,0,0,0,0],[1,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]
#    Then  User should see point increase 6