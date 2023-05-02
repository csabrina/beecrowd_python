A, B, C = map(int,input().split())

maiorAB = ((A + B) + abs(A - B)) / 2
maiorAC = ((A + C) + abs(A - C)) / 2

maior = ((maiorAB + maiorAC) + abs(maiorAB - maiorAC)) / 2

print("{:.0f} eh o maior" .format(maior))

"""if ( A > B and A > C):
    print("{} eh o maior" .format(A))
elif ( B > A and B > C):
    print("{} eh o maior" .format(B))
else:
    print("{} eh o maior" .format(C))
"""