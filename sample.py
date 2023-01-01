# program 1
# class A:
#     def show(self,a,b):
#         self.x=a
#         self.y=b
#
# class B(A):
#     def add(self):
#         self.z=self.x+self.y
#         return self.z
#     def sub(self):
#         self.z=self.x-self.y
#         return self.z
#
# b1=B()
# b1.show(100,20)
# print(b1.add())
# print(b1.sub())

# program 2

class A:
    def evenodd(self,a):
        if(a% 2 == 0):
            print("even number")
        else:
            print("odd number")
class B(A):
    def posneg(self,b):
        if(b>=0):
            print("positive number")
        else:
            print("negative number")
class C(B):
    def large(self,b,c):
        if(b>c):
            print("B is large")
        else:
            print("c is large")

c1=C()
c1.evenodd(10)
c1.posneg(20)
c1.large(20,30)