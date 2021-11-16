import time
import progressbar

def ft_progress(lst):
    widgets = [progressbar.ETA(),
                ' [', progressbar.Percentage(), ']'
                ' [',
                progressbar.Bar(marker='=',left='=',right='', marker_wrap=('','>')),
                '] ',
                progressbar.Timer(format= 'elapsed time: %(elapsed)s')
            ]
    
    bar = progressbar.ProgressBar(max_value=len(lst), widgets=widgets).start()
    for i in range(len(lst)):
        yield bar.update(i)

ret = 0
for elem in ft_progress(range(100)):
    time.sleep(0.1)
    print(elem)