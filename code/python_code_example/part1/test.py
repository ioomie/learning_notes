list_ = []

def sin(number):
    list_.append(number)

def sout():
    list_.pop(0)

sin(1)
sin(2)
sin(3)
sin(4)
sout()
print(list_)