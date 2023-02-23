import math
from timeit import default_timer as timer


def f1(n):
    s = 0
    for j in range(1, n):
        s = s + 1 / j
    return s


def f2(n):
    s = 0
    for j in range(1, n):
        for k in range(1, n):
            s = s + k / j
    return s


def f3(n):
    s = 0
    for j in range(1, n):
        for k in range(j, n):
            s = s + k / j
    return s


def f4(n):
    s = 0
    for j in range(1, n):
        k = 2
        while k <= n:
            s = s + k / j
            k = k * 2
    return s


def f5(n):
    s = 0
    k = 2
    while k <= n:
        s = s + 1 / k
        k = k * 2
    return s


funkcje = ["f1(n)", "f2(n)", "f3(n)", "f4(n)", "f5(n)"]
nn = [2000, 4000, 8000, 16000, 32000]
Fn_arr = ["math.log(n,2)", "n", "n*100", "n*math.log(n,2)", "n*n"]


def check_time_complexity(functions, complexity_functions):
    """Funkcja sprawdza złożoność czasową podanych funkcji
    :param functions: lista nazw funkcji
    :param compexity_functions: lista nazw funkcji złożoności
    """
    for function in functions:
        print("====== FUNKCJA: "+function+" ======")
        outcome = -1
        win = ""
        for Fn in complexity_functions:
            maxx = -1
            minn = -1
            sum = 0
            for n in nn:
                start = timer()
                exec(function)
                stop = timer()
                Tn = stop - start
                Fnn = eval(Fn)
                if maxx < 0 or Fnn/Tn > maxx:
                    maxx = Fnn / Tn
                if minn < 0 or Fnn / Tn < minn:
                    minn = Fnn / Tn
                sum += Fnn / Tn
                print(n, Tn, Fnn / Tn)
            res = (maxx - minn)/(sum/len(nn))
            print(res)
            if outcome < 0 or res < outcome:
                outcome = res
                win = Fn
            print("======")
        print("====== WYNIK: "+win+" ======")



# inne funkcje czasu:

# Fn=math.log(n,2)
# Fn=n
# Fn=100*n
# Fn=n*math.log(n,2)
# Fn=n*n
