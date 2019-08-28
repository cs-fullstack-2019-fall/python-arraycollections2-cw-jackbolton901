# problem 1
person_array = ["Kenn", "Kevin", "Erin", "Autumn"]
def stupid_array_tricks(person_array):
        # a)
    print(person_array[1:3])
        # b)
    print(person_array[2:5])
        # c)
    person_array.insert(2, "Chuck")
    print(person_array)
        # d)
    person_array.pop(1)
    print(person_array)
stupid_array_tricks(person_array)

Problem 2
userIn = ""
while userIn != q: # !! : q should be a string
    userIn = input("Enter something or press q to quit")

# Problem 3
dataArray = ['GOOD_DATA', 'DECENT_DATA', 'BAD_DATA', 'DECENT_DATA', 'GOOD_DATA',
             'BAD_DATA', 'GOOD_DATA', 'DECENT_DATA', 'BAD_DATA', 'GOOD_DATA']
print(len(dataArray))
dataArray.remove('BAD_DATA') # !! : this only removes the first instance of BAD_DATA
print(len(dataArray))

# Problem 4
score_list = [21, 14, 6, 8, 28, 42, 21]
sum = (sum(score_list))
max = max(score_list)
min = min(score_list)
print(f'The sum of all scores is {sum}.')
print(f'The maximum number is {max}')
print(f'The minimum number is {min}')