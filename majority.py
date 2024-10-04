def majority(x, y, z):
    return (x and y) or (y and z) or (x and z)

print(majority(False, False, False))