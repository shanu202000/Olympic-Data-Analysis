import pandas as pd
import numpy as np
def Medal_Tally(ath):
    #droping duplicates
    ath.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'], inplace=True)
    #groupby with country
    Medal_Tally = ath.groupby('region').sum()[['Gold', 'Silver', 'Bronze']].sort_values('Gold', ascending=False).reset_index()
    Medal_Tally['Total'] = Medal_Tally['Gold'] + Medal_Tally['Silver'] + Medal_Tally['Bronze']
    return Medal_Tally
def year(ath):
    year = ath["Year"].unique().tolist()
    year.sort()
    year.insert(0,'Overall')
    return year
def country(ath):
    country = np.unique(ath['region'].dropna()).tolist()
    country.sort()
    country.insert(0, 'Overall')
    return country
def fetch_medal_tally(df, year, country):
    medal_df = df.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'])
    flag = 0
    if year == 'Overall' and country == 'Overall':
        temp_df = medal_df
    if year == 'Overall' and country != 'Overall':
        flag = 1
        temp_df = medal_df[medal_df['region'] == country]
    if year != 'Overall' and country == 'Overall':
        temp_df = medal_df[medal_df['Year'] == int(year)]
    if year != 'Overall' and country != 'Overall':
        temp_df = medal_df[(medal_df['Year'] == year) & (medal_df['region'] == country)]

    if flag == 1:
        x = temp_df.groupby('Year').sum()[['Gold', 'Silver', 'Bronze']].sort_values('Year').reset_index()
    else:
        x = temp_df.groupby('region').sum()[['Gold', 'Silver', 'Bronze']].sort_values('Gold',
                                                                                      ascending=False).reset_index()

    x['total'] = x['Gold'] + x['Silver'] + x['Bronze']
    return x
def data_over_time(ath,col):
    nations_over_time = ath.drop_duplicates(['Year', col])['Year'].value_counts().reset_index().sort_values('Year')
    nations_over_time.rename(columns={'Year': 'Edition', 'count': col}, inplace=True)
    return nations_over_time


def mostsus(df, sports):
    temp = df.dropna(subset=["Medal"])
    if sports != 'Overall':
        temp = temp[temp["Sport"] == sports]
    return temp['Name'].value_counts().reset_index().head(14).merge(df, on='Name', how='left')[["Name", 'count', 'Sport', 'region']].drop_duplicates("Name")
def medal_countrywise(df,country):
    temp = df.dropna(subset=["Medal"])
    temp = temp.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'])
    temp = temp[temp['region'] == country]
    temp=temp.groupby('Year').count()["Medal"].reset_index()
    return temp

def pivot_table(df,counrty):
    temp = df.dropna(subset=['Medal'])
    temp = temp[temp['region'] == country]
    temp = temp.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal']  )

    pt=temp.pivot_table(index='Sport', columns='Year', values='Medal', aggfunc='count').fillna(0)
    return pt

def top_athlete(df,country):
    temp = df.dropna(subset=['Medal'])
    temp = temp[temp['region'] == country]
    temp=temp['Name'].value_counts().reset_index().head(10).merge(df, on="Name", how="left")[["Name", "Sport", "count"]].drop_duplicates(['Name'])
    return temp

def weight_v_height(df,sport):
    athlete_df = df.drop_duplicates(subset=['Name', 'region'])
    athlete_df['Medal'].fillna('No Medal', inplace=True)
    if sport != 'Overall':
        temp_df = athlete_df[athlete_df['Sport'] == sport]
        return temp_df
    else:
        return athlete_df

def men_vs_women(df):
    athlete_df = df.drop_duplicates(subset=['Name', 'region'])

    men = athlete_df[athlete_df['Sex'] == 'M'].groupby('Year').count()['Name'].reset_index()
    women = athlete_df[athlete_df['Sex'] == 'F'].groupby('Year').count()['Name'].reset_index()

    final = men.merge(women, on='Year', how='left')
    final.rename(columns={'Name_x': 'Male', 'Name_y': 'Female'}, inplace=True)

    final.fillna(0, inplace=True)

    return final