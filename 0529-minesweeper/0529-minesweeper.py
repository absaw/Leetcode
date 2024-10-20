from collections import deque
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        
        m = len(board)
        n = len(board[0])

        queue = deque()
        game_over = False
        queue.append((click[0],click[1]))
        neighbors = [[0,1],
                    [0,-1],
                    [1,0],
                    [-1,0],
                    [1,1],
                    [-1,-1],
                    [1,-1],
                    [-1,1]]
        visited = set()
        while queue and not game_over:

            r,c = queue.popleft()

            if board[r][c] == 'M':
                board[r][c] = 'X'
                game_over=True
                break
            elif board[r][c] == 'E':
                #iterate through neighbors to check for mines
                neighbor_list=deque()
                mines = 0
                for add_r, add_c in neighbors:
                    new_r = r + add_r
                    new_c = c + add_c
                    if (new_r in range(m) and
                        new_c in range(n) and 
                        (new_r,new_c) not in visited):
                        neighbor_list.append((new_r,new_c))
                        if board[new_r][new_c]=='M':
                            mines += 1
                        
                if mines:
                    board[r][c] = str(mines)
                else:
                    board[r][c] = 'B'
                    while neighbor_list:
                        queue.append(neighbor_list.popleft())
                visited.add((r,c))
        # print(board)
        return board
                        # check if mine is present
                        
                # if no mines, add neighbors to queue
                # if found mines, reveal count 