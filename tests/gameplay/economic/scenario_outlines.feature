# content of scenario_outlines.feature

Feature: Scenario outlines

  Scenario Outline: Outlined given, when, then
    Given Random numbers of houses on the game table
    Given Gets <data> for combo-merging
    Then User gets <n> coins

    Examples:
      | data                                             | n  |
      | [{"count": 3, "lvl": 1}, {"count": 4, "lvl": 2}] | 22 |
      | [{"count": 4, "lvl": 3}, {"count": 4, "lvl": 3}] | 48 |
      | [{"count": 4, "lvl": 3}, {"count": 4, "lvl": 3}, {"count": 4, "lvl": 3}] | 96 |