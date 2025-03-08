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






