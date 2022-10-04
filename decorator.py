
"""
Decorator: Là hàm trang trí, thêm bớt các thông tin vào một hàm có sẵn mà cần cần viết lại hàm đó nữa! 
Lưu ý :
        - Hàm cần có chữ @ để gọi decorator  lên mà dùng.
        - Hàm def cà @ phải cùng số lượng Parameter truyền vào.
        - @ đứng ở vị trí nào thì sẽ mang tụi nó vào decorator dùng.
"""
# class nameClass:
#     def __init__(self,name,age,weight):
#         self.ten = name
#         self.tuoi = age
#         self.cannang = weight

# addValue = nameClass("Due",24,"75kg")
# print(addValue.ten)
# print(addValue.tuoi)
# print(addValue.cannang)
####################################################################
""" Explain Decorator """
# def show_text(in1):
#     return 'this is a first information: {}'. format(in1)
# def decor_func(func):
#     def wrapper(in2):
#         return "This part is added into function: {}".format(func(in2))
#     return wrapper

# var = decor_func(show_text)
# x = var("BIM")
# print(x)

"""Contraction"""
# def decor_func(func): # func ví như là tham số (parameter)
#     def wrapper(infor):
#         return "This part is added into function: {}".format(func(infor))
#     return wrapper
# @decor_func
# def show_text(info):
#     return 'this is a first information: {}'. format(info)

# getValue = show_text("BIM3DM")
# print(getValue)

########################################################################
""""Example 01"""
# def minus(z1,z2):
#     var = z1 -z2
#     return var
# def deco_minus(func):
#     def result(inp1 , inp2):
#         return "The result is {}".format(func(inp1,inp2))
#     return result

# add = deco_minus(minus)
# re = add(30,50)
# print(re)

"""Contraction"""
# def dcor_func(func):
#     def result(ipt1 ,ipt2):
#         return "The result is {}".format(func(ipt1,ipt2))
#     return result
# @dcor_func
# def minus(z1,z2):
#     var = z1 - z2
#     return var

# re = minus(30,50)
# print(re)


########################################################################
""""Example 02"""
# def inf(func):
#     def alert(str):
#         return "Not result {} ".format(func(str))
#     return alert
# @inf
# def information(text):
#     return ", calculate agian {}".format(text)

# out = information("stupid")
# print(out)

########################################################################


