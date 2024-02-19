import random

print("Let's play Rock - Paper - Scissors!")

# Веса:     1       2          3
moves = ["Rock", "Paper", "Scissors"]

users_move = int(input("Type 1 for Rock, 2 for Paper, or 3 for Scissors: "))
pc_move = random.randint(1, 3)

# Ничья
if users_move == pc_move:
    print(f"You: {moves[users_move - 1]}\nPC: {moves[pc_move - 1]}\nIt's a draw.")
# Исключения
elif users_move == 1 and pc_move == 3:
    print(f"You: {moves[users_move - 1]}\nPC: {moves[pc_move - 1]}\nYou win!")
elif users_move == 3 and pc_move == 1:
    print(f"You: {moves[users_move - 1]}\nPC: {moves[pc_move - 1]}\nPC wins!")
# Основное правило
elif users_move > pc_move:
    print(f"You: {moves[users_move - 1]}\nPC: {moves[pc_move - 1]}\nYou win!")
else:
    print(f"You: {moves[users_move - 1]}\nPC: {moves[pc_move - 1]}\nPC wins!")
