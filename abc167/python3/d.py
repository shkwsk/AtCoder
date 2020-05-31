# def main():
#     N,K = [int(x) for x in input().split()]
#     Al = [int(x) for x in input().split()]
#     current = 1
#     steps = 1
#     visit = [0]*N
#     initial_step = 0
#     while visit[current] > 0:
#         visit[current] = steps
#         current = Al[current-1]
#         steps += 1
#         print(current, steps)
#     initial_step = visit[current]
#     loop_step = steps
#     print(initial_step, loop_step)
#     # loop_step = len(steps) - steps.index(current)
#     # if len(steps) == initial_step:
#     #     initial_step = 0
#     # print(steps.index(current))
#     # print(initial_step)
#     # print(loop_step)
#     print((K-initial_step)%loop_step)
#     print(Al[(K-initial_step)%loop_step])

def main():
    N,K = [int(x) for x in input().split()]
    Al = [int(x) for x in input().split()]
    current = 1
    visit = [0]*N
    steps = []
    initial_step = 0
    while visit[current-1] == 0:
        visit[current-1] = 1
        steps.append(current)
        current = Al[current-1]
        initial_step += 1
        print(initial_step, current, steps)
    loop_step = len(steps) - steps.index(current)
    if loop_step == 0:
        print(1)
        return
    if loop_step == 1:
        print(steps[1])
        return
    if len(steps) == initial_step:
        initial_step = 0
    # print(steps.index(current))
    # print(initial_step)
    # print(loop_step)
    print(steps[(K-initial_step)%loop_step])

if __name__ == '__main__':
    main()
