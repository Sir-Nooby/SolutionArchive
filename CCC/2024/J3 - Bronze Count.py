#Problem J3: Bronze Count - 2024 (SirNooby)
participants = int(input())

scores = []

for i in range(participants):
    scores.append(int(input()))

final_scores = sorted(list(set(scores)))

print(final_scores[-3], scores.count(final_scores[-3]))