# Created by User at 29.01.2023
Feature: Pause
  The user should be able to continue game after pause

  Background:
    Given Game in progress

  Scenario: Pressing the continue game button to continue the game
    When The user press on continue button
    Then The game will continue