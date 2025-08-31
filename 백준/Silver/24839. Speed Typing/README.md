# [Silver IV] Speed Typing - 24839 

[문제 링크](https://www.acmicpc.net/problem/24839) 

### 성능 요약

메모리: 32412 KB, 시간: 1760 ms

### 분류

구현, 그리디 알고리즘, 문자열

### 제출 일자

2025년 8월 31일 09:26:28

### 문제 설명

<p>Barbara is a speed typer. In order to check her typing speed, she performs a speed test. She is given a string $I$ that she is supposed to type.</p>

<p>While Barbara is typing, she may make some mistakes, such as pressing the wrong key. As her typing speed is important to her, she does not want to spend additional time correcting the mistakes, so she continues to type with the errors until she finishes the speed test. After she finishes the speed test, she produces a $P$.</p>

<p>Now she wonders how many extra letters she needs to delete in order to get $I$ from $P$. It is possible that Barbara made a mistake and $P$ cannot be converted back to $I$ just by deleting some letters. In particular, it is possible that Barbara missed some letters.</p>

<p>Help Barbara find out how many extra letters she needs to remove in order to obtain $I$ or if $I$ cannot be obtained from $P$ by removing letters then output <code>IMPOSSIBLE</code>.</p>

### 입력 

 <p>The first line of the input gives the number of test cases, $T$. $T$ test cases follow.</p>

<p>Each test case has $2$ lines. The first line of each test case is an input string $I$ (that denotes the string that the typing test has provided). The next line is the produced string $P$ (that Barbara has entered).</p>

### 출력 

 <p>For each test case, output one line containing <code>Case #x: y</code>, where $x$ is the test case number (starting from $1$) and $y$ is the number of extra letters that need to be removed in order to obtain $I$. If it is not possible to obtain $I$ then output <code>IMPOSSIBLE</code> as $y$.</p>

