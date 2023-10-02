def myfunc(**kwargs):
    for key, value in kwargs.items():
        print(key,value)

myfunc(name='peter',age=27, address='xyz')        