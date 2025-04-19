from method_timer import MethodTimer

class TestClass:
    def __init__(self, arg1, arg2, arg3=3, arg4="arg4"):
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
        self.arg4 = arg4

    def print1(self):
        print(self.arg1)

    def print2(self):
        print(self.arg2)

    def print3(self):
        print(self.arg3)

    def print4(self):
        print(self.arg4)

if __name__ == "__main__":
    # test obj based init
    obj_ = TestClass(1, 2,)
    obj1 = MethodTimer(obj_, ())
    # test obj based init with keyword args
    obj2_ = TestClass( 1, 2, arg3=3, arg4="test")
    obj2 = MethodTimer(obj2_, ())
    res = [obj1.print1() for i in range(500)]
    data = obj1.data_
    obj1.plot('print1')