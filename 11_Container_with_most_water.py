def max_area(height: list[int]) -> int:
    results = [0]
    x = len(height)-1
    y = 0
    while height[x] > height[y] and y < x:
        results.append((x - y) * height[y])
        results = [max(results)]
        y += 1
    else:
        results.append((x - y) * height[x])
        results = [max(results)]
    height_max = height[x]
    x -= 1
    while x > 0:
        if height[x] < height_max:
            x -= 1
            continue
        else:
            print(height[x])
            while height[x] > height[y] and y < x:
                results.append((x - y) * height[y])
                results = [max(results)]
                y += 1
            else:
                results.append((x - y) * height[x])
                results = [max(results)]
            height_max = height[x]
            x -= 1
    return max(results)


print(max_area([1,8,6,2,5,4,8,3,7]))
