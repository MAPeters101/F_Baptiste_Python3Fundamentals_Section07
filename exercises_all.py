"""
Question 1
Write some code that generates an m x n multiplication table.

For example if m=3 and n=4 your output should look something like:

1 x 1 = 1
1 x 2 = 2
1 x 3 = 3
1 x 4 = 4
---------------
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
2 x 4 = 8
---------------
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
3 x 4 = 12
---------------
Your code should be generic enough that it can handle any positive integer values of m and n.

Question 2
Your are given the following tuple of lists:

data = (
    ['2021-01-01', 10, 20],
    ['2021-01-02', 20, 18],
    ['2021-01-03', -10, 10],
    ['2021-01-04', 100, 102],
    ['2021-01-05', 20, 45]
)
Your program should:

Mutate the lists in data to add one more element indicating the distance between the two integer numbers (i.e. the absolute value fo the difference)
Determine on which date this newly calculate value was the largest.
Be able to work for a data set containing any number of lists.
Question 3
You are given a list of lists containing two numbers that will need to be color coded later based on a trend determined by the following rules:

If the first number of a row is higher than the second number of the previous row, append the string up to the row
If the first number of a row is lower than the second number of the previous row, append the string down to the row
Otherwise, append same to the row.
Obviously you cannot apply these rules to the first row (there is no preceding row), so append an empty string for the first row.

Basically think of this as a list of Open/Close values, and we want to assign the values same, up, or down based on how a row's Open value compares to the Close of the previous row.

For example, given the following list:

data = [
    [10, 20],
    [20, 30],
    [35, 50],
    [45, 60]
]
Then after your code finishes running, your data should look like this:

[
    [10, 20, ''],
    [20, 30, 'same'],
    [35, 50, 'up'],
    [45, 60, 'down']
]
"""