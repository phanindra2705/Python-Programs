# for loop
# prices = [10,20,30]
# total = 0
# for item in prices:
#     total = total + item
# print(item)

# Nested loops
# for x in range(4):
#     for y in range(3):
#         print(f'({x}, {y})')


nums = [2,2,2,6,6,6]

# for x in nums:
#     output = ''
#     for y in range(x):
#         output = output + 'X'
#     print(output)

for x in nums:
    for y in 'X':
        print(x * y)
