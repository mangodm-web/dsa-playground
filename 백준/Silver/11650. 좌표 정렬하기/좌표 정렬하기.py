N = int(input())
coordinates = []

for i in range(N):
    x, y = input().split(" ")
    coordinates.append((int(x), int(y)))
    
coordinates.sort()

for coordinate in coordinates:
    x, y = coordinate
    print(x, y)
