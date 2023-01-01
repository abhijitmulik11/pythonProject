class A:
    def evenodd(self,a):
        if(a%2==0):
            print("Even number")
        else:
            print("odd number")

class B(A):
    def posneg(self,b):
        if(b>0):
            print("positive number")
        else:
            print("negative number")
