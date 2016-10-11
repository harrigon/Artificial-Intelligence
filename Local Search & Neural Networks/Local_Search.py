import random

def random_restart(n):
    random.seed(0) # seeding so that the results can be replicated.
    assignment = list(range(1, n+1))
    while not greedy_descent(tuple(assignment)):
        random.shuffle(assignment)


def conflict_count(total_assignment):
    count = 0
    for i in  range(len(total_assignment)):
        for j in  range(len(total_assignment)):
            if i != j:
                if abs((total_assignment[i] - total_assignment[j])/(j - i)) == 1:
                    count+= 1
    return count//2


# print(conflict_count((1, 2)))
# print(conflict_count((1, 3, 2)))
# print(conflict_count((1, 2, 3)))
# print(conflict_count((1,)))
# print(conflict_count((1, 2, 3, 4, 5, 6, 7, 8)))
# print(conflict_count((2, 3, 1, 4)))

def neighbours(assignment):
    neighbours = []
    for i in  range(len(assignment)):
        for j in  range(len(assignment)):
            if i != j:
                temp_list = list(assignment)
                temp_list[i], temp_list[j] = temp_list[j], temp_list[i]
                if tuple(temp_list) not in neighbours:
                    neighbours.append(tuple(temp_list))
    return neighbours

# print(neighbours((1, 2)))
# print(sorted(neighbours((1, 3, 2))))
# print(sorted(neighbours((1, 2, 3))))
# print(neighbours((1,)))
# for neighbour in sorted(neighbours((1, 2, 3, 4, 5, 6, 7, 8))):
#     print(neighbour)
# for neighbour in sorted(neighbours((2, 3, 1, 4))):
#     print(neighbour)

def greedy_descent(assignment):
    complete = False
    last_conflicts = -1
    while not complete:
        num_conflicts = conflict_count(assignment)
        if last_conflicts == num_conflicts:
            print("A local minimum is reached.")
            break
            complete = True
        print("Assignment:", assignment, "Number of conflicts:", num_conflicts)
        if num_conflicts == 0:
            print("A solution is found.")
            complete = True
        possible_assignments = sorted(neighbours(assignment))
        if len(assignment) != 1:
            assignment = min(possible_assignments, key = lambda x: conflict_count(x))
        last_conflicts = num_conflicts

# greedy_descent((1, 2, 3, 4, 5, 6))
# greedy_descent((6, 5, 3, 4, 2, 1))
# greedy_descent((2, 1, 3, 4, 6, 5))
# greedy_descent((1,))
# greedy_descent((1, 2))
# greedy_descent(tuple(range(1, 4)))
# greedy_descent(tuple(range(1, 6)))
# greedy_descent(tuple(range(1, 11)))


