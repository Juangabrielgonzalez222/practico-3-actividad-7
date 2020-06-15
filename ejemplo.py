class A():
    __a=0
    def __init__(self,a):
        self.__a=a
        print("A")
    def mos(self):
        print(self.__a)
    def getA(self):
        return self.__a
class B(A):
    __b=0
    def __init__(self,a,b,c):
        self.__b=b
        print("B")
        super().__init__(a,b,c)
    def mos(self):
        super().mos()
        print(self.__b)
    def getB(self):
        print(self.getA())
class C(A):
    __c=0
    def __init__(self,a,b,c):
        self.__c=c
        print("C")
        super().__init__(a)
    def mos(self):
        super().mos()
        print(self.__c)
    def getC(self):
        print(self.getA())
class D(B,C):
    __d=0
    def __init__(self,a,b,c,d):
        self.__d=d
        super().__init__(a, b, c)
    def mos(self):
        super().mos()
        print(self.__d)
    def a(self):
        return self.getA()
    def c(self):
        self.getC()
        self.getB()
d=D(1,2,3,4)
d.mos()
d.c()
     