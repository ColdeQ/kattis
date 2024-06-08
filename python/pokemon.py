import sys


numberOfPokemon, amount = sys.stdin.readline().strip().split()
pokemonArray = []
def sortAtk(x):
    return x[1]

def sortDef(x):
    return x[2]

def sortHp(x):
    return x[3]

def sorts(x):
    return x[0]

for i in range(int(numberOfPokemon)):
    atk,deff,hp = sys.stdin.readline().strip().split()
    pokemonArray.append((i, int(atk),int(deff),int(hp)))


fullArray = []

#   [:int(amount)]

atkArray = sorted(pokemonArray,key=sortAtk,reverse=True)[:int(amount)]
defArray = sorted(pokemonArray,key=sortDef,reverse=True)[:int(amount)]
hpArray = sorted(pokemonArray,key=sortHp,reverse=True)[:int(amount)]

fullArray = atkArray + defArray + hpArray

fullArray.sort(key=sorts)

unique = 0

for i in range(len(fullArray) - 1):
    if(fullArray[i][0] != fullArray[i+1][0]):
        unique+=1

if(fullArray[-1][0] != fullArray[i+1][-2]):
    unique+=1

print(unique)