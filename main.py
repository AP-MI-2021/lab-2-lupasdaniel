def patrat_perfect(n):
    '''pp nr este patrat perfect
    :param: n
    :return: 1 sau 0'''
    for i in range(1, n//2+1):
        if n==i*i:
            return 1
    return 0


def test_patrat_perfect():
    assert patrat_perfect(4)==1
    assert patrat_perfect(3)==0
    assert patrat_perfect(16)==1
    assert patrat_perfect(21)==0

def get_perfect_squares(start,stop):
    '''adaugam in lista
    :param: start de unde incepem
    :return: list a doua lista'''
    list=[]
    for x in range(start,stop):
        if patrat_perfect(x)==1:
            list.append(x)
    return list


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
    test_patrat_perfect()
    while True:
        print('1. conjectura lui Goldbach')
        print('2. Calculul radicalului ')
        print('3. pb2')
        print('4.Exit')
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
            elem1 = int(input(" capatul inferior "))
            elem2 = int(input(" capatul superior "))
            print(get_perfect_squares(elem1, elem2))
        elif optiune == "4":
            break
        else:
            print('alege o alta optiune ')

main()