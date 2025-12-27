import copy

items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

def greedy_algorithm(money, items):
    copy_items = copy.deepcopy(items)
    
    for item, value in items.items():
        copy_items[item]["ratio"] = round(value['cost'] / value['calories'], 3)

    sorted_by_ratio = sorted(copy_items.items(), key=lambda x: x[1]['ratio'])

    max_calories = list()

    for k, v in sorted_by_ratio:
        if v['cost'] <= money:
            max_calories.append(k)
            money -= v['cost']


    return f"{max_calories}, the rest of the money: {money}"

money = 150

print(greedy_algorithm(money, items))