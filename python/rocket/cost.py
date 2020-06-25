import dynamics

def costAnyPointInsertion(control):
    cost = 0
    [t,X] = getStateTrajectory(x0,control)
    for i in range(len(control)):
        cost += 1 

def costFixedPointInsertion(control):
    cost = 0 
    for i in range(len(control)):
        cost += 1

def getStateTrajectory(x0,control):
    pass