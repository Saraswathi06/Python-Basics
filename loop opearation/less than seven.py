def lessthanseven(a):
    if(a<7):
        print(a,'is less than 7')
        lessthanseven(a+1)
    elif(a>7):
        print(a,'is not less than 7')
lessthanseven(4)
