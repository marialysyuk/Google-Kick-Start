This problem is taken from [here.](https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc8/00000000002d82e6)

## Problem

Li has planned a bike tour through the mountains of Switzerland. His tour consists of N checkpoints, numbered from 1 to N in the order he will visit them. The i-th checkpoint has a height of H<sub>i</sub>.

A checkpoint is a peak if:

- It is not the 1st checkpoint or the N-th checkpoint, and
- The height of the checkpoint is strictly greater than the checkpoint immediately before it and the checkpoint immediately after it.

Please help Li find out the number of peaks.

**Input**

The first line of the input gives the number of test cases, T. T test cases follow. Each test case begins with a line containing the integer N. The second line contains N integers. The i-th integer is Hi.

**Output**

For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the number of peaks in Li's bike tour.

**Limits**

Time limit: 10 seconds per test set.

Memory limit: 1GB.<br/>
1 ≤ T ≤ 100.<br/>
1 ≤ H<sub>i</sub> ≤ 100.



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
