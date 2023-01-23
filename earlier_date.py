def earlier_date(d1, m1, y1, d2, m2, y2):
    if y2 > y1:
        return "before"
    elif y2 < y1:
        return "after"
    elif y2 == y1:
        if m2 > m1:
            return "before"
        elif m2 < m1:
            return "after"
        elif m2 == m1:
            if d2 > d1:
                return "before"
            elif d2 < d1:
                return "after"
            elif d2 == d1:
                return "same"

print(earlier_date(7,8,9,4,5,6))