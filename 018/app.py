# 1. Get data
total_people = int(input('Total people: '))

base_cost = []
for i in range(total_people):
    cost = int(input(f'Cost of goods/service from people #{i+1}: '))
    base_cost.append(cost)

fee = int(input('Final fee: '))
discount = int(input('Final discount: '))

# 2. Calculate and show
print('='*50)
percentage_cost = []
for i, c in enumerate(base_cost):
    p = c/sum(base_cost)
    percentage_cost.append(p)
    print(f'Percentage payment for people #{i+1} is {p:.2%}')

total_cost = sum(base_cost) + fee - discount
print(f'Total cost: {" + ".join([str(c) for c in base_cost])} + {fee} - {discount} = {total_cost}')

print('='*50)
each_cost = [p*total_cost for p in percentage_cost]
for i in range(total_people):
    print(f'People #{i+1} pay: {percentage_cost[i]:.2%} x {total_cost} = {each_cost[i]}')
