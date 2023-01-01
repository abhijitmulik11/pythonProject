class A:
    def voting(self,a):
        if(a>18):
            print("vote")
        else:
            print("not applicable for vote ")

class B(A):
    def table(self,a):
        i=1
        while(i <= 10):
            print(a*i)
            i=i+1
