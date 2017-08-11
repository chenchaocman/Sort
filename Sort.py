import time;

#装饰器，修带参数函数
def funtionTime(fun):

	def decorate(*args, **kwargs):
		
		timeStar = time.time()

		list = fun(*args, **kwargs)

		timeEnd = time.time()

		print("%d s",(timeEnd-timeStar))

		return list 


	return decorate






#冒泡排序
@funtionTime
def buddleSort(list):
	
	#获取列表长度
	list_count = len(list)
	#从列表中第二个元素开始作比较
	index = 1

	while index<list_count:
		
		#我当初困惑于，如何从列表的某个位置开始，不断地和之元素比较。
		#其实是不断改变position的位置实现的
		#
		pos = index

		while pos>0:

			currentElement = list[pos]
			forwardElement = list[pos-1]
			#符合条件交换两个元素位置，大者在前
			if currentElement>forwardElement:
				list[pos-1] = currentElement
				list[pos] = forwardElement

			pos-=1

		index+=1

	return list 
			   	   




#桶排序
@funtionTime
def bucketSort(list):
	
	buckets = [0]*1000

	for element in list:

		buckets[element]+=1

	bucketsList = []

	for idx, val in enumerate(buckets):

		if buckets[idx]!=0:
			bucketsList.append(idx)
			
		

	return bucketsList
		


@funtionTime
def quickSort(list):
	
	if len(list)<2:

		return list

	else:

		middleEle = (max(list)+min(list))/2

		rightList = []
		leftList = []

#注意for内部，防止middle为列表极限值
		for element in list:	
			if element<middleEle:
				rightList.append(element)
			else:
				leftList.append(element)

	    
		if len(rightList)==0:
			rightEle = leftList.pop(0)
			rightList.append(rightEle)
						

	
		return quickSort(rightList) + quickSort(leftList)



@funtionTime
def anotherQuickSort(left,right,list):

	if left>right:
		return	None

	dateumNum = list[left]	

	leftPos = left 
	rightPos = right 

#核心代码，不断地交换位置，这样其实是将整个数字分开
	while leftPos!=rightPos:

		while (leftPos<rightPos) and (list[rightPos]>=list[left]):
			rightPos-=1

		while (leftPos<rightPos) and (list[leftPos]<=list[left]):
			leftPos+=1

		

#因为基准是从left侧选取的，如果再从left侧遍利选取基准值的话，
#如果left侧就是最小值的话，那么它实际上是无法将列表中元素分开的
		temp = list[leftPos]
		list[leftPos] = list[rightPos]
		list[rightPos] = temp

		
	list[left] = list[leftPos]
	list[leftPos] = dateumNum


	anotherQuickSort(left, leftPos-1, list)
	anotherQuickSort(leftPos+1, right, list)

	return list 




				


			

		
		







	















if __name__ == '__main__':
	
	var_list = [3,4,5,6,7,1,2,10,2,3,6,77,44,33]
	testingList = var_list
	#var_list = buddleSort(var_list)

	#var_list = quickSort(var_list)
	
	var_list = bucketSort(var_list)
	
	#var_list = anotherQuickSort(0, len(testingList)-1, testingList)			

	print(var_list)

















