def sumar(n1,n2):
    return n1+n2

def test_sumar_positivos():
    assert sumar(2,3)==5

def  test_sumar_negativos():
    assert sumar(-1,-1)==-2

def test_sumar_cero():
    assert sumar(5,0)==5
