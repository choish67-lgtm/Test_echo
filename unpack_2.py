def f(*args, **kwargs):
    #print("Positional:", args)
    print("Named:", kwargs)

#f(100, 50, 25, 1, "dsf")
f(galleons=100, sickels=50, knuts=25)