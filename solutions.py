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

Solution
To do this we'll need to use a nested for loop to loop through each row, and then each column of the multiplication table:

m = 3
n = 4

for row in range(1, m + 1):
    for col in range(1, n+1):
        print(f'{row} x {col} = {row * col}')
    print('-' * 15)
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
And this code will work for other values of m and n as well:

m = 5
n = 5

for row in range(1, m + 1):
    for col in range(1, n+1):
        print(f'{row} x {col} = {row * col}')
    print('-' * 15)
1 x 1 = 1
1 x 2 = 2
1 x 3 = 3
1 x 4 = 4
1 x 5 = 5
---------------
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
2 x 4 = 8
2 x 5 = 10
---------------
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
3 x 4 = 12
3 x 5 = 15
---------------
4 x 1 = 4
4 x 2 = 8
4 x 3 = 12
4 x 4 = 16
4 x 5 = 20
---------------
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
---------------
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
Solution
First we'll need to add that calculated value to each list - we'll do that by appending an element to the lists as we loop through them:

for row in data:
    row.append(abs(row[1] - row[2]))
data
(['2021-01-01', 10, 20, 10],
 ['2021-01-02', 20, 18, 2],
 ['2021-01-03', -10, 10, 20],
 ['2021-01-04', 100, 102, 2],
 ['2021-01-05', 20, 45, 25])
Now that we have the new data, we simply need to loop through it and find the date for the row with the largest last number.

To do that we'll start by setting a starting maximum value (and corresponding date) based on the first row:

max_spread = data[0][-1]
max_date = data[0][0]

max_date, max_spread
('2021-01-01', 10)
Now we'll iterate through the remaining rows and see if we find something larger. We'll also use unpacking to unpack the values of each row into separate variables:

for dt, num_1, num_2, spread in data[1:]:
    if spread > max_spread:
        # found a new high
        max_spread = spread
        max_date = dt

max_date, max_spread
('2021-01-05', 25)
Note that we did not have to use unpacking, we could also have done it this way:

max_spread = data[0][-1]
max_date = data[0][0]

for row in data[1:]:
    if row[-1] > max_spread:
        # found a new high
        max_spread = row[-1]
        max_date = row[0]

max_date, max_spread
('2021-01-05', 25)
However, as you can see, the first approach is much easier for someone to read and understand what the code is doing.

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
Solution
We'll need to iterate through data and append a string to each row in data based on the stated rules.

We'll also need to reference the "previous" row. To do this we can use the enumerate() function - let's just loop through the data first and see how we could do this:

for idx, row in enumerate(data):
    if idx == 0:
        print(idx, 'no previous row')
    else:
        print(idx, row)
0 no previous row
1 [20, 30]
2 [35, 50]
3 [45, 60]
We can also use unpacking to unpack the two numbers in the rows:

for idx, (op, cl) in enumerate(data):
    if idx == 0:
        print(f'{idx}: no previous row')
    else:
        print(f'{idx}: open={op}, close={cl}')
0: no previous row
1: open=20, close=30
2: open=35, close=50
3: open=45, close=60
And we can also get the Open/Close values from the previous row (when there is one):

for idx, (op, cl) in enumerate(data):
    if idx == 0:
        print(f'{idx}: no previous row')
    else:
        print('-----')
        prev_op, prev_cl = data[idx-1]
        print(f'{idx}: open={op}, close={cl}')
        print(f'{idx-1}: open={prev_op}, close={prev_cl}')

0: no previous row
-----
1: open=20, close=30
0: open=10, close=20
-----
2: open=35, close=50
1: open=20, close=30
-----
3: open=45, close=60
2: open=35, close=50
Now we can finally apply our rules to assign that string to each row:

for idx, (op, cl) in enumerate(data):
    if idx == 0:
        data[idx].append('')
    else:
        # we have to watch out here, since we appended an extra element to the previous
        # row in the previous iteration, we now actually have 3 values to unpack!
        prev_op, prev_cl, trend = data[idx-1]
        if op > prev_cl:
            data[idx].append('up')
        elif op < prev_cl:
            data[idx].append('down')
        else:
            data[idx].append('same')

data
[[10, 20, ''], [20, 30, 'same'], [35, 50, 'up'], [45, 60, 'down']]
"""