import numpy as np
def backtracking_algorithm(x_coords,y_coords):
    def validateMove(bo, row, col):
        if row < 8 and row >= 0 and col < 8 and col >= 0 and bo[row, col] == 0:
            return True

    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]


    def solve (bo, row, col, n, counter):
        global solution
        solution=[]
        for i in range(8):
            if counter >= 65:
                return True
            new_x = row + move_x[i]
            new_y = col + move_y[i]
            if validateMove(bo, new_x, new_y):
                bo[new_x,new_y] = counter
                if solve(bo,new_x, new_y, n, counter+1):
                    solution.append((new_x,new_y))
                    return True
                bo[new_x,new_y] = 0
        return False

    br = np.zeros((8, 8))
    br[x_coords, y_coords] = 1
    solve(br,x_coords,y_coords,8,2)

    print(solution)
    
    return solution