import module

if __name__ == '__main__':
    print('main')
else:
    print(f'not main, its: {__name__}')

print(dir(module))
print(module.sum_3(10, 20, 30))