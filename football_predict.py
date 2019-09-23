#international soccer/football games prediciton based on all international soccer games played 1872-2019

#football_predict.py

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
import time
import matplotlib as mpl
from warnings import simplefilter
simplefilter(action='ignore', category=FutureWarning)



#print(football_data.columns)
#print(football_data)
#['date', 'home_team', 'away_team', 'home_score', 'away_score',
      #'tournament', 'city', 'country', 'neutral']
country='England'

def create_game_df(country, football_data):

	df_country=pd.DataFrame()
	df_country_temp=pd.DataFrame()

#Creates a data frame for country with all its home games with scores
	df_country['date']=football_data.loc[(football_data['home_team'] == country)].date
	df_country['country_score']=football_data.loc[(football_data['home_team'] == country)].home_score
	df_country['other_score']=football_data.loc[(football_data['home_team'] == country)].away_score

#Creates a data frame for country with all its away games with scores
	df_country_temp['date']=football_data.loc[(football_data['away_team'] == country)].date
	df_country_temp['country_score']=football_data.loc[(football_data['away_team'] == country)].away_score
	df_country_temp['other_score']=football_data.loc[(football_data['away_team'] == country)].home_score

#I have not found a way to make this prettier, I am sure there is a way by putting an or conditional statement
#but I get errors when using an 'or' statement

#Creates the a row with an outcome from the game outcome => win, loss, or tie
	temp_arr = []
	for index, row in df_country.iterrows():
	
		if(row.country_score>row.other_score):
			temp_arr.append('win')
		elif(row.country_score<row.other_score):
			temp_arr.append('loss')
		else:
			temp_arr.append('tie')

	df_country['outcome']=temp_arr

#Same thing as the above for loop but for the away games data frame
	temp_arr1 = []
	for index, row in df_country_temp.iterrows():
	
		if(row.country_score>row.other_score):
			temp_arr1.append('win')
		elif(row.country_score<row.other_score):
			temp_arr1.append('loss')
		else:
			temp_arr1.append('tie')

	df_country_temp['outcome']=temp_arr1

#concat both data frames into one data frame
	df_country=pd.concat([df_country, df_country_temp], sort=False)

	print(df_country)

	return df_country


#_____MAIN____#

football_path='results.csv'
football_data=pd.read_csv(football_path)

england_df=create_game_df('England', football_data)