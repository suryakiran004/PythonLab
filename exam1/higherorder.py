from functools import reduce


number = ['1','2','3','4']

mapp =  list(map(int ,number ))
print(mapp)

fil = list(filter(lambda x : x % 2 != 0,mapp))
print(fil)

red = reduce(lambda x , y : x+y , mapp)
print(red)