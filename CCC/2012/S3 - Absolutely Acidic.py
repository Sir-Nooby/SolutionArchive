#Problem S3: Absolutely Acidic - 2012 (SirNooby)
sensors = int(input())

levels = [int(input()) for i in range(sensors)]

counts = {}

for i in levels:
    counts[i] = counts.get(i, 0) + 1

highest_frequency = max(counts.values())

max_readings = [i for i, count in counts.items() if count == highest_frequency]

if len(max_readings) >= 2:
    best = abs(max(max_readings) - min(max_readings))
else:
    first = max_readings[0]

    next_maximum_frequency = max(i for i in counts.values() if i < highest_frequency)
    second_max_readings = [i for i, count in counts.items() if count == next_maximum_frequency]

    for i in second_max_readings:
        best = max(abs(first - i))

print(best)