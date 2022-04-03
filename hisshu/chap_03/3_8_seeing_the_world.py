locations = ["barcelona", "machu picchu", "uyuni", "guiana shield", "ulruru"]
print("元の順番")
print(locations)

print("\nsorted()を使用してアルファベット順")
print(sorted(locations))
print("元の順番")
print(locations)

print("\nsorted()を使用してアルファベットの逆順")
print(sorted(locations, reverse=True))
print("元の順番")
print(locations)

print("\nreverse()を使用して逆順")
locations.reverse()
print(locations)
print("reverse()を使用して元の順番に修正")
locations.reverse()
print(locations)

print("\nsort()を使用してアルファベット順に変更")
locations.sort()
print(locations)
print("\nsort()を使用してアルファベットの逆順に変更")
locations.sort(reverse=True)
print(locations)
