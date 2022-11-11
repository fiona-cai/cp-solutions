#https://dmoj.ca/problem/ccc10j5
#CCC '10 J5 - Knight Hop

def minStepstoEnd(start_pos, end_pos):
    queue = [start_pos]
    minSteps = {
        start_pos : 0
    }

    nextp = [
        (1, 2),
        (2, 1),
        (2, -1),
        (1, -2),
        (-1, -2),
        (-2, -1),
        (-2, 1),
        (-1, 2),
    ]

    while queue != []:
        current_pos = queue.pop(0)
        steps = minSteps[current_pos]

        if current_pos == end_pos:
            return steps

        for nextpos in nextp:
            if 1 <= current_pos[0] + nextpos[0] <=8 and 1 <= current_pos[1] + nextpos[1] <= 8:

                nextPosition = (current_pos[0] + nextpos[0], current_pos[1] + nextpos[1])
            

                if nextPosition not in minSteps:
                    minSteps[nextPosition] = steps + 1
                    queue.append(nextPosition)



start_x, start_y = (int(x) for x in input().split())
end_x, end_y = (int(x) for x in input().split())
print(minStepstoEnd((start_x, start_y), (end_x, end_y)))