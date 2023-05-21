# Зачастую переводить сериалы, не теряя изначальный смысл, невозможно, особенно за счет игр слов. Сумасшедший режиссер хочет снять сериал, в котором бы в целях эксперимента задействовал как можно больше языков, чтобы пользоваться красотой каждого из них. Тем не менее если задействовать слишком много языков, то сериал станет непонятен абсолютно всем, поэтому режиссер достает случайных людей на улице и спрашивает их, какие языки они знают, таким образом он будет использовать языки которые знают все из них.

# Напишите программу, которая определяет, какие языки будут использоваться в сериале.
n = int(input())
l = [input().split(", ") for i in range(n)]
res = []
for i in l:
    for j in i:
        res.append(j)
res = {i: res.count(i) for i in res if res.count(i) == n}
#res = [i for i in res if res.count(i) == n]
if res == {}:
    print("Сериал снять не удастся")
reso = []
for i in sorted(res.keys()):
    reso.append(i)
print(*sorted(reso), sep = ", ")