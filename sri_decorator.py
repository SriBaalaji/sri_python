import time

def Trans(FuncPointerTrans):
    def innerTrans(*args, **kwds):
        print('Transaction started')
        i = FuncPointerTrans(*args, **kwds)
        print('Transaction completed')
        return i
    return innerTrans

def Time(FuncPointerTime):
    def innerTime(*args, **kwds):
        starttime = time.strftime("TIme: %H:%M:%S", time.localtime())
        print(starttime)
        i = FuncPointerTime(*args, **kwds)
        endtime = time.strftime("Time: %H:%M:%S", time.localtime())
        print(endtime)
        return i
    return innerTime

@Trans
@Time
def atm(a : int):
    print('Fetching Cash =', a)
    time.sleep(3)

atm(300)
