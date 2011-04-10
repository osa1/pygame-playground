
def dotProduct(v1, v2):
    r = []
    for i in range(len(v1)):
        r.append(v1[i] * v2[i])
    return r

v1 = [1, 2, 3]
v2 = [3, 4, 5]

print dotProduct(v1, v2)
raw_input()
