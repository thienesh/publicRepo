while True:
    num = input("Enter the number::")
    try:
        if num == "exit":
            print("Program exited")
            break
        else:
            try:
                n = int(num)
                if n > 1:
                    for i in range(2, n):
                        if n % i == 0:
                            print("Not prime number")
                            break
                    else:
                        print("Prime number")
                else:
                    print("Not a prime number")
            except Exception as e:
                print(e)
    except Exception as f:
        print(f)
