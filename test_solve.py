from solve import Maze

def testing():
    s = Maze()
    
    print(s)
    print()
    start = [1, 9]
    goal = [5, 1]
    path = s.solve(start, goal)
    maze = s.get_maze()
    print('Printing Maze:')
    for i in maze:
        print(*i, sep=' ')
    print()
    print('Start: {0}, Goal: {1}'.format(start, goal))
    print()
    print('Printing path to goal:')
    final_path = []
    for i in path:
        final_path.append([i[0]+1, i[1]+1])
    print(final_path)
    print()

testing()

