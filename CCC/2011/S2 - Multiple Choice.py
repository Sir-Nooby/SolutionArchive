#Problem S2: Multiple Choice - 2011 (SirNooby)
questions = int(input())
student_answers = [input() for i in range(questions)]
solutions = [input() for i in range(questions)]

score = 0

for i in range(questions):
    if student_answers[i] == solutions[i]:
        score += 1

print(score)