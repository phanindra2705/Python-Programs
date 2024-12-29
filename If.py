# num = input('enter a num ')
#
# if int(num) % 2 == 0:
#     print('num is even')
# else:
#     print('num is odd')



# temp=input('enter the num ')
#
# if int(temp)>30:
#     print('hot day')
# elif int(temp)<10:
#     print('cold day')
# else:
#     print('Its neither hot nor cold')

# name = input('enter name')

# if len(name)<3:
#     print("Name must be atleast 3 characters")
# elif len(name)>50:
#     print('name can be max of 50 characters')
# else:
#     print('name looks good')

weight = int(input('weight'))

unit = input('Lbs or Kgs ')


if unit == 'L':
    print(weight * 0.45)
elif unit=='K':
    print(weight * 2.2)

