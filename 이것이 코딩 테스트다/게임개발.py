import sys; sysinput = sys.stdin.readline

def main():
    world, x, y ,direction = get_inputs()
    solution(world, x, y, direction)

def get_inputs():
    n, m = map(int, sysinput().split())
    x, y, direction = map(int, sysinput().split())

    world = []
    for _ in range(n):
        world.append(list(map(int, sysinput().split())))
    world[y][x] = 2

    return world, x, y, direction

def solution(world, x, y, direction):
    answer = 1

    while True:
        num_turn = 0

        while num_turn <= 4:
            direction = turn(direction)
            num_turn += 1
            nx, ny = peek(x, y, direction)
            if can_go(world, nx, ny):
                x, y = nx, ny
                world[y][x] = 2
                answer += 1
                num_turn = 0
        
        nx, ny = peek(x, y, flip_direction(direction))
        if is_sea(world, nx, ny):
            break

        x, y = nx, ny

    print(answer)

def turn(direction):
    return (direction+3)%4

def peek(x, y, direction):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    return x+dx[direction], y+dy[direction]

def can_go(world, x, y):
    return world[y][x] == 0

def is_sea(world, x, y):
    return world[y][x] == 1

def flip_direction(direction):
    return (direction+2)%4

main()
