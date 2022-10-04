"""
1. Map áp dụng map(function, iterable, ...) 1 hàm 1 interable. Có thể dùng map thay cho vòng lặp for
2. filter áp dụng 1 func, 1 interable. Lấy ra các phần tử phù hợp. Có thể thay cho for, cấu trúc rẽ nhánh if.
3. reduce áp dụng 1 func, 1 interable. Thu về 1 giá trị. Áp dụng phép tính cộng dồn, nhân dồn.
4. Lambda là hàm thay cho các hàm thông thường.

"""

###########################################################################################
""" def fil(n):
    re = []
    if n in lst1:
        re.append(lst1.index(n))
    else:
        "False"
    return re

lst1 = [70,50,40,30]
lst2 = [70,80,90,50,50,10,70,40]

OUT = list(filter(fil,lst2))
print(OUT) """
###########################################################################################
""" OUT = list(filter(lambda n: n in lst1, lst2))
print(OUT) """
###########################################################################################
# def filterGetIndex(lstTemplate,lstCheck):
#     idx = []
#     for i in lstCheck:
#         if i in lstTemplate:
#             idx.append(lstTemplate.index(i))
#         else:
#             idx.append(False)
#     return idx

# lst1 = [70,50,40,30]
# lst2 = [70,80,90,50,50,10,70,40]
# print(filterGetIndex(lst1,lst2))
###########################################################################################
def filterGetIndex(lstTemplate,lstCheck1,lstCheck2): #whether that items of two lists in list template!!!
    idx = []
    for i,j in zip(lstCheck1,lstCheck2):
        if i and j in lstTemplate:
            idx.append(True)
            print("Have value",i,j)
        else:
            idx.append(False)
            print('Else Value:', "No Value")
    return idx

temp1 = [70,50,40,30,35]
lst2 = [70,50,35,30,50,70,35,40]
lst3 = [50,50,50,70,40,30,40,35]
print(filterGetIndex(temp1,lst2,lst3)) 
###########################################################################################
""" def filterGetIndex(lsttemp1,lsttemp2,lstCheck1,lstCheck2): #whether that items of two lists in two list template!!!
    idx = []
    for i,j in zip(lstCheck1,lstCheck2):
        if i in lsttemp1 and j in lsttemp2:
            idx.append(True)
        else:
            idx.append(False)
    return idx

temp1 = [70,60,40,30]
temp2 = [70,50,40,30]
lst1 = [70,80,60,30,50,10,70,40]
lst2 = [50,60,50,30,90,10,70,80]
print(filterGetIndex(temp1,temp2,lst1,lst2)) """
###########################################################################################
""" def filterGetIndex(lsttemp1,lsttemp2,lstCheck1,lstCheck2): 
    #get Index items of list templatewhether that items of two lists in two list template!!!
    idx = []
    for i,j in zip(lstCheck1,lstCheck2):
        if i in lsttemp1 and j in lsttemp2:
            idx.append(lsttemp1.index(i))
        else:
            idx.append(False)
    return idx

temp1 = [70,60,40,30]
temp2 = [70,50,40,30]
lst1 = [70,80,60,30,50,10,70,40]
lst2 = [50,60,50,30,90,10,70,80]
print(filterGetIndex(temp1,temp2,lst1,lst2))

temp1 = [450,600,450,800,1500]
temp2 = [2400,800,1500,1200,1000]
lst1 = [450,450,600,800,1500,450,800,600]
lst2 = [2400,1500,800,1200,1000,2400,1200,800]
print(filterGetIndex(temp1,temp2,lst1,lst2)) """

###########################################################################################
""" lst = [1,23,4,5,6,7,10]
#map(function, iterable, ...)
va_map = list(map(lambda n: n + 2,lst))
print(va_map) """
###########################################################################################
# from functools import reduce
# lst = [1,2,3,4]
# va_reduce = reduce(lambda x,y : x+y,lst)
# print(va_reduce)


