
suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
for suit in suits:
    print(f'{suit[0].upper()} = {suit}')

for c in 'python':
    print(c)

print(c, suit)
print()

for i in range(2, 11, 2):
    print(i)

print(list(range(2,11,2)))
print('-'*80)

for i in range(3):
    for j in range(3):
        print(f'i={i}, j={j}')
    print('-'*10)
print('-'*80)

m = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

for row_idx in range(3):
    for col_idx in range(3):
        print(f'[{row_idx}, {col_idx}] = {m[row_idx][col_idx]}')
print('='*80)

print(len(m))
print(len(m[0]))
print(len(m[1]))
print(len(m[2]))
print('='*80)


for row_idx in range(len(m)):
    for col_idx in range(len(m[row_idx])):
        print(f'[{row_idx}, {col_idx}] = {m[row_idx][col_idx]}')
print('=' * 80)
print()

m = [
    [0,1],
    [2,3,4,5,6],
    [7,8,9],
    [10]
]

for row_idx in range(len(m)):
    for col_idx in range(len(m[row_idx])):
        print(f'[{row_idx}, {col_idx}] = {m[row_idx][col_idx]}')
print('+' * 80)
print()

n = 5
matrix = []
for row_idx in range(n):
    row = []
    for col_idx in range(n):
        if row_idx == col_idx:
            row.append(1)
        else:
            row.append(0)
    matrix.append(row)
print(matrix)

print('+' * 80)
print()

n = 10
matrix = []
for row_idx in range(n):
    row = []
    for col_idx in range(n):
        if row_idx == col_idx:
            row.append(1)
        else:
            row.append(0)
    matrix.append(row)
print(matrix)
print('-'*80)

data = [10, 20, 30]
print(enumerate(data))
print(list(enumerate(data)))
for t in enumerate(data):
    print(t)

for t in enumerate(data):
    idx, el = t
    print(idx, el)

for idx, el in enumerate(data):
    print(idx, el)
print()




