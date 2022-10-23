g = 10

def addone(k):
	k = k + 1
	return k

def addOneList(k):
	k[0][0] = 10


def myToupper(s):

	print(id(s))
	s = s.upper()
	print(id(s))

	return 

def testOfReference():

	a = [[1, 2, 3], [4, 5, 6]]
	
	for row in a:
		row[0] = 10
		print(row)
	print(a)
	
	addOneList(a)


	b = [15, -2, 7]

	for i, ele in enumerate(b): #[(0, 15), (1, -2), (2, 7)]
		
		b[i] = 10
	

	if(b[0] != 10):
		hello = 10
	print(hello)

	c = 10
	addone(c)
	print(c)

	s = "abc"
	myToupper(s)
	print(s)

def testOfAddress():
	a = 10
	b = 10
	print(id(a))
	print(id(b))
	a = 20.2
	print(id(a))
	a = 'ihfoewhfie'
	print(id(a))
	a = 1283212387129371237812037123712803780
	print(id(a))


#testOfReference()
#testOfAddress()

count = 0
def quickSort(a, left, right): # recursive function
	if(right <= left):
		return
	original_left = left
	original_right = right
	pivotIdx = left
	pivot = a[left]
	left += 1
	
	while(left < right):

		while(a[left] < pivot):
			left += 1	
		while(a[right] > pivot):
			right -= 1
		print(f"left = {left}, right = {right}")
		print(f"left value = {a[left]}, right value = {a[right]}")
		if(left < right):
			tmp = a[left]
			a[left] = a[right]
			a[right] = tmp
		print(a)
	exit(0)

	if(a[left] < pivot):
		tmp = a[left]
		a[left] = pivot
		a[pivotIdx] = a[left]
	elif(a[left] > pivot):
		tmp = a[left-1]
		a[left-1] = pivot
		a[pivotIdx] = a[left-1]

	quickSort(a, original_left, left-1)
	quickSort(a, left + 1, original_right)
	return





a = [6, 2, 5, 4, 7, 8 ,2, 7, 2, 1, -3]
quickSort(a, 0, len(a)-1)


'''
data = [89, 34, 23, 78, 67, 100, 66, 29, 79, 55, 78, 88, 92, 96, 96, 23]

def quicksort(data, left, right): # 輸入資料，和從兩邊開始的位置
    if left >= right :            # 如果左邊大於右邊，就跳出function
        return

    i = left                      # 左邊的代理人
    j = right                     # 右邊的代理人
    key = data[left]                 # 基準點

    while i != j:                  
        while data[j] > key and i < j:   # 從右邊開始找，找比基準點小的值
            j -= 1
        while data[i] <= key and i < j:  # 從左邊開始找，找比基準點大的值
            i += 1
        if i < j:                        # 當左右代理人沒有相遇時，互換值
            data[i], data[j] = data[j], data[i] 

    # 將基準點歸換至代理人相遇點
    data[left] = data[i] 
    data[i] = key

    quicksort(data, left, i-1)   # 繼續處理較小部分的子循環
    quicksort(data, i+1, right)  # 繼續處理較大部分的子循環

quicksort(data, 0, len(data)-1)
print(data)
'''

