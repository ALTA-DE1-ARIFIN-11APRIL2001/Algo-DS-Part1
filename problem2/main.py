def adalah_prima(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def primeX(x):
    daftar_prima = []
    num = 2
    while len(daftar_prima) < x:
        if adalah_prima(num):
            daftar_prima.append(num)
        num += 1
    return daftar_prima[-1]
    
if __name__ == "__main__":
    print(primeX(1))  # 2
    print(primeX(5))  # 11
    print(primeX(8))  # 19
    print(primeX(9))  # 23
    print(primeX(10)) # 29