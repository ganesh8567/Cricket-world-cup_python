import pandas as pd
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv(r"C:/Users/ganes/CWC2023.csv")

# Title
st.title("CWC 2023 Analysis Dashboard")

# Section 1: Data Overview
st.header("Dataset Overview")
st.write("### Dataset")
st.dataframe(data)
st.write("### Statistical Summary")
numerical_columns = ['Score A', 'Score B', 'Overs Played A', 'Overs Played B']
st.write(data[numerical_columns].describe())

# Section 2: Toss Decision Analysis
st.header("Toss Decision Analysis")
toss_decision_counts = data.groupby(['Toss Decision', 'Wining Team']).size().reset_index(name='Count')
st.write(toss_decision_counts)
st.write("### Toss Decision Distribution")
fig = px.pie(data, names='Toss Decision', title='Toss Decision Distribution')
st.plotly_chart(fig)

# Section 3: Scores and Winning Margins
st.header("Score and Margin Analysis")
st.write("### Scores Over Time")
fig = px.line(data, x="Match Date", y=["Score A", "Score B"])
st.plotly_chart(fig)

st.write("### Winning Margins")
data['Winning Margin'] = abs(data['Score A'] - data['Score B'])
fig = px.box(data, y="Winning Margin", color="Wining Team", title="Winning Margin by Team")
st.plotly_chart(fig)

# Section 4: Total Boundaries
st.header("Total Boundaries by Team")
boundaries = data.groupby('Wining Team')[['4s A', '6s A', '4s B', '6s B']].sum().reset_index()
boundaries['Total Boundaries'] = boundaries['4s A'] + boundaries['6s A'] + boundaries['4s B'] + boundaries['6s B']
fig = px.bar(boundaries, x='Wining Team', y='Total Boundaries', title="Total Boundaries by Team")
st.plotly_chart(fig)

# Section 5: Matches Played by City
st.header("Matches Played by City")
city_match_counts = data['City'].value_counts().reset_index()
city_match_counts.columns = ['City', 'Matches Played']
fig = px.bar(city_match_counts, x="City", y="Matches Played", title="Matches Played in Each City")
st.plotly_chart(fig)

# Section 6: Top Performers
st.header("Top Performers - Man of the Match")
man_of_match_counts = data['Man of the Match'].value_counts().reset_index()
man_of_match_counts.columns = ['Player', 'Man of the Match Count']
fig = px.bar(man_of_match_counts.head(10), x='Player', y='Man of the Match Count', title="Top Performers")
st.plotly_chart(fig)

# Section 7: Umpire Analysis
st.header("Umpire Analysis")
umpire_counts = data['Umpire 1'].value_counts().head(10).reset_index()
umpire_counts.columns = ['Umpire', 'Matches Officiated']
fig = px.bar(umpire_counts, x="Umpire", y="Matches Officiated", title="Top Umpires - Matches Officiated")
st.plotly_chart(fig)