

# available seat
available_seat = '.'
occupied_seat = 'X'
empty_covid = 'e'

seating = []
n_row = 20
n_col = 26


def alpha():

    abc_list = []

    start = ord('a')
    end = ord('z')

    print()
    print('    ', end='\t')

    for i in range(start, end+1):

        ch = chr(i)
        abc_list.append(ch)
        print(ch, end=' ')

    print()
    print('        '+('-')*51)

    return abc_list

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
            print(seating[r][c], end=' ')
        print()


# reservation seats


def buy_ticket():

    row = int(input('Que fila es bro?'))

    col_letter = input('Which Column?').lower()

    col = alpha().index(col_letter)

    (seating[row-1][col]) = occupied_seat

    alpha()
    print_seating()


create_seating()
alpha()
print_seating()
buy_ticket()
