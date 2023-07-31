def keytodict(**kwargs):
    res = {}
    for key, value in kwargs.items():
        try:
            res[value] = key
        except:
            res[str(value)] = key
    print(res)


keytodict(res=1, reverse=[1, 2, 3])
