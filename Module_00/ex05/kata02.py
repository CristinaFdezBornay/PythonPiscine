if __name__ == "__main__":
    t = (3, 30, 2019, 9, 25)
    h, m, year, month, day = t
    print("{:02d}/{:02d}/{} {:02d}:{:02d}".format(month, day, year, h, m))
