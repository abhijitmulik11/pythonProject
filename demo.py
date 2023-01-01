# class A:
#     def get(self):
#         self.a=int(input("Enter first no:"))
#         self.b=int(input("Enter second no:"))
#         self.c=int(input("Enter third no:"))
#
# class B(A):
#     def large(self):
#         if((self.a>self.b) and (self.a>self.c)):
#             print("A is large")
#         elif((self.b>self.a) and (self.b>self.c)):
#             print("B is large")
#         else:
#             print("C is large")
# b1=B()
# b1.get()
# b1.large()

#program 2
# class A:
#     def get(self,a,b):
#         self.x=a
#         self.y=b
# class B(A):
#     def add(self):
#         return(self.x+self.y)
#     def sub(self):
#         return(self.x-self.y)
# b1=B()
# b1.get(100,20)
# print(b1.add())
# print(b1.sub())

#program 3

class A:
    def posneg(self,a):
        if(a >0):
            return("positive number")
        else:
            return("negative number")
class B(A):
    def large(self,a,b):
        if(a>b):
            return("A is large")
        else:
            return("B is large")
class C(A):
    def show(self,b):
        return "B=",b
class D(A):
    def add(self,a,b):
        return(a+b)
b1=B()
print(b1.posneg(10))
print(b1.large(10,20))
c1=C()
print(c1.show(10))
d1=D()
print(d1.add(100,20))
