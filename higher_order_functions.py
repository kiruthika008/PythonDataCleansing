from functools import reduce
mylist=[1,2,3,4,5]

#Map example to square all even numbers in list
square_list=list(map(lambda x: x**2 , mylist))
print(square_list)

square_list_even=list(map(lambda x: x**2, [x for x in mylist if x%2==0]))
print(square_list_even)

square_list_odd=list(map(lambda x: x**2, [x for x in mylist if x%2!=0]))
print(square_list_odd)


#Reduce example to sum all numbers in list
sum_list=reduce(lambda x,y : x+y,mylist)
print(sum_list)

sum_list_even=reduce(lambda x,y : x+y,[x for x in mylist if x%2==0])
print(sum_list_even)

sum_list_odd=reduce(lambda x,y : x+y,[x for x in mylist if x%2!=0])
print(sum_list_odd)


#filter exaample to filter based on value in a list

filter_list=list(filter(lambda x:x>2,mylist))
print(filter_list)

filter_list=list(filter(lambda x:x>2,mylist))
print(filter_list)


#sorted exaample to sort value in a list
#ascending 
sorted_list_asc=list(sorted(mylist,key= lambda x:x))
print(sorted_list_asc)

#get 2nd largest number in ascending
sorted_list_asc_2nd=list(sorted(mylist,key= lambda x:x))[1]
print(sorted_list_asc_2nd)

#ascending 
sorted_list_desc=list(sorted(mylist,key= lambda x:-x))
print(sorted_list_desc)

#get third largest number desc
sorted_list_desc_3rd=list(sorted(mylist,key= lambda x:-x))[2]
print(sorted_list_desc_3rd)


#any any() → OR logic
result = any(map(lambda x: x < 0, mylist))
print(result)

#all all() → AND logic

result = all(map(lambda x: x < 6, mylist))
print(result)