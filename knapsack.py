def knapsack(values, weight, knap_weight):
    table = [[0 for x in range(knap_weight + 1)] for y in range(len(values) + 1)]
    
    for i in range(1,len(values) + 1):
        for j in range(1,knap_weight + 1):
            if j >= weight[i - 1]:
                table[i][j] = max(table[i - 1][j], values[i - 1] + table[i - 1][j - weight[i - 1]])
            else:
                table[i][j] = table[i - 1][j]
    print(table[len(values)][knap_weight])
    
knapsack([3,5,8,4,10], [2,4,5,3,9], 20)