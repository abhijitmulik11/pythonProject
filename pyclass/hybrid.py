#program 1
# class A:
#     def get(self):
#         print("welcome to")
# class B(A):
#     def show(self):
#         print("python")
#
# class C(A):
#     def disp(self):
#         print("hello")
#
# class D(B,C):
#     def get1(self):
#         print("SGM")
#
# d1=D()
# d1.disp()
# d1.get()
# d1.show()
# d1.get1()

#program 2
class A:
    def get(self):
        print("Abhijit")

class B(A):
    def show(self,a):
        print("integer", a)

class C(A):
    def disp(self,b):
        print("float" , b)

class D(B,C):
    def get1(self,c):
        print("string", c)

d1=D()
d1.get()
d1.show(10)
d1.disp(2.3)
d1.get1("abhi")


#program 3
# class A:
#     def get(self):
#         self.a=int(input("Enter first number:"))
#         self.b=int(input("Enter second number:"))
#
# class B(A):
#     def add(self):
#         print(self.a + self.b)
#
# class C(A):
#     def sub(self):
#         print(self.a- self.b)
#
# class D(B,C):
#     def mul(self):
#         print(self.a*self.b)
#
# d1=D()
# d1.add()
# d1.sub()
# d1.mul()