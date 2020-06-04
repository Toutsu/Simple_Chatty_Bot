min_sleep = abs(int(input()))
max_sleep = abs(int(input()))
sleep = abs(int(input()))
if sleep <= max_sleep:
    if sleep < min_sleep:
        print("Deficiency")
    else:
        print("Normal")
else:
    print("Excess")
