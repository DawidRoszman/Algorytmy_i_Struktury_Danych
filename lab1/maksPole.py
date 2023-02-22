from timeit import default_timer as timer

def time(fn):
    
    def inner(n, M):
        start = timer()
        print(fn(n, M))
        stop = timer()
        print(stop-start)
    return inner

@time
def NAIWNY(n, M):
    maks = 0
    lokalMaks = 0
    for x1 in range(0, n):
        for y1 in range(0, n):
            for x2 in range(n-1, x1-1, -1):
                for y2 in range(n-1, y1-1, -1):
                    lokalMaks = 0
                    for x in range(x1, x2+1):
                        for y in range(y1, y2+1):
                            lokalMaks += M[x][y]
                    if lokalMaks == (x2-x1+1)*(y2-y1+1) and lokalMaks > maks:
                        maks = lokalMaks
    return maks

@time
def DYNAMICZNY(n, M):
    maks = 0
    #  utworz tablicę kwadratową MM rozmiaru n
    #  i wypełnij ją zerami
    MM=[[0 for _ in range(n)] for _ in range(n)]
    for y in range(0, n):
        for x1 in range(0, n):
            iloczyn = 1
            for x2 in range(x1, n):
                iloczyn *= M[x2][y]
                MM[x1][x2] = iloczyn*(x2-x1+1+MM[x1][x2])
                if MM[x1][x2] > maks:
                    maks = MM[x1][x2]
    return maks


def CZULY(n, M):
    maks = 0
    lokalMaks = 0
    for x1 in range(0, n):
        for y1 in range(0, n):
            lokalMaks = 0
            x2 = x1
            ymaks = n-1
            while (x2 < n) and (M[x2][y1] == 1):
                y2 = y1
                while (y2 < ymaks+1) and (M[x2][y2] == 1):
                    y2 += 1
                ymaks = y2-1
                lokalMaks = (x2-x1+1)*(ymaks-y1+1)
                if lokalMaks > maks:
                    maks = lokalMaks
                x2 += 1
    return max


CZULY(3, [[1,1,1], [0,1,1], [0,1,0]])