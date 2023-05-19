#Напишите программу, которая вычисляет минимальное расстояние, которое потребуется пройти Тимуру, чтобы посетить оба магазина и вернуться домой. Тимур всегда стартует из дома. Он должен посетить оба магазина, перемещаясь только по имеющимся трём дорожкам, и вернуться назад домой. При этом его совершенно не смутит, если ему придётся посетить один и тот же магазин или пройти по одной и той же дорожке более одного раза. Единственная его задача — минимизировать суммарное пройденное расстояние.
l = [int(input()) for i in range(3)]
d1, d2, d3 = l[0], l[1], l[2]
print(min((d1 + d3 + d2),(d2 * 2 + d1 * 2), (d1 * 2 + d3 * 2), (d2 * 2 + d3 * 2)))

