class A:
    def spam(self):
        print('A.spam')
        super().spam()

a = A()
#a.spam() #error

class B:
    def spam(self):
        print('B.spam')

class C(A,B):
    pass

c = C()
c.spam()