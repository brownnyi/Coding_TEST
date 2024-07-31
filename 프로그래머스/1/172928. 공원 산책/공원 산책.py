def solution(park, routes):
    
    def find_location(park):
        for i in range(len(park)):
            for j in range(len(park[0])):
                if park[i][j] == 'S':
                    return [i, j]

    dir = {'E': [0, 1],
           'W': [0, -1],
           'S': [1, 0],
           'N': [-1, 0]}

    y, x = find_location(park)
    my, mx = y, x
    for route in routes:
        for _ in range(int(route[2])):
            my = my + dir[route[0]][0]
            mx = mx + dir[route[0]][1]
            if not(0 <= my <= len(park) - 1) or not(0 <= mx <= len(park[0]) - 1) or park[my][mx] == 'X':
                my, mx = y, x
                break
        y, x = my, mx

    return [y, x]