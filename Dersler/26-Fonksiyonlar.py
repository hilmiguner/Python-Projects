def sayHello():
    print("Hello")
sayHello()

print(100*"-")

def sayHelloWithParameter(name):
    print(f"Hello {name}")
sayHelloWithParameter("Hilmi")

print(100*"-")

def sayHelloWithParameter2(name = "Hilmi"):
    print(f"Hello {name}")
sayHelloWithParameter2("Kemal")
sayHelloWithParameter2()

print(100*"-")

def sayHelloWithReturn(name):
    return (f"Hello {name}")
msg = sayHelloWithReturn("Dönüş")
print(msg)

print(100*"-")

def total(num1,num2):
    return num1+num2
result = total(5,10)
print(result)

print(100*"-")

def ageCalculator(birthyear):
    return 2021-birthyear
def retireCalculator(birthyear,name):
    age = ageCalculator(birthyear)
    retiring = 65 - age
    if retiring > 0:
        print(f"Sayın {name}, emekliliğinize {retiring} yıl kaldı.")
    elif retiring < 0:
        print(f"Sayın {name}, emekliliğiniz {-1*retiring} yıl önce başlamış.")
    else:
        print(f"Sayın {name}, emekliliğiniz için bir yıldan az süre kalmış")
retireCalculator(2001,"Hilmi")