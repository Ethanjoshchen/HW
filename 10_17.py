'''
a = [1, 2, 3, 4, 5, 6]
# print info
print(f'a = {a}') #fstring
print(f'type a = {type(a)}')

# access
a[0] = 10
print(f'a[0] = {a[0]}')

# concatenate
a = a + [1, 2, 3]
print(f'After concatenating, a becomes {a}')


print(a[1: 3]) # slice
print(a[::2])
print(f'len of a = {len(a)}')
'''


#tuple
'''
s = (1 ,2 ,3)
print(type(s))
print(s)
s = list(s)
print(type(s))
print(s)
'''

'''
print(f"list(range(31)) ={list(range(31))}")

print("First for:")
for i in list(range(31)):
	print(f"	i = {i}")

print("Second for:")
for i in [10, 20, 30]:
	print(f"	i = {i}")

# initialize
grades = [0] * 30
grades.append(50) # method of list

#traverse 遍歷
for i in range(len(grades)):
	grades[i] = i * 10
	print(i, grades[i])

for ele in grades:
	ele *= -1
	print(f'ele = {ele}')


for i, ele in list(enumerate(grades)):
	print(i , ele)


for i in range(len(grades[0:5])):
	grades[i] = int(input(f"Input the grade of student {i} : "))
	
print(grades)
'''

'''
grades = []

print(len(grades)) # 0

count = 0
while(True):
	grades.append(int(input(f"Input the grade of student {count} : ")))
	count += 1
	if(grades[-1] == 101):
		grades = grades[: len(grades) - 1]
		break
	

#print(sorted(grades))

#grades.sort()
grades = sorted(grades)
print(grades)
'''





def mySort(my_list):
	for i in range(len(my_list)): 
		# i is the index of next inserted number
		nextNum = my_list[i]
		for j in list(range(0, i))[::-1]:
			print(f"nextNum = {nextNum}, compare to index = {j}, number {my_list[j]}")
			# j means the index of the sorted list
			if(nextNum < my_list[j]):
				my_list[j+1] = my_list[j]
			else:
				my_list[j+1] = nextNum
				break

			if( j == 0):
				my_list[0] = nextNum
			

		print(f'list becomes : {my_list[:i+1]}')
	return my_list




def main():
	my_list = [10, 3, 5, 7, 3, 2, 1, -5]
	print(my_list)

	print("Expected list = ", sorted(my_list))
	print("My sort = ", mySort(my_list))

main()










