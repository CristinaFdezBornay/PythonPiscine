import time
import progressbar

def ft_progress(lst):
    widgets = [progressbar.ETA(),
                ' [', progressbar.Percentage(), ']'
                ' [',
                progressbar.Bar(marker='=',left='=',right='', marker_wrap=('','>')),
                '] ',
                progressbar.Counter(format='%(value)d/{}'.format(len(lst))),' ',
                progressbar.Timer(format= 'elapsed time: %(elapsed)s')
            ]

    bar = progressbar.ProgressBar(max_value=len(lst), widgets=widgets).start()
    for i in range(len(lst)):
        bar.update(i)
        yield i*i

if __name__ == "__main__":
    ret = 0
    X = range(100, 200)
    listy = X
    for elem in ft_progress(listy):
        ret += (elem + 3) % 5
        time.sleep(0.1)
    print()
    print(ret)