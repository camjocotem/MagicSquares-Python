from random import randint

MAX_SAFE_NUM = 605

def getRandomSquareNumbers(min,max):
    res = randint(min,max)
    return res * res

def calcMagicSquare():
    a = getRandomSquareNumbers(2, MAX_SAFE_NUM)
    b = getRandomSquareNumbers(2, MAX_SAFE_NUM)
    c = getRandomSquareNumbers(2, MAX_SAFE_NUM)
    d = getRandomSquareNumbers(2, MAX_SAFE_NUM)
    e = getRandomSquareNumbers(2, MAX_SAFE_NUM)
    f = getRandomSquareNumbers(2, MAX_SAFE_NUM)
    g = getRandomSquareNumbers(2, MAX_SAFE_NUM)
    h = getRandomSquareNumbers(2, MAX_SAFE_NUM)
    i = getRandomSquareNumbers(2, MAX_SAFE_NUM)
    
    rowA = a + b + c
    rowB = d + e + f
    rowC = g + h + i
    colA = a + d + g
    colB = b + e + h
    colC = c + f + i
    diagA = a + e + i
    diagB = g + e + c
    
    arr = [a,b,c,d,e,f,g,h,i]
    
    if (rowA == rowB & rowB == rowC & rowC == colA & colA == colB & colB == colC & colC == diagA & diagA == diagB & len(set(arr)) >= 7):
        print("Success with Squares", arr)
    

print("Starting calculations")
while( 1 == 1 ):
    calcMagicSquare()