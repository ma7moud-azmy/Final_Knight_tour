import random
def simulated_annealing_algorithm(x_coords, y_coords):
    #check valid knight moves
    def check_knight(position):
        move_list = []
        targets = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
        for i in range(8):
            target = (position[0] + targets[i][0], position[1] + targets[i][1])
            if 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
                move_list.append(target)
        return move_list

    #check if the move is in the history
    def check_valid_moves(moves, his):
        valid_options = []
        for i in moves:
            if i not in his:
                valid_options.append(i)
        return valid_options


    #making a population
    def generat_solutions(moves, sol_history):
        valid = []
        x = random.randint(0,len(moves)-1) #choosing a random next move
        next = moves[x]
        #checking for the next move moves 
        opt = check_knight(next)
        valid = check_valid_moves(opt, sol_history)
        sol_history.append(next)
        if len(valid) > 0:
            generat_solutions(valid, sol_history)
        return sol_history


    def candidate_check(position, moves):
        move_list = []
        targets = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
        for i in range(8):
            target = (position[0] + targets[i][0], position[1] + targets[i][1])
            if 0 <= target[0] <= 7 and 0 <= target[1] <= 7 and target not in moves:
                move_list.append(target)
        return move_list


    def candidate_move(moves, index):
        new_moves = moves
        opt = []
        if len(new_moves) == index:
            next = new_moves[len(new_moves)-1]
            opt = candidate_check(next, new_moves)
        while len(opt) > 0:
            x = random.randint(0,len(opt)-1)
            next = opt[x]
            new_moves.append(next)
            opt = candidate_check(next, new_moves)
        return new_moves



    def make_candidate(sol):
        his = []
        index = random.randint(30,len(sol))
        for i in range(index):
            his.append(sol[i])
        new = candidate_move(his, index)
        return new





    def simulated_annealing(initial):
        T = 100
        e = 2.718281828459045
        
        state = initial
        for i in range(20000):
            T -= 0.01
            if len(state) > 60:
                break
            candidate = make_candidate(state)
            print(len(candidate))
            print(candidate)
            E = len(candidate) - len(state)
            if E > 0:
                state = candidate
            else:
                prop = e ** (-E / T)
                if random.random() < prop:
                    state = candidate
        return state

    hist = [(x_coords,y_coords)]
    while len(hist) < 60:
        hist = [(x_coords,y_coords)]
        opt = check_knight((x_coords,y_coords))
        valid = check_valid_moves(opt, hist)
        hist = generat_solutions(valid, hist)

    sol = simulated_annealing(hist)
    sol.reverse()
    print(sol)
    print(len(sol))
    
    return sol