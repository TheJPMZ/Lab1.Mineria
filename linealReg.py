import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import plotly.express as px

datos = pd.read_csv("baseball.csv")

datos['attendance'] = datos['attendance'].str.replace(',', '').str.replace("']", '').astype(float)
datos['game_duration'] = datos['game_duration'].str.replace(':', '').astype(float)

# initialize the regresor
regresor = LinearRegression()

# fit the regresor 
regresor.fit(datos[['attendance']], datos['game_duration'])

# make predictions
predictions = regresor.predict(datos[['attendance']])

fig = px.scatter(x=datos['attendance'], y=datos['game_duration'], 
                 labels={'attendance':'Attendance', 'game_duration':'Game Duration'})

fig.add_shape(type='line', x0=datos['attendance'].min(), x1=datos['attendance'].max(), 
              y0=regresor.predict(datos[['attendance']]).min(), 
              y1=regresor.predict(datos[['attendance']]).max(),
              line=dict(color='red', dash='dash'))

fig.show()

# calculate R^2 score
r2 = r2_score(datos['game_duration'], predictions)

# create a result dataframe
result = pd.DataFrame({'Actual': datos['game_duration'], 'Predicted': predictions})

# save the result as an HTML file
fig.to_html("linear_regression.html")

# coefficient, intercept, and R^2 score
print('Coefficient: ', regresor.coef_)
print('Intercept: ', regresor.intercept_)
print('R^2 Score: ', r2)
