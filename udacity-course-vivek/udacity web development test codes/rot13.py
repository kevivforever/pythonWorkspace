from string import *
def create13_text(t):
    ROT13 = maketrans("ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz", 
    "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")
    new_t = t.translate(ROT13)
    print type(new_t)
    print new_t

input_text ="vivek naik <html>"
create13_text(input_text)
