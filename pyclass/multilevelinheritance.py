# program 1- Multilevel inheritance
# class A:
#     def get (self):
#         print("hello")
#
# class B(A):
#     def show (self):
#         print("wleome to")
#
# class C(B):
#     def disp(self):
#         print("python")
#
# a1=C()
# a1.get()
# a1.show()
# a1.disp()

# program 2-evenodd posneg lage
# class a:
#     def posneg (self,b):
#         if(b>=0):
#             print("positive number")
#         else:
#             print("negetive number")
#
#
# class b(a):
#     def evenodd (self,a):
#         if(a%2==0):
#             print("even number")
#         else:
#             print("odd number")
#
# class c(b):
#     def large (self,c,d):
#         if(c>d):
#             print("C is large")
#         else:
#             print("d is large")
#
# a1=c()
# a1.posneg(10)
# a1.evenodd(30)
# a1.large(10,20)

# program 3
# class A:
#     def get (self):
#         self.a=int(input("Enter a first number:"))
#         self.b=int(input("Enter second number:"))
#
# class B(A):
#     def add (self):
#         return self.a + self.b
#
# class C(B):
#     def sub (self):
#         return self.a - self.b
#
# a1=C()
# a1.get()
# print(a1.add())
# print(a1.sub())


# #program 4- using constructor name,add,find large no
class A:
    def __init__(self):
        print("abhijit")

class B(A):
    def __init__(self,a,b):
        super().__init__()
        print(a+b)

class C(B):
    def __init__(self,a,b,c,d,f):
        super().__init__(d,f)
        if((a>b) and (a>c)):
            print("A is large")
        elif((b>a) and (b>c)):
            print("B is large")
        else:
            print("C is large")

a1=C(10,20,30,40,50)
