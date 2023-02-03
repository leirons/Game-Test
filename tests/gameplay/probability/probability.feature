# Created by User at 31.01.2023
# content of probability.feature
Feature: Probability


  Background:
    Given A tests/fixtures/probabilities/chances/give/default.yml with probability chances

  Scenario Outline: Outlined given, when, then
    Given Game board with max house <lvl>
    When User place a house on game board
    Then The user gets a house on the spawn board with a certain probability chance

    Examples:
      | lvl |
      | 1   |
      | 2   |
      | 3   |
      | 4   |
      | 5   |
      | 6   |
      | 7   |
      | 8   |
      | 9   |
      | 10  |


