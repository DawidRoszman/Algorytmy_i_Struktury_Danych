import math
from timeit import default_timer as timer
import time_complexity_checker as tcc


def f1(n):
    s = 0
    for j in range(1, n):
        s = s+1/j
    return s


def f2(n):
    s = 0
    for j in range(1, n):
        for k in range(1, n):
            s = s+k/j
    return s


def f3(n):
    s = 0
    for j in range(1, n):
        for k in range(j, n):
            s = s+k/j
    return s


def f4(n):
    s = 0
    for j in range(1, n):
        k = 2
        while k <= n:
            s = s+k/j
            k = k*2
    return s


def f5(n):
    s = 0
    k = 2
    while k <= n:
        s = s+1/k
        k = k*2
    return s


nn = [2000, 4000, 8000, 16000, 32000]

# for n in nn:
#     start = timer()
#     f2(n)
#     stop = timer()
#     Tn = stop-start
#     Fn = math.log(n, 2)
#     print(n, Tn, Fn/Tn)

# inne funkcje czasu:

tcc.check_time_complexity([f2, f3, f4, f5],
                          ["n", "math.log(n, 2)", "n", "n*100",
                           "n*math.log(n, 2)", "n*n"], nn)


''' n*n
for n in nn:
    start = timer()
    f2(n)
    stop = timer()
    Tn = stop-start
    Fn = n*n
    print(n, Tn, Fn/Tn)

2000 0.9143088000000716 4374889.534038923
4000 3.2258497000002535 4959933.502171147
8000 12.833367499999895 4986999.709935878
16000 49.74931400000014 5145799.598362287
32000 205.0424134 4994088.701064811

'''
# funkcje_czasu(f3, n**2, nn)
''' n*n
for n in nn:
    start = timer()
    f2(n)
    stop = timer()
    Tn = stop-start
    Fn = n*n
    print(n, Tn, Fn/Tn)

2000 0.9143088000000716 4374889.534038923
4000 3.2258497000002535 4959933.502171147
8000 12.833367499999895 4986999.709935878
16000 49.74931400000014 5145799.598362287
32000 205.0424134 4994088.701064811

'''
# funkcje_czasu(f4, (n*math.log(n, 2)), nn)
''' n*lg(n)
for n in nn:
    start = timer()
    f2(n)
    stop = timer()
    Tn = stop-start
    Fn = n*math.log(n, 2)
    print(n, Tn, Fn/Tn)

2000 0.6821924999999283 32148.650958969032
4000 3.071384300000318 15583.57159624844
8000 13.099654499999815 7918.245040531273
16000 63.15771390000009 3538.0088156514653
32000 214.22237900000027 2235.5512031223693

'''
# funkcje_czasu(f5, math.log(n, 2), nn)
''' lg(n)
for n in nn:
    start = timer()
    f2(n)
    stop = timer()
    Tn = stop-start
    Fn = math.log(n, 2)
    print(n, Tn, Fn/Tn)

2000 1.056992799999989 10.3745118080863
4000 3.051919999999882 3.920739824327817
8000 11.967524099999991 1.0834140943707893
16000 47.57502789999944 0.2935528343570819
32000 217.61378700000023 0.06877222482536031
'''
# Fn=math.log(n,2)
# Fn=n
# Fn=100*n
# Fn=n*math.log(n,2)
# Fn=n*n
