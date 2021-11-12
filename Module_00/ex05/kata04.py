if __name__ == "__main__":
    t = ( 0, 4, 132.42222, 10000, 12345.67)
    module, ex, t1, t2, t3 = t
    print("module_{:02}, ex_{:02} : {:3.2f}, {:.2e}, {:.2e}".format(module, ex, t1, t2, t3))
