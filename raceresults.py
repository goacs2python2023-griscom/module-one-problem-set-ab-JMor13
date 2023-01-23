def results(my_time, time1, time2, time3):
    if my_time < time1 and my_time < time2 and my_time < time3:
        return "gold"
    elif (my_time < time1 and my_time < time2 and my_time > time3) or (my_time < time1 and my_time > time2 and my_time < time3) or (my_time > time1 and my_time < time2 and my_time < time3):
        return "silver"
    elif (my_time < time1 and my_time > time2 and my_time > time3) or (my_time > time1 and my_time < time2 and my_time > time3) or (my_time > time1 and my_time > time2 and my_time < time3):
        return "bronze"
    else:
        return "no medal"

print(results(0.2, 0.3, 1, 3))