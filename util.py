# For PTS
def setIndex(index):
    return bytearray([2,index])

def bcd(n):
    assert(n<=100)
    return n%10+((n/10)%100)*2**4

def setCode(code):
    return bytearray([1]+[bcd(code/100**i%100) for i in range(0,4)])

def setFreq(index,freq):
    return setIndex(index)+setCode(freq)

# You may need to edit this function to match your top level design.    
def transform(qtext):
    n = float(qtext)
    n = n*10/3
    return int(n)
    