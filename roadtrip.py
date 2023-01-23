def roadtrip(distance, mpg, price):
    if distance % mpg == 0:
        return (distance/mpg) * price
    else:
        return ((distance//mpg)+1)*price

print(roadtrip(400, 30, 1.5))