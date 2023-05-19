l = [int(input()) for i in range(3)]
d1, d2, d3 = l[0], l[1], l[2]
print(min((d1 + d3 + d2),(d2 * 2 + d1 * 2), (d1 * 2 + d3 * 2), (d2 * 2 + d3 * 2)))

