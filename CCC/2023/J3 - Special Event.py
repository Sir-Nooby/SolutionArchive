#Problem J3: Special Event - 2023 (SirNooby)
days = int(input())

attendance = []
replies = []

day_counter = ""

for i in range(days):
    attendance.append(input())

for i in range(5):
    counter = 0
    for v in attendance:
        if v[i] == "Y":
            counter += 1
    replies.append(counter)

for i in range(len(replies)):
    if replies[i] == max(replies):
        current = i+1
        day_counter += str(current)

print(",".join(day_counter))