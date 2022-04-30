def solution(src, dest):
    # Take a numbered sqaure and convert it to coordinates
    convert_to_coord = lambda number : [number // 8, number % 8]
    src = convert_to_coord(src)
    dest = convert_to_coord(dest)

    # Take the coordinates of a square and check if it's inside the puzzle
    is_inside = lambda x, y : (x >= 0 and x <= 7 and y >= 0 and y <= 7)

    # A class to model the sqaures of the puzzle
    class square:
        def __init__(self, x = 0, y = 0, moves = 0):
            self.x = x
            self.y = y
            self.moves = moves

    # Possible movements
    dxy = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]]

    # A queue to hold the sqaures that will be visited
    queue = []
     
    # Push starting position with 0 steps
    queue.append(square(src[0], src[1], 0))
     
    # Make all squares unvisited
    visited = [[False for i in range(8)]
                      for j in range(8)]
    
    # Visit starting sqaure
    visited[src[0]][src[1]] = True

    # Loop until there is one element in the queue
    while(len(queue) > 0):
         
        c = queue.pop(0)
         
        # If current sqaure is equal to destination sqaure return number of steps
        if(c.x == dest[0] and c.y == dest[1]):
            return c.moves
             
        # Else iterate for all reachable states
        for i in range(8):
             
            x = c.x + dxy[i][0]
            y = c.y + dxy[i][1]
             
            if(is_inside(x, y) and not visited[x][y]):
                visited[x][y] = True
                queue.append(square(x, y, c.moves + 1))

print(solution(19,36))