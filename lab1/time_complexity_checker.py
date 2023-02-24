def check_time_complexity(functions, complexity_functions, nn):
    '''Funkcja sprawdza złożoność czasową podanych funkcji
    :param functions: lista referencji funkcji
    :param compexity_functions: lista nazw funkcji złożoności
    :param nn: lista argumentów dla których sprawdzamy złożoność czasową
    '''
    from timeit import default_timer as timer
    import math
    results = []

    for function in functions:
        print("====== FUNKCJA: "+str(function.__name__)+" ======")
        outcome = -1
        win = ""
        for Fn in complexity_functions:
            print(f"======= SPRAWDZANA ZLOZONOSC {Fn} ========")
            maxx = -1
            minn = -1
            sum = 0
            for n in nn:
                start = timer()
                if type(n) != list or type(n) != tuple:
                    function(n)
                else:
                    function(*n)
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
                results.append((function, win))
            print("======")
    for res in results:
        print(f"====== WYNIK: {res[0]}: {res[1]} ======")
