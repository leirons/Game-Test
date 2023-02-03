# content of combo_merge_outline_economic.feature

Feature: Combo Merge Outline

  Scenario Outline: Getting ( (x1*n1) + (x2*n2)+ ... +(хN*nN) ) * N coins for combo-merge
    Given Random numbers of houses on the game table
    Given Gets <data> for combo-merging
    Then User gets <n> coins

    Examples:
      | data                                             | n  |
      | [{"count": 3, "lvl": 1}, {"count": 4, "lvl": 2}] | 22 |
      | [{"count": 4, "lvl": 3}, {"count": 4, "lvl": 3}] | 48 |
      | [{"count": 4, "lvl": 3}, {"count": 4, "lvl": 3}, {"count": 4, "lvl": 3}] | 96 |