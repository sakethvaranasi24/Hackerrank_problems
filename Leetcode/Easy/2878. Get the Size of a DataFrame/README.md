# Get the Size of a DataFrame

> Easy | 2878 | LeetCode

## Problem Overview

- Platform: LeetCode
- Difficulty: Easy
- Problem ID: 2878
- Tags: N/A
- Problem Link: [https://leetcode.com/problems/get-the-size-of-a-dataframe/](https://leetcode.com/problems/get-the-size-of-a-dataframe/)

## Problem

<pre>
DataFrame <code>players:</code>
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| player_id   | int    |
| name        | object |
| age         | int    |
| position    | object |
| ...         | ...    |
+-------------+--------+
</pre>

<p>Write a solution to calculate and display the <strong>number of rows and columns</strong> of <code>players</code>.</p>

<p>Return the result as an array:</p>

<p><code>[number of rows, number of columns]</code></p>

<p>The result format is in the following example.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:
</strong>+-----------+----------+-----+-------------+--------------------+
| player_id | name     | age | position    | team               |
+-----------+----------+-----+-------------+--------------------+
| 846       | Mason    | 21  | Forward     | RealMadrid         |
| 749       | Riley    | 30  | Winger      | Barcelona          |
| 155       | Bob      | 28  | Striker     | ManchesterUnited   |
| 583       | Isabella | 32  | Goalkeeper  | Liverpool          |
| 388       | Zachary  | 24  | Midfielder  | BayernMunich       |
| 883       | Ava      | 23  | Defender    | Chelsea            |
| 355       | Violet   | 18  | Striker     | Juventus           |
| 247       | Thomas   | 27  | Striker     | ParisSaint-Germain |
| 761       | Jack     | 33  | Midfielder  | ManchesterCity     |
| 642       | Charlie  | 36  | Center-back | Arsenal            |
+-----------+----------+-----+-------------+--------------------+<strong>
Output:
</strong>[10, 5]
<strong>Explanation:</strong>
This DataFrame contains 10 rows and 5 columns.
</pre>


## Submission

| Item | Value |
| --- | --- |
| Status | Accepted |
| Language | Pandas |
| Runtime | 282 ms (51.75%) |
| Memory | 66.6 MB (21.73%) |
| Submission ID | 2108625814 |

---

_Synced with AlgorithmHub_