try:
    f = open('input.txt', 'r')
    r = f.readlines()
    f.close()
except FileNotFoundError:
    print('File Not Found')