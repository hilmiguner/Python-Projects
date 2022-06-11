def add(*params):
    print(len(params))
    print(params)
    print(params[3])
    print(sum(params))
add(1,2,3,4,5,6)

print(100*"-")

def altAdd(*params):
    temp = 0
    for i in params:
        temp += i
    return (f"Toplam: {temp}")

print(altAdd(5,10,20,30))