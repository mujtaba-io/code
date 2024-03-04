
# make a character matrix 4x4 (boggle board) with different characters and use DFS to find a word in the matrix. words will be pre-defined in a list. and we need to search for all 8 directions for each character in the matrix.

# In the boggle board, we can move to any of 8 adjacent characters, but a word should be constructed by a sequence of adjacent characters. We’ll use a dictionary to store the words and a matrix to store the characters.


board = [
    ['P', 'L', 'A', 'Y'],
    ['E', 'T', 'G', 'H'],
    ['S', 'A', 'Y', 'R'],
    ['R', 'N', 'O', 'P']
]

words = ['STAR', 'PLAY']

def dfs(board, i, j, word, visited):
    if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or visited[i][j]:
        return False
    if len(word) == 0:
        return True
    if board[i][j] == word[0]:
        visited[i][j] = True
        if dfs(board, i+1, j, word[1:], visited) or dfs(board, i-1, j, word[1:], visited) or dfs(board, i, j+1, word[1:], visited) or dfs(board, i, j-1, word[1:], visited) or dfs(board, i+1, j+1, word[1:], visited) or dfs(board, i-1, j-1, word[1:], visited) or dfs(board, i+1, j-1, word[1:], visited) or dfs(board, i-1, j+1, word[1:], visited):
            return True
        visited[i][j] = False
    return False


def find_word(board, word):
    visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == word[0]:
                if dfs(board, i, j, word, visited):
                    return True
    return False


for word in words:
    if find_word(board, word):
        print(word, 'is found')
    else:
        print(word, 'is not found')

