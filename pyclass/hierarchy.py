#program 1
# class A:
#     def get (self):
#         print("hello")
#
# class B(A):
#     def show (self):
#         print("welcome to ")
#
# class C(A):
#     def disp (self):
#         print("python")
#
# class D(A):
#     def get1 (self):
#         print("SGM")
#
# b1=B()
# b1.get()
# b1.show()
# c1=C()
# c1.get()
# c1.disp()
# d1=D()
# d1.get()
# d1.get1()

#program 2
class A:
    def get(self):
        print("welcome to voting system")

class B(A):
    def age(self):
        self.age = int(input("Enter your age:"))

class C(B):
    def info(self):
        if(self.age >18):
            self.name=input("Enter your name:")
            print(self.name)
            self.contno=int(input("Enter your cont number:"))
            print(self.contno)
            self.address=input("Enter your adress:")
            print(self.address)
        else:
            print("Not appplicable for voting")

class D(C):
    def displ(self):
        print("Thank you for registration")


d1=D()
d1.get()
d1.age()
d1.info()
d1.displ()


