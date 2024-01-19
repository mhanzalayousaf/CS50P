c = 300000000

def main():
    m = int(input("What's value of m?"))
    e = energy(m)
    print(int(e))

def energy(m):
    e = m * c**2 #or e = m * c*c
    return e

main()
    