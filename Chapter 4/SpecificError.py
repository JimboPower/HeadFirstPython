try:
    data = open('Edoardo.txt')
    print(data.readline(), end='')
except IOError as error:
    print("File error" + str(error))
finally:
    if 'data' in locals():
        data.close()
