

class Test:
    def __init__(self):
        pass
    
    def process(self):
        a = 15
        b = 10
        return a+b

if __name__=="__main__":
    obj = Test()
    res = obj.process()
    print(res)