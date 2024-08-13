
q = [1150,2000, 1212, 2396, 2800, 544, 1618, 346, 1523, 3965, 3681]
q = sorted(q)
direction = 0 # 0 == left 1 == right

totalCylinderMovement = 0
print(q)

# starting at current position, move towards direction
startingIndex = q.index(1150)



'From the starting index move to direction and add all distances to tCM'

for i in range(startingIndex, 0, -1):
    totalCylinderMovement += abs(q[i] - q[i-1])
    

'Second half move from 0 to index after startingIndex'

startingIndex += 1

totalCylinderMovement += q[startingIndex] # Account for movement from 0 to right index
print(totalCylinderMovement)

for i in range(startingIndex, len(q)-1, 1):
    print(abs(q[i+1] - q[i]))
    totalCylinderMovement += abs(q[i+1] - q[i])
    


print(totalCylinderMovement)

