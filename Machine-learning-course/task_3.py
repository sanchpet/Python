import pandas as pd
DATA = pd.read_csv("candy-data.csv", delimiter=',', index_col='competitorname')
DATA
#обучение модели будем проводить на данных, за исключением некоторых конфет
train_data = DATA.drop(['Milky Way','Mr Good Bar'])
train_data

#отбираем данные для предикторов, удаляя два последних столбца, индекс не включается в данные.
X = pd.DataFrame(train_data.drop(['winpercent', 'Y'], axis=1))
#указываем столбец отклика
y = pd.DataFrame(train_data['winpercent'])
#подключаем модель линейной регрессии из библиотеки sklearn
from sklearn.linear_model import LinearRegression
#обучение модели
reg = LinearRegression().fit(X, y)
#предсказание для конфет введеных вручную
reg.predict([[0, 1, 0, 1, 0, 1, 1, 0, 0, 0.93, 0.635]])



#предсказание для конфет из таблицы

#выбираем строку из таблицы
AirHeads = DATA.loc['Mr Good Bar',:].to_frame().T

#отбираем данные для предикторов и выполняем предсказание с помощью модели
reg.predict(AirHeads.drop(['winpercent', 'Y'], axis=1))


reg.intercept_

reg.coef_
