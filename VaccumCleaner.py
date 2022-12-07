start = {'a':1, 'b':0}

goal = {'a':0, 'b': 0}

vc = 'a' #vaccum cleaner 
cost =0


while(start != goal):
    

    if vc=='a' and start['a'] == 1:
        cost = cost +1
        vc = 'b'
        start['a'] =0
        cost = cost+1

    if vc=='a' and start['a'] == 0:
        vc='b'
        cost= cost+1

    if vc=='b' and start['b'] == 1:
        cost = cost +1
        vc = 'a'
        start['b'] =0
        cost = cost+1

    if vc=='b' and start['b'] == 0:
        cost= cost+1
        vc='a'


print("cost is")
print(cost)



