# -*- coding: utf-8 -*-
#
'''
一个数独的解法需遵循如下规则：

数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
空白格用 '.' 表示。
'''
def find_key3(board,row,col):
    r=row//3*3
    c=col//3*3
    temp=board[r][c:c+3]+board[r+1][c:c+3]+board[r+2][c:c+3]
    key3={'1','2','3','4','5','6','7','8','9'}-set(temp)
    return key3
def find_empty(board):
    for r in range(9):
        for c in range(9):
            if board[r][c]=='.':
                return r,c
    else:
        return None,None
def solveSudoku(board):
    """
    :type board: List[List[str]]
    :rtype: void Do not return anything, modify board in-place instead.
    """
    #find position of the first '.'
    row,col=find_empty(board)
    if row==None:
        return board

    key1={'1','2','3','4','5','6','7','8','9'}-set(board[row])
    key2={'1','2','3','4','5','6','7','8','9'}-set([board[i][col] for i in range(9)])
    key3=find_key3(board,row,col)
    key=key1&key2&key3

    while key:
        k = key.pop()
        board[row][col]=k
        temp=solveSudoku(board)
        if temp:
            return temp
        else:
            board[row][col] = '.'
    else:
        return False

def isValidSudoku(board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """
    for i in board:
        r=[j for j in i if j!='.']
        row=set(i)-{'.'}
        if len(r)!=len(row):
            return False

    for i in range(9):
        temp=[board[j][i] for j in range(9)]
        col=[j for j in temp if j!='.']
        c=set(temp)-{'.'}
        if len(c)!=len(col):
            #print('col false:',i)
            return False
    for i in range(0,9,3):
        for j in range(0,9,3):
            temp = board[i][j:j + 3] + board[i + 1][j:j + 3] + board[i + 2][j:j + 3]
            unit = [i for i in temp if i!='.']
            u=set(temp)-{'.'}
            if len(unit)!=len(u):
                return False
    return True



def main():
    board=[["5","3",".",".","7",".",".",".","."],
           ["6",".",".","1","9","5",".",".","."],
           [".","9","8",".",".",".",".","6","."],
           ["8",".",".",".","6",".",".",".","3"],
           ["4",".",".","8",".","3",".",".","1"],
           ["7",".",".",".","2",".",".",".","6"],
           [".","6",".",".",".",".","2","8","."],
           [".",".",".","4","1","9",".",".","5"],
           [".",".",".",".","8",".",".","7","9"]]
    for i in board:
        print(i)
    if isValidSudoku(board):
        print('This is a valid sudoku! \nThe sudoku solution is as follow:\n')
        key = solveSudoku(board)
        for i in key:
            print(i)
    else:
        print('This is an invalid sudoku!')

if __name__ == '__main__':
    main()