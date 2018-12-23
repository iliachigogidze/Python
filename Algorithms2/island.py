'''
14. shemodis matrica sadac X nishnavs xmelets da O nishnavs zgvas. unda ipovo kundzulebis raodenoba
'''

board = [
    ['O','O','O','O','O','O','O','O','O','X'],
    ['O','X','X','X','X','X','X','O','O','O'],
    ['X','X','O','O','O','O','X','O','X','O'],
    ['X','X','O','X','X','O','X','O','O','O'],
    ['X','X','O','O','O','O','X','O','O','O'],
    ['O','X','X','X','X','X','X','O','O','O'],
    ['O','O','O','O','O','O','O','O','X','X'],
    ['O','O','X','O','O','O','O','O','X','X'],
    ['O','X','O','O','O','O','O','X','O','O'],
    ['O','O','O','X','O','O','X','O','O','O']
    ]

def print_board():
    string_board = ''

    for i in range(len(board)):
        for j in range(len(board[0])):
            string_board += board[i][j] + ' '
        string_board += '\n'

    return string_board




def main():
    print(print_board())


main()