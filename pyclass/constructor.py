#program 1-
# class A:
#     def __init__(self):
#         print("hello python")
#
#     def get(self):
#         print("hello")
#
# a1=A()
# a1.get()



#program 2
# class A:
#     def get(self): #__init__(self)
#         self.a=int(input("Enter first value:"))
#         self.b=int(input("Enter second value:"))
#
#     def large(self):
#         if(self.a > self.b):
#             print("A is large")
#         else:
#             print("B is large")
#
# b1=A()
# b1.get()
# b1.large()

#program 3
# class A:
#     def __init__(self):
#         self.a=int(input("Enter a value:"))
#
#     def multiple(self):
#         i=1
#         while(i<=10):
#             print(i*self.a)
#             i=i+1
# a1=A()
# a1.multiple()

#program 4-parameterized
# class A:
#     def get(self,a,b):   #__init__(self)
#         self.x=a
#         self.y=b
#     def large(self):
#         if(self.x > self.y):
#             print("A is large")
#         else:
#             print("B is large")
#
# a1=A()
# a1.get(10,20)
# a1.large()

#program 5 -Table
# class A():
#     def __init__(self,a):
#         self.x=a
#
#     def table(self):
#         for i in range(1,11):
#             print(i*self.x)
#
# a=int(input("Enter no:"))
# a1=A(a)
# a1.table()


#program 6-prametrised constructor
# class employs:
#     def __init__(self,a,b,c):
#         self.x=a
#         self.y=b
#         self.z=c
#
#     def info(self):
#         print("id",self.x)
#         print("name",self.y)
#         print("contno",self.z)
#
# a1=employs(1,"abhijit",7840909852)
# a1.info()
# a1=employs(2,"ajit",1887696149)
# a1.info()
# a1=employs(3,"swapnil",7854594355)
# a1.info()

#program 6
class A:
    def get (self,x):
        self.x=x

    def evenodd(self):
        if(self.x% 2==0):
            print("even number")
        else:
            print("odd number ")

    def posneg(self):
        
        if(self.x>=0):
            print(" positive number")
        else:
            print("negetive nunmber")

b1=A()
b1.get(10)
b1.evenodd()
b1.posneg()