def JHMC(A):
    if A == 0:
        return 1
    else:
        return A * JHMC(A - 1)
        
    

def main():
    Vidyoot = int(input("Enter Number for Factorial: "))
    print(JHMC(Vidyoot))
    
if __name__ == "__main__":
	main()