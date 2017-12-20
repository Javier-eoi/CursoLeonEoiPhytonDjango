def print_everthing(*args):
    for n in args:
        print(n)

print_everthing('manzana', 'platano', 'pera')

def print_all_whit_positions(*args):
    for count, thing in enumerate(args):
        print('{}. {}'.format(count,thing))
        #print(count,thing)

print_all_whit_positions('manzana', 'platano', 'pera')

counter = 0
while True: #counter < 7:
    counter += 1
    print(counter)
    if counter > 25:
        break

    print('zas')
print('fin del counter')

def count_until(n=3):
    count = 0
    while count <= n:
        print(count)
        count +=1
    #pass # pasar codigo que no queremos que haga nada

count_until(3)
count_until(10)

def show_keyword_argument(**kwards):
    for name, value in kwards.items():
        print('{}. {}'.format(name,value))

show_keyword_argument(uno=1, dos=2, nombre='Carlos')
