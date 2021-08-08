# Bucles while


def run():
    LIMIT = 1000000
    counter = 0
    potency = 2*counter
    while potency < LIMIT:
        print("2 elevado a " + str(counter) + "es igual a: " + str(potency))
        counter = counter + 1
        potency = 2*counter


if __name__ == "__main__":
    run()
