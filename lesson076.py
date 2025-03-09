for i in range(100):
    print(i)
    if i >= 5:
        print('breaking out of loop')
        break
print('done')
print()

for i in range(1, 11):
    if i % 2 == 1:
        continue
    print(i)
print()

for i in range(1,11):
    if i%2 == 0:
        print(i)
print('-'*80)
print()

for i in range(1, 5):
    for j in range(1, 5):
        if (i + j) %2 == 1:
            print(f'{i} + {j} is odd, skipping...')
            continue
        print(f'adding numbers: {i} + {j} = {i + j}')
    print('-'*10)
print()


for i in range(1, 4):
    for j in range(1, 4):
        if j >= 3:
            break
        print(i, j)
    print('-'*10)
print()


i = 0
while True:
    i += 1
    if i > 5:
        break
    print(i)
print('-'*80)


data = [1,2,3,-4,5,6]
all_positive = True
for element in data:
    if element <= 0:
        all_positive = False
        break

if all_positive:
    print('Processing all positive elements')
print('--')

data = [1,2,3,4,5,6]
all_positive = True
for element in data:
    if element <= 0:
        all_positive = False
        break

if all_positive:
    print('Processing all positive elements')
print('-'*80)


for i in range(5):
    print(i)
else:  # no break
    print('loop terminated normally (no break)')


for i in range(5):
    print(i)
    if i > 3:
        break
else:  # no break
    print('loop terminated normally (no break)')
print('='*80)


data = [1,2,3,-4,5,6]
all_positive = True
for element in data:
    if element <= 0:
        all_positive = False
        break

if all_positive:
    print('Processing all positive elements')
print('-----')

data = [1,2,3,-4,5,6]
for element in data:
    if element < 0:
        break
else:
    print('Processing all positive elements')
print('--')

data = [1,2,3,4,5,6]
for element in data:
    if element < 0:
        break
else:
    print('Processing all positive elements')
print('--')
