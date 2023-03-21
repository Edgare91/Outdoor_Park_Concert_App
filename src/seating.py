

# available seat
available_seat = '.'
occupied_seat = 'X'
empty_covid = 'e'


seating = []
n_row = 20
n_col = 26


def alpha():

    start = ord('a')
    end = ord('z')
    print()
    print('    ', end='\t')
    for i in range(start, end+1):
        ch = chr(i)
        print(ch, end=' ')

    print()
    print('        '+('-')*51)


# create some available seating
def create_seating():

    for r in range(n_row):
        row = []
        for c in range(n_col):
            row.append(available_seat)
        seating.append(row)

    return seating


# print available seating
def print_seating():

    for r in range(n_row):

        print(r+1, end="\t")
        for c in range(n_col):
            seats_data = seating[r][c]
            print(seats_data, end=" ")
        print()


# reservation seats
def buy_ticket(fila, colum):

    fila = int(input('Que fila es bro?'))
    colum = int(input('Que columa es bro?'))
    (seating[fila-1][colum-1]) = occupied_seat

    print_seating()


create_seating()
alpha()
print_seating()
buy_ticket(int, int)
