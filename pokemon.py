import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('./Pokemon.csv')
shp = df.shape
sz = df.size
types = df.dtypes
print(shp, types, sz)

fire_pokemons = df.query('`Type 1` == "Fire" | `Type 2` == "Fire"')
fire_count = fire_pokemons.shape[0]
#print(fire_count)
#pd.set_option('display.max_columns', 20)
#print(fire_pokemons)

grass_pokemons = df.query('`Type 1` == "Grass" | `Type 2` == "Grass"')
grass_count = grass_pokemons.shape[0]

water_pokemons = df.query('`Type 1` == "Water" | `Type 2` == "Water"')
water_count = water_pokemons.shape[0]

flying_pokemons = df.query('`Type 1` == "Flying" | `Type 2` == "Flying"')
flying_count = flying_pokemons.shape[0]

poison_pokemons = df.query('`Type 1` == "Poison" | `Type 2` == "Poison"')
poison_count = poison_pokemons.shape[0]

bug_pokemons = df.query('`Type 1` == "Bug" | `Type 2` == "Bug"')
bug_count = bug_pokemons.shape[0]

ground_pokemons = df.query('`Type 1` == "Ground" | `Type 2` == "Ground"')
ground_count = ground_pokemons.shape[0]

fairy_pokemons = df.query('`Type 1` == "Fairy" | `Type 2` == "Fairy"')
fairy_count = fairy_pokemons.shape[0]

electric_pokemons = df.query('`Type 1` == "Electric" | `Type 2` == "Electric"')
electric_count = electric_pokemons.shape[0]

psychic_pokemons = df.query('`Type 1` == "Psychic" | `Type 2` == "Psychic"')
psychic_count = psychic_pokemons.shape[0]

normal_pokemons = df.query('`Type 1` == "Normal" | `Type 2` == "Normal"')
normal_count = normal_pokemons.shape[0]

others_pokemons = df.query('`Type 1` != "Fire" | `Type 2` != "Fire" | `Type 1` != "Grass" | `Type 2` != "Grass" | `Type 1` != "Water" | `Type 2` != "Water" | `Type 1` != "Flying" | `Type 2` != "Flying" | `Type 1` != "Poison" | `Type 2` != "Poison" | `Type 1` != "Bug" | `Type 2` != "Bug" | `Type 1` != "Ground" | `Type 2` != "Ground" | `Type 1` != "Fairy" | `Type 2` != "Fairy" | `Type 1` != "Electric" | `Type 2` != "Electric" | `Type 1` != "Psychic" | `Type 2` != "Psychic" | `Type 1` != "Normal" | `Type 2` != "Normal"')
others_count = others_pokemons.shape[0]

vals = [fire_count, grass_count, water_count, flying_count, poison_count, bug_count, ground_count, fairy_count, electric_count, psychic_count, normal_count]
labels = ["Fire", "Grass", "Water", "Flying", "Poison", "Bug", "Ground", "Fairy", "Electric", "Psychic", "Normal"]
fig, ax = plt.subplots()
ax.pie(vals, labels=labels)
ax.axis("equal")
plt.title('Percentage of Pokemon types')
plt.show()

legendary_pokemons = df.query('Legendary == True')
not_legendary_pokemons = df.query('Legendary == False')
legendary_pokemons_count = legendary_pokemons.shape[0]
not_legendary_pokemons_count = not_legendary_pokemons.shape[0]

vals = [legendary_pokemons_count, not_legendary_pokemons_count]
labels = ["Legendary pokemons", "Not legendary pokemons"]
fig, ax = plt.subplots()
ax.pie(vals, labels=labels, wedgeprops=dict(width=0.5))
plt.title('Percentage of Legendary Pokemons')
plt.show()

#Total
total_1 = df.query('Total > 0 & Total <= 240')
total_1_count = total_1.shape[0]

total_2 = df.query('Total > 240 & Total <= 360')
total_2_count = total_2.shape[0]

total_3 = df.query('Total > 360 & Total <= 480')
total_3_count = total_3.shape[0]

total_4 = df.query('Total > 480 & Total <= 540')
total_4_count = total_4.shape[0]

total_5 = df.query('Total > 540 & Total <= 660')
total_5_count = total_5.shape[0]

total_6 = df.query('Total > 660')
total_6_count = total_6.shape[0]

index = np.arange(6)
values = [total_1_count, total_2_count, total_3_count, total_4_count, total_5_count, total_6_count]
plt.barh(index,values, color = 'violet')
plt.title('Total score of Pokemons power')
plt.show()

#Defensive Strength
Defensive_Strength = {'<= 50': [df.query('Defense <= 50').shape[0]],
                      '50 < <= 73': [df.query('Defense > 50 & Defense <= 73').shape[0]],
                      '73 < < 117': [df.query('Defense > 73 & Defense < 117').shape[0]],
                      ' > 117': [df.query('Defense > 117').shape[0]],
                      }

c = []
v = []
for key, val in Defensive_Strength.items():
    c.append(key)
    v.append(val)
v = np.array(v)
plt.bar(range(len(c)), v[:,0], color= 'pink')
plt.xticks(range(len(c)), c)
plt.title('Defensive Strength of Pokemons')
plt.show()

Fire_min = df.query('Defense <= 50 & `Type 1` == "Fire"')
Fire_min_count= len(Fire_min)

Fire_mid = df.query('Defense > 50 & Defense <= 73 & `Type 1` == "Fire"')
Fire_mid_count = len(Fire_mid)

Fire_middle = df.query('Defense > 73 & Defense < 117 & `Type 1` == "Fire"')
Fire_middle_count = len(Fire_middle)

Fire_max = df.query('Defense > 117 & `Type 1` == "Fire"')
Fire_max_count = len(Fire_max)

Water_min = df.query('Defense <= 50 & `Type 1` == "Water"')
Water_min_count = len(Water_min)

Water_mid = df.query('Defense > 50 & Defense <= 73 & `Type 1` == "Water"')
Water_mid_count= len(Water_mid)

Water_middle = df.query('Defense > 73 & Defense < 117 & `Type 1` == "Water"')
Water_middle_count = len(Water_middle)

Water_max = df.query('Defense > 117 & `Type 1` == "Water"')
Water_max_count = len(Water_max)

Grass_min = df.query('Defense <= 50 & `Type 1` == "Grass"')
Grass_min_count = len(Grass_min)

Grass_mid = df.query('Defense > 50 & Defense <= 73 & `Type 1` == "Grass"')
Grass_mid_count= len(Grass_mid)

Grass_middle = df.query('Defense > 73 & Defense < 117 & `Type 1` == "Grass"')
Grass_middle_count = len(Grass_middle)

Grass_max = df.query('Defense > 117 & `Type 1` == "Grass"')
Grass_max_count = len(Grass_max)

dic = {'Fire': {'Min': Fire_min_count, 'Mid': Fire_mid_count, 'Middle': Fire_middle_count, 'Max': Fire_max_count},
    'Grass': {'Min': Grass_min_count, 'Mid': Grass_mid_count, 'Middle': Grass_middle_count, 'Max': Grass_max_count},
     'Water': {'Min': Water_min_count, 'Mid': Water_mid_count, 'Middle': Water_middle_count, 'Max': Water_max_count}}
df = pd.DataFrame(dic)

df.plot(kind="bar", stacked=True)
plt.title('Distribution of power types for certain types of Pokémon')
plt.show()

total1_min = min(total_1['Total'])
print('Minimum value of Total: ', total1_min)
total_6_max = max(total_6['Total'])
print('Maximum value of Total: ', total_6_max)

fmin= min(Fire_min['Defense'])
print('Minimum of Fire type: ', fmin)
fmax = max(Fire_max['Defense'])
print('Maxmum of Fire type: ', fmax)
wmin = min(Water_min['Defense'])
print('Minimum of Water type: ', wmin)
wmax = max(Water_max['Defense'])
print('Maximum of Water type: ', wmax)
gmin = min(Grass_min['Defense'])
print('Minimum of Grass type: ', gmin)
gmax = max(Grass_max['Defense'])
print('Maximum of Grass type: ', gmax)

minmax_dic = {'Fire': {'Min': fmin, 'Max': fmax},
              'Water': {'Min': wmin, 'Max': wmax},
              'Grass': {'Min': gmin, 'Max': gmax }}
df = pd.DataFrame(minmax_dic)

df.plot(kind="bar", stacked=True)
plt.title('Сomparison of minimum and maximum values for some types')
plt.show()
