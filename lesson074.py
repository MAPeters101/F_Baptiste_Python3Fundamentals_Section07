price = 100

while price > 90:
    print(f'price = {price} - waiting for price to come down...')
    price -= 1

print(f'buying at {price}')
print('-'*80)

price = 100
while price < 50:
    print(f'price={price}')
print('Done')
print('-'*80)

# price = 100
# while price > 90:
#     print(price)
#     price += 1
# print('Done')

data = [100, 200, 300, 400, 500]
while len(data) > 0:
    last_element = data.pop()
    print(f'Processing element: {last_element}')
    print(data)
print('-'*80)


data = [100, 200, 300, 400, 500]
for i in range(len(data)):
    print(f'i = {i}')
    print(f'before removing element: data = {data}')
    element = data.pop(i)
    print(f'Processing element: {element}')
    print(f'after removing element: data = {data}')
    print('-'*10)

print('-'*80)






