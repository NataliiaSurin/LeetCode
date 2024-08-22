def max_area(height: list[int]) -> int:
    results = list(())
    for x in range(len(height)):
        for y in range(len(height)):
            if x != y:
                if height[x] > height[y]:
                    results.append((y - x) * height[y])
                else:
                    results.append((y - x) * height[x])
    return max(results)


print(max_area([1, 1, 5, 4, 7]))
