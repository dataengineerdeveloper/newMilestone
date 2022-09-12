# previous cell we a couple of variables and the goal is convert into a function


def calculatefoodTotal(food: float, tip_percentage:int)-> float:
    tip =  food * (tip_percentage / 100)
    total=  food + tip
    return total
    
calculatefoodTotal(100, 10)