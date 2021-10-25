
class Maze:
    SIZE = (5, 9)
    BARRIER = [[1, 8], [2, 1], [2, 2], [2, 4], [2, 5], [3, 4], [3, 7], [3, 9], [4, 4], [4, 7], [4, 8], [4, 9], [5, 2]]
    
    def __init__(self, mazeSize=SIZE, barriers=BARRIER):
        #constructor
        self.mazeSize = mazeSize
        self.barriers = barriers
    
    def get_size(self):
        # return maze size
        return self.mazeSize
    
    def set_size(self, size):
        #set maze size
        #if no size is passed, size is set to default
        #returns true if size is passed, false if set to default
        valid = False
        if isinstance(size, tuple) and size[0] < size[1] and size[0] > 0:
            self.mazeSize = size
            valid = True
        else:
            self.mazeSize = Maze.SIZE
        return valid
    
    def get_barrier(self):
        #return barriers
        return self.barriers

    def set_barrier(self, barriers):
        #sets barriers
        #if no barriers are passed, barriers are set to default
        #returns true if barrier is passed, false if set to default
        valid = False
        if isinstance(barriers, list) and len(barriers) > 0:
            self.barriers = barriers
            valid = True
        else:
            self.barriers = Maze.BARRIER
        return valid

    def __str__(self):
        #print initialized size and barriers
        output = 'Maze Testing:\nsize = {0}\nbarriers = {1}'.format(Maze.get_size(self), Maze.get_barrier(self))
        return output

    def get_maze(self):
        #return maze with barriers
        size = Maze.get_size(self)
        barriers = Maze.get_barrier(self)
        row = size[0]
        col = size[1]
        maze = [[0 for i in range(col)] for j in range(row)]
        
        for i in barriers:
            maze[i[0]-1][i[1]-1] = 1
        
        return maze

    def move_up(node):
        #move up in maze
        copy_node = node.copy()
        copy_node[0] = copy_node[0] - 1
        return copy_node
    
    def move_down(node):
        #move down in maze
        copy_node = node.copy()
        copy_node[0] = copy_node[0] + 1
        return copy_node

    def move_left(node):
        #move left in maze
        copy_node = node.copy()
        copy_node[1] = copy_node[1] - 1
        return copy_node
    
    def move_right(node):
        #move right in maze
        copy_node = node.copy()
        copy_node[1] = copy_node[1] + 1
        return copy_node
    
    def collision(self, node):
        #check if move causes collision with barrier, returns True or False
        maze = Maze.get_maze(self)
        row = node[0]
        col = node[1]
        collision = False
        if maze[row][col] == 1:
            collision = True
        return collision
    
    def possible_moves(self, current_node, path, dead_end):
        #checks possible moves from the current position in the maze
        #current_node is the current position in maze
        #path is the list of moves taken from the start to the current position
        #dead_end is the list of moves taken that result in a dead end
        mazeSize = Maze.get_size(self)
        row = mazeSize[0]
        col = mazeSize[1]
        
        #all moves from current position
        move_right = Maze.move_right(current_node)
        move_left = Maze.move_left(current_node)
        move_up = Maze.move_up(current_node)
        move_down = Maze.move_down(current_node)
    
        #check if each move stays in the maze
        possible_moves = []
        if move_down[0] < row:
            possible_moves.append(move_down)
        if move_up[0] >= 0:
            possible_moves.append(move_up)
        if move_right[1] < col:
            possible_moves.append(move_right)
        if move_left[1] >= 0:
            possible_moves.append(move_left)
        
        #removes a move from the list of possible moves if:
        #1. the move causes a collision with a barrier
        #2. the move has already been taken and is in the current path
        #3. the move will result in a dead end
        final_moves = possible_moves.copy()
        for i in possible_moves:
            if Maze.collision(self, i) or path.count(i) > 0 or dead_end.count(i) > 0:
                final_moves.remove(i)
        
        #return a list of possible moves
        return final_moves

    def lowest_dist_to_goal(self, moves, goal):
        #check the lowest distance to the goal on an X, Y axis from a list of possible moves

        #create new list: distances. Append the distances of each move to the list
        distances = []
        for i in moves:
            row_diff = abs(goal[0] - i[0])
            col_diff = abs(goal[1] - i[1])
            dist = row_diff + col_diff
            distances.append(dist)
        
        #from the list of distances, find the shortest distance
        shortest = distances[0]
        for i in distances:
            if i < shortest:
                shortest = i
        
        #find the index of the shortest distance in the list of moves
        index = distances.index(shortest)
        lowest_dist_move = moves[index]

        #return the move with the shortest distance
        return lowest_dist_move
        

    def solve(self, start, goal):
        #find a path from start to goal within the maze
        start = [start[0]-1, start[1]-1]
        goal = [goal[0]-1, goal[1]-1]

        #current_node initialized as the start position
        current_node = start.copy()
        #initialize a path containing the start position
        path = []
        path.append(start)
        #intialize dead end as an empty list. This will eventually contain a list of moves that lead to a dead end
        dead_end = []

        #start a loop that iterates until our path is complete and contains the goal
        while path.count(goal) == 0:

            #find the moves from the current position
            moves_from_current = Maze.possible_moves(self, current_node, path, dead_end)

            #if there are no possible moves from the current position we are at a dead end
            if len(moves_from_current) == 0:
                #update the list of dead ends
                dead_end.append(current_node)
                #reset the path and current position at the start
                path = []
                current_node = start.copy()
                path.append(current_node)
                #reset the lowest distance move to the start position
                lowest = current_node
                #find the moves from the start position
                moves_from_current = Maze.possible_moves(self, current_node, path, dead_end)
            #find the lowest distance move to the goal from the list of possible moves
            else:
                lowest = Maze.lowest_dist_to_goal(self, moves_from_current, goal)
            #lowest is the next move. Add it to the path and set current position to lowest
            if path.count(lowest) == 0:
                path.append(lowest)
            current_node = lowest
        

        #return the path taken to get to the goal
        
        return path
        


                    
        
            
                    

    
  
