def parallel(a, b):
    return (a*b)/(a+b)


while(True):
    try:
        a = float(input('a: '))
        b = float(input('b: '))
        print(parallel(a,b))
        print()
    except:
        print()
