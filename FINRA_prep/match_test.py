day = 6


def what_day(day:int):

    match day:
        case 1:
            return "Monday"
        case 2:
            return "Tuesday"
        case 3:
            return "Wednesday"
        case 4|5:
            return "Thu | Friday"
        case _:
            return "Weekend!"


print(what_day(day=day))