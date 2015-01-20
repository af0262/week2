import math
 
def main():

    n = eval(input('Enter a number: '))
                     
    if n == 1: print('1 is not A Prime number.')
    elif n == 2: print('2 is Prime number.')
         
    else:
             
                b = math.sqrt(n)    
                c = 2
             
    while c <= b and n%c != 0:
                        c = c+1
             
    if n%c == 0: print(n,'is not a Prime number.')
    else: print(n,'is A Prime number.')       
main()
