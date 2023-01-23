def num_buses(num_people):
    if num_people % 52 == 0:
        return num_people / 52
    else:
        return (num_people // 52) + 1


print(num_buses(52))