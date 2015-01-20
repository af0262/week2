
def main():

  bg = eval(input("Please enter a number to start the Syracuse Sequence: "))
  x = bg
  pat = []
  while x != 1:
    if x%2 == 0:
      x = x / 2
    else:
      x = 3 * x + 1
    pat.append(x)

  print("The Sequence starting with", bg, "is", pat)

main()
