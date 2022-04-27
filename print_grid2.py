#generate grid with same +/- pattern but takes 2 parameters to control size of grid and number of grid cells
PLUS = '+'
MINUS = '-'
BAR = '|'
SPACE = ' '


def get_grid_size():
    s = input("Please enter the size/width of each cell to print: ")
    return s


def get_num_cells():
    n = input("Please enter the number of cells you want in your grid: ")
    return n


def print_row(grid_size, number_of_cells):
    while number_of_cells > 0:
        print((PLUS + SPACE), end="")
        print((MINUS + SPACE) * grid_size, end="")
        number_of_cells -= 1
    print(PLUS)
    return 0


def print_column(grid_size, number_of_cells):
    while number_of_cells > 0:
        print(BAR, end="")
        print(SPACE * (grid_size * 2 + 1), end="")
        number_of_cells -= 1
    print(BAR)
    return 0


def print_grid(grid_size, number_of_cells):
    num = number_of_cells
    while num >= 0:
        print_row(grid_size, number_of_cells)
        i = grid_size
        while i > 0:
            print_column(grid_size, number_of_cells)
            i = i - 1
        num = num - 1
    print_row(grid_size, number_of_cells)
    return 0



#main
size = int(get_grid_size())
num_cells = int(get_num_cells())

#print_row(size, num_cells)
#print_column(size, num_cells)
print_grid(size, num_cells)
print()
