#program 1
# class A:
#     def show(self):
#         self.a=int(input("Enter 1st no:"))
#         self.b=int(input("Enter 2nd no:"))
#         self.c=int(input("Eneter srd no:"))
#
# class B(A):
#     def disp(self):
#         if((self.a>self.b) and (self.a>self.c)):
#             print("A is large")
#         elif((self.b>self.a) and (self.b>self.c)):
#             print("B is large")
#         else:
#             print("C is large")
#
# b1=B()
# b1.show()
# b1.disp()

#program 2
# class A:
#     def show(self):
#         self.std={}
#         self.std["Name"]=input("Enter name:")
#         self.std["Rollno"]=int(input("Enter no:"))
#         self.std["class"]=input("Enter class:")
#
# class B(A):
#     def disp(self):
#         print(self.std)
#
# b1=B()
# b1.show()
# b1.disp()

#program 3
class A:
    def get(self,a,b):
        self.x=a
        self.y=b
class B(A):
    def add(self):
        print(self.x+self.y)
    def sub(self):
        print(self.x-self.y)

b1=B()
b1.get(50,90)
b1.add()
b1.sub()






















