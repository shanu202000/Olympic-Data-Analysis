import streamlit as st
import pandas as pd
import preprocessor,helper
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.figure_factory  as ff
import scipy
ath=pd.read_csv('athlete_events.csv')
cnt=pd.read_csv("noc_regions.csv")
st.sidebar.title("Olympic Analysis")
ath=preprocessor.preprocess(ath,cnt)
usermenu=st.sidebar.radio('Select an option',
                 ("Medal-Tally","Overall Analysis","Athelete-Wise","Country-Wise"))
#st.dataframe(ath)
if usermenu == "Medal-Tally":
    st.sidebar.header("Medal-Tally")
    year=helper.year(ath)
    selected_yrs=st.sidebar.selectbox("Select Year",year)
    Country=helper.country(ath)
    slected_country=st.sidebar.selectbox("Select Country", Country)
    mt=helper.fetch_medal_tally(ath,selected_yrs,slected_country)
    if selected_yrs=="Overall" and slected_country=="Overall":
        st.title('Overall Medal Tally')
    if selected_yrs=="Overall" and slected_country!="Overall":
        st.title("Overall Medal Tally of " + slected_country)
    if selected_yrs!="Overall" and slected_country=="Overall":
        st.title(' Overall Medal Tally in '+ str(selected_yrs) )
    if selected_yrs!="Overall" and slected_country!="Overall":
        st.title('Medal Tally of ' +slected_country+' in '+str(selected_yrs))
    st.table(mt)

if usermenu == 'Overall Analysis':
    editions = ath['Year'].unique().shape[0] - 1
    cities = ath['City'].unique().shape[0]
    sports = ath['Sport'].unique().shape[0]
    events = ath['Event'].unique().shape[0]
    athletes = ath['Name'].unique().shape[0]
    nations = ath['region'].unique().shape[0]

    st.title("Top Statistics")
    col1,col2,col3 = st.columns(3)
    with col1:
        st.header("Editions")
        st.title(editions)
    with col2:
        st.header("Hosts")
        st.title(cities)
    with col3:
        st.header("Sports")
        st.title(sports)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("Events")
        st.title(events)
    with col2:
        st.header("Nations")
        st.title(nations)
    with col3:
        st.header("Athletes")
        st.title(athletes)

    nations_over_time = helper.data_over_time(ath, 'region')
    fig = px.line(nations_over_time, x="Edition", y="region")
    st.title("Participating Nations over the years")
    st.plotly_chart(fig)

    Event_over_time = helper.data_over_time(ath, 'Event')
    fig = px.line(Event_over_time, x="Edition", y="Event")
    st.title(" Events over the years")
    st.plotly_chart(fig)

    Player_over_time = helper.data_over_time(ath, 'Name')
    fig = px.line(Player_over_time, x="Edition", y="Name")
    st.title("Participating Player over the years")
    st.plotly_chart(fig)

    st.title("No of Events over time(every sports)")
    fig,ax=plt.subplots(figsize=(10,10))
    ht=ath.drop_duplicates(['Year','Sport',"Event"])
    ax=sns.heatmap(ht.pivot_table(index="Sport",columns="Year",values="Event",aggfunc="count").fillna(0).astype('int'),annot=True)
    st.pyplot(fig)

    st.title("Most Successfull Athelete")
    sport_list=ath["Sport"].unique().tolist()
    sport_list.sort()
    sport_list.insert(0,"Overall")
    selected_sport=st.selectbox("Select a Sport",sport_list)
    x=helper.mostsus(ath,selected_sport)
    st.table(x)

if usermenu == 'Country-Wise':
    st.sidebar.title("Country wise Analysis")
    countrylist=ath['region'].dropna().unique().tolist()
    countrylist.sort()
    country=st.sidebar.selectbox("Select Country",countrylist)
    temp=helper.medal_countrywise(ath,country)
    fig = px.line(temp, x="Year", y="Medal")
    st.title(country  +  " Medal Chart over the years")
    st.plotly_chart(fig)

   # st.title("Medal HeatMap in Every Sport of " + country)
   # pt=helper.pivot_table(ath,country)
   # ax = sns.heatmap(pt,annot=True)
    #st.pyplot(fig)

    st.title("Most Successfull Athelete from "  + country)
    temp=helper.top_athlete(ath,country)
    st.table(temp)

if usermenu == 'Athelete-Wise':
    athlete_df = ath.drop_duplicates(subset=['Name', 'region'])

    x1 = athlete_df['Age'].dropna()
    x2 = athlete_df[athlete_df['Medal'] == 'Gold']['Age'].dropna()
    x3 = athlete_df[athlete_df['Medal'] == 'Silver']['Age'].dropna()
    x4 = athlete_df[athlete_df['Medal'] == 'Bronze']['Age'].dropna()

    fig = ff.create_distplot([x1, x2, x3, x4], ['Overall Age', 'Gold Medalist', 'Silver Medalist', 'Bronze Medalist'],show_hist=False, show_rug=False)
    fig.update_layout(autosize=False,width=1000,height=600)
    st.title("Distribution of Age")
    st.plotly_chart(fig)

    x = []
    name = []
    famous_sports = ['Basketball', 'Judo', 'Football', 'Tug-Of-War', 'Athletics',
                     'Swimming', 'Badminton', 'Sailing', 'Gymnastics',
                     'Art Competitions', 'Handball', 'Weightlifting', 'Wrestling',
                     'Water Polo', 'Hockey', 'Rowing', 'Fencing',
                     'Shooting', 'Boxing', 'Taekwondo', 'Cycling', 'Diving', 'Canoeing',
                     'Tennis', 'Golf', 'Softball', 'Archery',
                     'Volleyball', 'Synchronized Swimming', 'Table Tennis', 'Baseball',
                     'Rhythmic Gymnastics', 'Rugby Sevens',
                     'Beach Volleyball', 'Triathlon', 'Rugby', 'Polo', 'Ice Hockey']
    for sport in famous_sports:
        temp_df = athlete_df[athlete_df['Sport'] == sport]
        x.append(temp_df[temp_df['Medal'] == 'Gold']['Age'].dropna())
        name.append(sport)

    fig = ff.create_distplot(x, name, show_hist=False, show_rug=False)
    fig.update_layout(autosize=False, width=1000, height=600)
    st.title("Distribution of Age wrt Sports(Gold Medalist)")
    st.plotly_chart(fig)

    sport_list = ath["Sport"].unique().tolist()
    sport_list.sort()
    sport_list.insert(0, "Overall")

    st.title('Height Vs Weight')
    selected_sport = st.selectbox('Select a Sport', sport_list)
    temp_df = helper.weight_v_height(ath, selected_sport)
    fig, ax = plt.subplots()
    ax = sns.scatterplot(x=temp_df['Weight'], y=temp_df['Height'], hue=temp_df['Medal'], style=temp_df['Sex'], s=60)
    st.pyplot(fig)

    st.title("Men Vs Women Participation Over the Years")
    final = helper.men_vs_women(ath)
    fig = px.line(final, x="Year", y=["Male", "Female"])
    fig.update_layout(autosize=False, width=1000, height=600)
    st.plotly_chart(fig)

