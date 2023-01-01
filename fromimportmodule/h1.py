class A:
    def get(self,username,password):
        self.x=username
        self.y=password

class B(A):
    def show(self):
        if((self.x=="admin") and (self.y=="pass")):
            return("login successfull")
        else:
            return("login fail")
