This problem is taken from [here.](https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc8/00000000002d83bf)

## Problem

Bucket is planning to make a very long journey across the countryside by bus. Her journey consists of N bus routes, numbered from 1 to N in
the order she must take them. The buses themselves are very fast, but do not run often. The i-th bus route only runs every X\_i days.

More specifically, she can only take the i-th bus on day X\_i, 2X\_i, 3X\_i and so on. Since the buses are very fast, she can take multiple buses on the same day.

Bucket must finish her journey by day D, but she would like to start the journey as late as possible. What is the latest day she could take the first bus, and still finish her journey by day D?

It is guaranteed that it is possible for Bucket to finish her journey by day D.

**Input**

The first line of the input gives the number of test cases, T. T test cases follow. Each test case begins with a line containing the integer N. The second line contains N integers. The i-th integer is Hi.

**Output**

For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the number of peaks in Li's bike tour.

**Limits**

Time limit: 10 seconds per test set.

Memory limit: 1GB.<br/>
1 ≤ T ≤ 100.<br/>
1 ≤ Hi ≤ 100.



Test Set 1<br/>
3 ≤ N ≤ 5.

Test Set 2<br/>
3 ≤ N ≤ 100.

**Sample**

*Input*
 
4<br/>
3<br/>
10 20 14<br/>
4<br/>
7 7 7 7<br/>
5<br/>
10 90 20 90 10<br/>
3<br/>
10 3 10<br/>

*Output*

Case #1: 1 <br/>
Case #2: 0 <br/>
Case #3: 2<br/>
Case #4: 0 <br/>
  
- In sample case #1, the 2nd checkpoint is a peak.
- In sample case #2, there are no peaks.
- In sample case #3, the 2nd and 4th checkpoint are peaks.
- In sample case #4, there are no peaks.
