list =[6,1,2,8,3,4,7,10,5]
list_size=len(list)
list.sort()
index=0
diff = list[index]-index
while list[index]-index==diff:
    index+=1
print (index+diff)