def Min_Cost_Climbing_Stairs(cost:list[int]):
    cost.append(0)

    for i in range(len(cost)-3,-1,-1):
        cost[i] += min(cost[i+1],cost[i-+2])

    return min(cost[0],cost[1])

print(Min_Cost_Climbing_Stairs(cost = [10,15,20]))