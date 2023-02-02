# Created by User at 1.02.2023
Feature: Board
  Checking the installation of elements from the queue to the board

  Background:
    Given The game is in progress


  @positive
  Scenario: User puts the house at empty cell
    Given Game board with default preset houses board/positive/default.yml
    Given User have in board queue [1,1,1,1]
    When User place on board/positive/user_place.yml
    Then A new board/positive/result_board.yml should  be generated by user as a result of the installation of the house at empty cell

  @positive
  Scenario: User puts the house at used cell
    Given Game board with default preset houses board/negative/default.yml
    Given User have in board queue [1,1,1,1]
    When User place on board/negative/user_place.yml
    Then Nothing will happen

  @positive
  Scenario: Checking the end of the game after the entire game board is full
    Given Fully filled board with houses of different levels
    Then Game is stopped