n = int(input("Enter Number: "))

if n <= 1:
    print("Not Prime")
else:
    is_prime = True
    limit = int(n ** 0.5)

    for d in range(2, limit + 1):
        if n % d == 0:
            is_prime = False
            break

    if is_prime:
        print("Prime")
    else:
        print("Not Prime")
