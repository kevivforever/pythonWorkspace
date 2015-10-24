def func1(x, y, z):
    print x
    print y 
    print z                 

def func2(*args):
    # Convert args tuple to a list so we can modify it
    args = list(args)
    args[0] = 'Hello'
    args[1] = 'awesome'
    func1(*args)

func2('Goodbye', 'cruel', 'world!')
