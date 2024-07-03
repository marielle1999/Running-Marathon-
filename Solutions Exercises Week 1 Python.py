#import the data
import pandas as pd
WorldHappiness = pd.read_csv('World Happiness 2019.csv')
WorldHappiness.head()

#----------Exercise 1a
import matplotlib.pyplot as plt

Happiness_Score = WorldHappiness['Happiness_Score']
GDP_per_capita = WorldHappiness['GDP_per_capita']

plt.scatter(Happiness_Score,GDP_per_capita)
plt.title('Happiness and GDP')
plt.xlabel('GDP per capita')
plt.ylabel('Happiness Score')


#----------Exercise 1b
import scipy.stats

scipy.stats.pearsonr(Happiness_Score,GDP_per_capita)


#----------Exercise 1c
import seaborn as sn
data = WorldHappiness[['Happiness_Score','GDP_per_capita','Social_support','Healthy_life_expectancy',
                       'Freedom_to_make_life_choices','Generosity','Perceptions_of_corruption']] #select only the relevant data
sn.pairplot(data) #create pairplot

matrix = data.corr() #create correlation matrix
sn.heatmap(matrix, annot=True) #create heatmap

scipy.stats.pearsonr(data['Happiness_Score'],data['Generosity']) #there is no significant correlation between happiness and generosity

#----------Exercise 2

#import file
video_games = pd.read_excel('video_games.xlsx')
video_games.head()

#import relevant package
import statsmodels.formula.api as sm

#model 1
model1 = sm.ols('Sales ~ Review_Score', data = video_games).fit()
print(model1.summary())

#model 2
model2 = sm.ols('Sales ~ Used_Price', data = video_games).fit()
print(model2.summary())

#model 3
model3 = sm.ols('Sales ~ Release_Year', data = video_games).fit()
print(model3.summary())

#model 4
model4 = sm.ols('Sales ~ Length_All_PlayStyles_Polled', data = video_games).fit()
print(model4.summary())