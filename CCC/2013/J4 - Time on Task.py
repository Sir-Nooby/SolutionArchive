#Problem J4: Time on Task - 2013 (SirNooby)
minutes, chores = int(input()), int(input())
chore_times = []
total_time, total_checks = 0, 0

for i in range(chores):
    chore_times.append(int(input()))

chore_times.sort()

for chore in chore_times:
    if total_time + chore <= minutes:
        total_time += chore
        total_checks += 1
    else:
        print(total_checks)
        break