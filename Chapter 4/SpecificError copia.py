try:
    with open("missing.txt", "w") as data:
        print("Il mio nome e' James, James Bond", file=data)
except IOError as error:
    print("File error!" + str(error))


