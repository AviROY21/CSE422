import random

def minimax(node, depth, isMaximizingPlayer, alpha, beta, max_neg_hp):
    if depth == 0:
        return node
    if isMaximizingPlayer:
        bestval = -float('inf')
        for child in range(max_neg_hp + 1):
            value = minimax(child, depth-1, False, alpha, beta, max_neg_hp)
            bestval = max(bestval, value)
            alpha = max(alpha, bestval)
            if beta <= alpha:
                break
        return bestval
    else:
        bestval = float('inf')
        for child in range(max_neg_hp + 1):
            value = minimax(child, depth-1, True, alpha, beta, max_neg_hp)
            bestval = min(bestval, value)
            beta = min(beta, bestval)
            if beta <= alpha:
                break
        return bestval

id = input("Enter your Student Id: ")
num_turns = int(id[0])
max_neg_hp = int(id[1:3][::-1])
initial_hp = int(id[3])
num_bullets = int(id[4])

min_neg_hp, max_neg_hp = map(int, input("Minimum and Maximum value for the range negative HP: ").split())

attacker_hp = num_bullets * min_neg_hp
defender_hp = initial_hp

depth = 1
num_branches = 0

for i in range(num_turns):
    best_choice = -float('inf')
    alpha = -float('inf')
    beta = float('inf')
    for j in range(max_neg_hp + 1):
        value = minimax(j, depth, False, alpha, beta, max_neg_hp)
        num_branches += 1
        if value > best_choice:
            best_choice = value

    defender_hp -= best_choice
    attacker_hp -= best_choice
    if defender_hp <= 0:
        break
    depth += 1

print(f"Depth and Branches ratios is {depth-1} : {num_branches//(max_neg_hp**depth)}")
print(f"Terminal States (Leaf Nodes) are {','.join([str(random.randint(min_neg_hp,max_neg_hp)) for i in range(max_neg_hp ** (depth-1))])}.")
print(f"Left life (HP) of the defender after maximum damage caused by the attacker is {defender_hp}.")
print(f"After Alpha-beta pruning Leaf Node Comparisons {num_branches}.")