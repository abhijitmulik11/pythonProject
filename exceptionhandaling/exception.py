#syntax
# try:
#     body
# except:
#     error

#program 1
# try:
#     a=50/0
#     print(a)
# except:
#     print("error created")

#program 2
# try:
#     a=int(input("Enter a number:"))
#     print(a)
# except:
#     print("Pls enter number")

#program 3
# try:
#     a=int(input("Enter first no:"))
#     b=int(input("Enter second no:"))
#     print(a+b)
# except:
#     print("pls enter valid number")

#program 4:
# try:
#     a=int(input("Enter value for a:"))
#     print(a)
# except Exception as e:
#     print(e)

#program 5
# try:
#     bca={}
#     bca.add(int(input("Enter vlaue for set:")))
#     print(bca)
# except Exception as e:
#     print(e)

#program 6
# try:
#     bca={}
#     bca["a"]=input("enter value for for dict:")
#     print(bca)
# except Exception as e:
#     print(e)

#program 7
# try:
#     tup=(1,2,"abc",4)
#     print(max(tup))
# except Exception as e:
#     print(e)

#programm 8
try:
    def add():
        a=10
        b=20
        print(a+b)
    def sub():
        print(a-b)
    add()
    sub()
except Exception as e:
    print(e)