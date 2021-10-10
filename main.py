def is_prime(n):
    '''
    verifica danumarul dat este prim
    Input:
    -n:int
    Output:
   val de adevar
    '''
    if n < 2:
        return False
    for i in range(2,n//2+1):
        if n % i == 0:
            return False
    return True

def get_goldbach(n):
    '''
  numerele prime p1,p2 pentru care n=p1+p2 iar daca nu  val lui p1 respectiv p2 este 0

    Input:
    -n:int
    output:
    p1,p2

    '''
    for i in range(2,n):
        p1=i
        p2=n-i
        if is_prime(p1) & is_prime(p2):
            return p1, p2
    return 0, 0
def test_goldbach():
    assert get_goldbach(4) != 0, 0
    assert get_goldbach(10) != 0, 0
    assert get_goldbach(6) != 0, 0
def get_newton_sqrt(n,steps):
    '''
   radicalul cu algoritmul lui Newton

    input:
    -n ,steps:int
    output:
    -x1:float

    '''
    i = 1
    x0 = 2
    while i <= steps:
        x1 = x0-(pow(x0, 2)-n)/(2*x0)
        x0 = x1
        i+=1
    return x1

def test_get_newton_sqrt():
    assert get_newton_sqrt(16, 2) == 4.1
    assert get_newton_sqrt(36, 1) == 10.0


def main():
    test_get_newton_sqrt()
    test_goldbach()
    while True:
        print('1. conjectura lui Goldbach')
        print('2. Calculul radicalului ')
        print('3. exit')
        optiune = (input('Alegeti optiunea  :'))
        if optiune == '1':
            nr = int(input('introduceti un nr par >=4 '))
            g, d = get_goldbach(nr)
            if g == 0 & d == 0:
                print("Nu exista")
            else:
                print(f'{nr}={g}+{d}')
        elif optiune=='2':
            nr1=int(input('Dati un numar: '))
            steps=int(input(' numarul de pasi: '))
            print(get_newton_sqrt(nr1, steps))
        elif optiune == '3':
            break
        else:
            print('alege o alta optiune ')

main()