
# progarm that calculates the Fibonacci value after user input 

print("This program that computes the nth Fibonacci number where the n is a value input by the user")
num = eval(input("how many numbers would you like to evalute? "))

def f(n,a = 0, b = 1):
    k = [a,b]
    while len(k) < n:
        k = k +([k[len(k)-1] + k[len(k)-2]])
    return k
 
b = sum(f(num + 1))
print(b)
         
