#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    list_t = dir(hidden_4)
    for li in list_t:
        if li[0] != "_":
            print("{}".format(li))
