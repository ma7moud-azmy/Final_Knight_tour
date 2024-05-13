def genetic_algorithm(x_coords, y_coords):
    import random

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
    def generat_solutions(moves):
        valid = []
        x = random.randint(0,len(moves)-1) #choosing a random next move
        next = moves[x]
        #checking for the next move moves 
        opt = check_knight(next)
        valid = check_valid_moves(opt, hist)
        hist.append(next)
        if len(valid) > 0:
            generat_solutions(valid)



    #asign values for the indvidual solution
    def fitness(sol):
        ans = len(sol)
        
        if ans == 64:
            return 100
        else:
            return ans


    #checks the move for generating a new mutation
    def mutate_check(position, moves):
        move_list = []
        targets = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
        for i in range(8):
            target = (position[0] + targets[i][0], position[1] + targets[i][1])
            if 0 <= target[0] <= 7 and 0 <= target[1] <= 7 and target not in moves:
                move_list.append(target)
        return move_list


    #moving for the mutation
    def mutate_move(moves, index):
        new_moves = moves
        opt = []
        if len(new_moves) == index:
            next = new_moves[len(new_moves)-1]
            opt = mutate_check(next, new_moves)
        while len(opt) > 0:
            x = random.randint(0,len(opt)-1)
            next = opt[x]
            new_moves.append(next)
            opt = mutate_check(next, new_moves)
        return new_moves


    #generating the mutation
    def mutate_soltion(sol):
        his = []
        mutate_index = (len(sol) // 2) + 8 
        for i in range(mutate_index):
            his.append(sol[i])
        new = mutate_move(his, mutate_index)
        return new



    x = x_coords
    y = y_coords

    #the initial state
    history = []
    history.append((x, y))
    options = check_knight((x, y))
    valid_moves = check_valid_moves(options,history)


    #creating the population
    population=[] #list that holds all the chromosoms of the population
    for i in range(1000):
        hist= [(x, y)]   #a list with the initial state to be the history of each on of the population 
        generat_solutions(valid_moves)
        population.append(hist)




        #making a generations
    for g in range(5000):
        #making a list of tuples of the best population fitness with the solution
        ranked_population = []
        #calculate the fitness
        for i in population:
            ranked_population.append((len(i), i))
        #ranking the population
        ranked_population.sort()
        ranked_population.reverse()
        
        print(f"=== Gen {g} best solution ===")
        print(ranked_population[0])
        
        if ranked_population[0][0] == 64:
            break
        
        #retreive the best 200 solutions 
        best_solutions = ranked_population[:200]
        
        
        #mutate the solutions 
        mutated = []
        for s in best_solutions:
            mutated.append(mutate_soltion(s[1]))
        
        #the new population is the mutated generation
        population = mutated



    final = ranked_population[0][1]
    final.reverse()
    return final
