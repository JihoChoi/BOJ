for _ in range(int(input())):
    items_dict = {}
    for _ in range(int(input())):
        item, category = input().split()

        if not category in items_dict:
            items_dict[category] = []

        items_dict[category].append(item)

    ans = 1
    for i in items_dict:
        ans *= len(items_dict[i]) + 1

    ans -= 1

    print(ans)