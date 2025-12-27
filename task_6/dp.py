def dynamic_programming(money, items):
    dish = []
    cost = []
    calories = []

    for k, v in items.items():
        dish.append(k)
        cost.append(v['cost'])
        calories.append(v['calories'])

    len_dish = len(dish)

    K = [[0 for w in range(money + 1)] for i in range(len_dish + 1)]

    for i in range(1,len_dish + 1):
        for w in range(money + 1):
            if cost[i - 1] > w:
                K[i][w] = K[i - 1][w]
            else:
                K[i][w] = max(K[i - 1][w], K[i - 1][w - cost[i - 1]] + calories[i - 1])

    selected = []
    m = money
    l = len_dish

    while l > 0 and m >= 0:
        if K[l][m] != K[l-1][m]:
            selected.append(dish[l-1])
            m -= cost[l-1]
        l -= 1
    selected = list(reversed(selected))

    return f"Calories: {K[len_dish][money]}, Dish: {selected}, the rest of the money: {m}"

items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

money = 50

print(dynamic_programming(money, items))
