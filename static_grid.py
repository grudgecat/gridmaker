#This is a program to print a grid using +- characters
plus = '+ '
minus = '- '
bar = '| '
space = ' '

def print_row(n):
    while n > 0:
        print(plus, end="")
        print(minus * 4, end="")
        n -= 1
    print(plus)


def print_column(n):
    while n > 0:
        print(bar, end="")
        print(space * 8, end="")
        n -= 1
    print(bar)


i = 0
while i < 2:
    print_row(2)
    num_cols = 4
    while num_cols > 0:
        print_column(2)
        num_cols -= 1
    i += 1
print_row(2)
print()



