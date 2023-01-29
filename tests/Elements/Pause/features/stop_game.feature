# Created by User at 29.01.2023
Feature: Pause
  The user should be able to press pause and see such elements as:
  tooltip,
  amount of money,
  record for the amount of money

  Background:
    Given Game in progress

  Scenario: Pressing the pause button to stop game
    When The user press on the pause button
    Then The game stops and a menu will appear with this elements  <- [tooltip,amount_of_money,record_amount_of_money]