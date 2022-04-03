# 立方数
print("\n立方数")
cubes = [number**3 for number in range(1, 11)]
num = 0
for cube in cubes:
    num += 1
    print(f"{num}^3 = {cube}")
