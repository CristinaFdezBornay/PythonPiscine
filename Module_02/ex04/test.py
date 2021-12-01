import myminipack

if __name__ == "__main__":
    ret = 0
    X = range(100, 200)
    listy = X
    for elem in myminipack.Progress.ft_progress(listy):
        ret += (elem + 3) % 5
        time.sleep(0.1)
    print()
    print(ret)