#Problem J3: Harp Tuning - 2022 (SirNooby)
tuning = input()
point = 0

for i in range(len(tuning)):
    current_tuning = ""
    if tuning[i].isdigit():
        if (i + 1) >= len(tuning):
            current_tuning = tuning[point:i+1]
            if "+" in current_tuning:
                print(current_tuning[:current_tuning.find("+")] + " tighten " + current_tuning[current_tuning.find("+")+1:])
            else:
                print(current_tuning[:current_tuning.find("-")] + " loosen " + current_tuning[current_tuning.find("-")+1:])
        else:
            if not tuning[i+1].isdigit():
                current_tuning = tuning[point:i+1]
                point = i+1
                if "+" in current_tuning:
                    print(current_tuning[:current_tuning.find("+")] + " tighten " + current_tuning[current_tuning.find("+")+1:])
                else:
                    print(current_tuning[:current_tuning.find("-")] + " loosen " + current_tuning[current_tuning.find("-")+1:])

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                