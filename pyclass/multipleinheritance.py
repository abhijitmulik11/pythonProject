# program 1-multiple
# class A:
#     def get (self):
#         print("Class A")
#
# class B:
#     def show(self):
#         print("Class B")
#
# class C:
#     def show1(self):
#         print("Class C")
#
# class D(A,B,C):
#     def disp(self):
#         print("Class D")
#
# a1=D()
# a1.get()
# a1.show()
# a1.show1()
# a1.disp()

# program 2- 1)user input name,password 2)prn num user
# class A:
#     def get (self):
#         self.name=input("Enter your name:")
#         self.Pass=input("Enter your password")
#
# class B:
#     def prn(self):
#         self.prn=int(input("Enter your prn no"))
#
# class C:
#     def show(self):
#         if((self.name=="Abhijit") and (self.Pass=="admin")):
#              if(self.prn==123456789):
#                    print("login successful")
#              else:
#                    print("wrong name & wrong pass")
#         else:
#             print("wrong prn")
#
# class D(A,B,C):
#     def dis (self):
#         print("*******")
#
# a1=D()
# a1.get()
# a1.prn()
# a1.show()
# a1.dis()


# # program 3-1)name 2)positive negetive 3)evenodd
class A:
    def get(self):
        print("Abhjit")


class B():
    def show(self, a):

        if (a >= 0):
            print("positive number")
        else:
            print("negetive number")


class C(A,B):
    def displ(self, b):
        if (b % 2 == 0):
            print("even number ")
        else:
            print("odd number")


a1 = C()
a1.get()
a1.show(10)
a1.displ(17)

