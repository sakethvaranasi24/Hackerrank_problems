# 2D Array - DS

> Data Structures | Arrays | HackerRank

## Problem Overview

- Platform: HackerRank
- Domain: Data Structures
- Track: Arrays
- Difficulty: Easy
- Problem ID: 13581
- Max Score: 15
- Problem Link: [https://www.hackerrank.com/challenges/2d-array/problem](https://www.hackerrank.com/challenges/2d-array/problem)

## Problem

Given a $6 \times 6$ 2D array, $arr$, an hourglass is a subset of values with indices falling in the following pattern:

```
a b c  
  d  
e f g
```

There are $16$ hourglasses in a $6 \times 6$ array. The $hourglass\ sum$ is the sum of the values in an hourglass. Calculate the hourglass sum for every hourglass in $arr$, then print the $maximum$ hourglass sum.

**Example**  

$arr =$

    -9 -9 -9  1 1 1 
	 0 -9  0  4 3 2
	-9 -9 -9  1 2 3
	 0  0  8  6 6 0
	 0  0  0 -2 0 0
	 0  0  1  2 4 0

The $16$ hourglass sums are:

    -63, -34, -9, 12, 
	-10,   0, 28, 23, 
	-27, -11, -2, 10, 
	  9,  17, 25, 18
    
The highest hourglass sum is $28$ from the hourglass beginning at row $1$, column $2$:

    0 4 3
      1
    8 6 6
    
**Note:** If you have already solved the Java domain's *Java 2D Array* challenge, you may wish to skip this challenge.

**Function Description**

Complete the function $hourglassSum$ with the following parameter(s):

- $int\ arr[6][6]$: a 2-D array of integers  

**Returns**  

- $int$: the maximum hourglass sum

## Submission

| Item | Value |
| --- | --- |
| Status | Accepted |
| Language | python3 |
| Score | 15.0 |
| Testcases | 9/9 passed |
| Submission ID | 480748165 |

---

_Synced with AlgorithmHub_