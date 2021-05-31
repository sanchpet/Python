import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

df = pd.read_csv('./Aids2.csv') # импорт датасета

shp = df.shape # задание 2
sz = df.size
types = df.dtypes

tf = df.loc[:, 'sex'] # разделение на два сабсета
k = 0
for i in range(shp[0]):
    if tf[i] == 'M':
        k = k + 1

print("Male(%):") # процентное соотношение мужчин и женщин - задание 3
print(k * 100 / shp[0])
print("Female(%):")
print((shp[0] - k) * 100 / shp[0])

MAs45 = df.query('status == "A" & age < 45 & sex == "M"').shape[0] # задание 4 - процент мужчин до 45
print("Alive Male in age < 45 to All Males (%):")
print(MAs45 * 100 / k)

sdf = df.query('age > 14 & status == "D"') # задание 5 1 способ - функция plotline
ages = sdf['age'].tolist()
unique_ages = list(dict.fromkeys(ages))
unique_ages.sort()
deaths = [ages.count(i) for i in unique_ages]
tab_df = pd.DataFrame({'age': unique_ages, 'deaths': deaths})
tab_df.plot.line(x='age',y='deaths')
plt.show()
fig = px.line(tab_df, x="age", y="deaths", title='Deaths rate for ages > 14') # 2 способ plotly
fig.show()


sdf = df.query('age < 30 & status == "D"') # задание 6 1- способ круговая plotpie
wc = sdf.shape[0]
indexes = sdf['state'].tolist()
ind = list(dict.fromkeys(indexes))
perc = [indexes.count(i)/wc for i in ind]
pie_df = pd.DataFrame({'percent of dead': perc}, index = ind)
pie_df.plot.pie(y='percent of dead')
plt.show()

labels = ind # задание 6 2- способ круговая matplotlib
sizes = perc
explode = (0, 0, 0, 0)
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90, normalize=False)
plt.show()


ways = df['T.categ'].tolist() # задание 9
ways = list(dict.fromkeys(ways))

ov_mean = df['age'].mean()
state_means = []
state_ways = {'hs': [],
              'haem': [],
              'other': [],
              'hsid': [],
              'het': [],
              'id': [],
              'mother': [],
              'blood': [],
}

for i in ind: # перебор штатов
  sm = df.loc[lambda df: df['state'] == i] # выбор штата
  state_means.append(sm['age'].mean()) # Средний возраст в штате для 7
  for j in list(state_ways.keys()): # преебор путей передачи для каждго штата для 9
    sd = sm.loc[lambda sm: sm['T.categ'] == j] # выбор пути передачи из датасета
    state_ways[j].append(sd.shape[0]) # добавление в список по ключу словаря  кол-во заразившихся

pd.DataFrame(state_ways, index = ind).plot.bar(rot=0)
pd.DataFrame({'Average age in states': state_means}, index = ind).plot.bar(rot=0)
plt.show()

state_ages={'age <= 30 & status == "D"': [], # задание 8
            'age > 30 & age <= 54 & status == "D"': [],
            'age > 54 & status == "D"': [],
}

minmaxage={'NSW': [],
           'QLD': [],
           'Other': [],
           'VIC': [],
}

for i in ind: #
  sm = df.loc[lambda df: df['state'] == i]
  minmaxage[i].append(sm['age'].min())
  minmaxage[i].append(sm['age'].max())
  for j in list(state_ages.keys()):
    state_ages[j].append(sm.query(j).shape[0])

pd.DataFrame(state_ages, index = ind).plot.bar(rot=0) # вывод умерших по возрасту и по штатам для 8
plt.show()

state_ages2={'age <= 30': [], # задание 10
            'age > 30 & age <= 54': [],
            'age > 54': [],
}

for i in list(state_ages2.keys()):
    age_group = df.query(i)
    deads = age_group.query('status == "D"')
    alives = age_group.query('status == "A"')
    state_ages2[i].append('Dead: ' + str(deads.shape[0]*100/age_group.shape[0]) + ' %')
    state_ages2[i].append('Alive: ' + str(alives.shape[0]*100/age_group.shape[0]) + ' %')

print(state_ages2) # таких нет поэтому выводим все


print("Austaralia average age:", end=" ") # задание 7 - средний возраст по Австралии
print(ov_mean)
print(ind)
print(state_means)
print("Min and Max age:")  # самый молодой и самый старый по регионам 8
print(minmaxage)
