#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os


# In[4]:


import pandas as pd


# In[8]:


import plotly.express as px


# In[5]:


os


# In[6]:


data =pd.read_csv("CWC2023.csv")


# In[7]:


data


# In[10]:


numerical_columns = ['Score A', 'Score B', 'Overs Played A', 'Overs Played B']
print(data[numerical_columns].describe())


# In[12]:


toss_decision_counts = data.groupby(['Toss Decision', 'Wining Team']).size().reset_index(name='Count')
print(toss_decision_counts)


# In[14]:


fig = px.histogram(data, x="Score A")
fig.show()

# Scores over time
fig = px.line(data, x="Match Date", y=["Score A", "Score B"])
fig.show() 

# Win margin histogram
fig = px.histogram(data, x="Margin")  
fig.show()

# Win margin by team
fig = px.box(data, y="Margin", color="Wining Team")
fig.show()

# Boundaries by team
fig = px.box(data, y="Boundaries A", color="Wining Team") 
fig.show()


# In[16]:


# Calculate winning margins
data['Winning Margin'] = abs(data['Score A'] - data['Score B'])
print(data[['Team A', 'Team B', 'Winning Margin']])


# In[17]:


# Count of matches won based on toss decision
toss_decision_counts = data.groupby(['Toss Decision', 'Wining Team']).size().reset_index(name='Count')
print(toss_decision_counts)


# In[18]:


fig = px.box(data, y=['Score A', 'Score B'], title='Boxplot of Total Scores')
fig.update_layout(yaxis_title='Total Score')
fig.show()


# In[19]:


fig = px.pie(data, names='Toss Decision', title='Toss Decision Distribution')
fig.show()


# In[20]:


import matplotlib.pyplot as plt

# Calculate total scores for each team
team_scores = data.groupby('Wining Team')[['Score A', 'Score B']].sum().reset_index()

# Plotting total scores for each team
plt.figure(figsize=(10, 6))
plt.bar(team_scores['Wining Team'], team_scores['Score A'], alpha=0.7, label='Total Score Team A')
plt.bar(team_scores['Wining Team'], team_scores['Score B'], alpha=0.7, label='Total Score Team B')
plt.xlabel('Teams')
plt.ylabel('Total Score')
plt.title('Total Scores for Each Team')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# In[21]:


# Calculate average maiden overs for each team
maiden_overs = data.groupby('Wining Team')[['Maiden Overs A', 'Maiden Overs B']].mean().reset_index()

# Plotting average maiden overs for each team
plt.figure(figsize=(10, 6))
plt.bar(maiden_overs['Wining Team'], maiden_overs['Maiden Overs A'], alpha=0.7, label='Avg Maiden Overs Team A')
plt.bar(maiden_overs['Wining Team'], maiden_overs['Maiden Overs B'], alpha=0.7, label='Avg Maiden Overs Team B')
plt.xlabel('Teams')
plt.ylabel('Average Maiden Overs')
plt.title('Average Maiden Overs Bowled by Each Team')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# In[22]:


# Count occurrences of 'Man of the Match' for each player
man_of_match_counts = data['Man of the Match'].value_counts().reset_index()
man_of_match_counts.columns = ['Player', 'Man of the Match Count']

# Plotting top performers - Man of the Match
plt.figure(figsize=(12, 6))
plt.bar(man_of_match_counts['Player'][:10], man_of_match_counts['Man of the Match Count'][:10], alpha=0.7)
plt.xlabel('Player')
plt.ylabel('Man of the Match Count')
plt.title('Top Performers - Man of the Match')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# In[23]:


# Calculate total boundaries (4s and 6s) for each team
boundaries = data.groupby('Wining Team')[['4s A', '6s A', '4s B', '6s B']].sum().reset_index()
boundaries['Total Boundaries'] = boundaries['4s A'] + boundaries['6s A'] + boundaries['4s B'] + boundaries['6s B']

# Plotting total boundaries for each team
plt.figure(figsize=(10, 6))
plt.bar(boundaries['Wining Team'], boundaries['Total Boundaries'], alpha=0.7)
plt.xlabel('Teams')
plt.ylabel('Total Boundaries')
plt.title('Total Boundaries (4s and 6s) Hit by Each Team')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# In[24]:


# Count of matches played and their outcomes in each city
city_match_counts = data['City'].value_counts().reset_index()
city_match_counts.columns = ['City', 'Matches Played']

# Plotting matches played in each city
plt.figure(figsize=(12, 6))
plt.bar(city_match_counts['City'], city_match_counts['Matches Played'], alpha=0.7)
plt.xlabel('City')
plt.ylabel('Matches Played')
plt.title('Matches Played and Outcomes in Each City')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# In[25]:


# Calculate total wides and no balls for each team
wides_no_balls = data.groupby('Wining Team')[['Wides A', 'No Balls A', 'Wides B', 'No Balls B']].sum().reset_index()
wides_no_balls['Total Wides and No Balls'] = wides_no_balls['Wides A'] + wides_no_balls['No Balls A'] +                                              wides_no_balls['Wides B'] + wides_no_balls['No Balls B']

# Plotting total wides and no balls for each team
plt.figure(figsize=(10, 6))
plt.bar(wides_no_balls['Wining Team'], wides_no_balls['Total Wides and No Balls'], alpha=0.7)
plt.xlabel('Teams')
plt.ylabel('Total Wides and No Balls')
plt.title('Total Wides and No Balls Bowled by Each Team')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# In[26]:


# Calculate average maiden overs and extras for each team
maiden_extras = data.groupby('Wining Team')[['Maiden Overs A', 'Maiden Overs B', 'Extras A', 'Extras B']].mean().reset_index()

# Plotting average maiden overs and extras for each team
fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(10, 8))

axes[0].bar(maiden_extras['Wining Team'], maiden_extras['Maiden Overs A'], alpha=0.7, label='Avg Maiden Overs Team A')
axes[0].bar(maiden_extras['Wining Team'], maiden_extras['Maiden Overs B'], alpha=0.7, label='Avg Maiden Overs Team B')
axes[0].set_ylabel('Average Maiden Overs')
axes[0].set_title('Average Maiden Overs Bowled by Each Team')
axes[0].legend()
axes[0].tick_params(axis='x', rotation=45)

axes[1].bar(maiden_extras['Wining Team'], maiden_extras['Extras A'], alpha=0.7, label='Avg Extras Team A')
axes[1].bar(maiden_extras['Wining Team'], maiden_extras['Extras B'], alpha=0.7, label='Avg Extras Team B')
axes[1].set_ylabel('Average Extras')
axes[1].set_title('Average Extra Runs Conceded by Each Team')
axes[1].legend()
axes[1].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.show()


# In[28]:


# Count of matches officiated by each umpire
umpire1_counts = data['Umpire 1'].value_counts().reset_index()
umpire1_counts.columns = ['Umpire', 'Matches Officiated']

umpire2_counts = data['Umpire 2'].value_counts().reset_index()
umpire2_counts.columns = ['Umpire', 'Matches Officiated']

# Plotting matches officiated by each umpire
plt.figure(figsize=(12, 6))
plt.bar(umpire1_counts['Umpire'][:10], umpire1_counts['Matches Officiated'][:10], alpha=0.7, label='Umpire 1')
plt.bar(umpire2_counts['Umpire'][:10], umpire2_counts['Matches Officiated'][:10], alpha=0.7, label='Umpire 2')
plt.xlabel('Umpires')
plt.ylabel('Matches Officiated')
plt.title('Top Umpires and Matches Officiated')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# In[29]:


# Count of matches officiated by each umpire
umpire1_counts = data['Umpire 1'].value_counts().reset_index()
umpire1_counts.columns = ['Umpire', 'Matches Officiated']

umpire2_counts = data['Umpire 2'].value_counts().reset_index()
umpire2_counts.columns = ['Umpire', 'Matches Officiated']

# Plotting matches officiated by each umpire
plt.figure(figsize=(12, 6))
plt.bar(umpire1_counts['Umpire'][:10], umpire1_counts['Matches Officiated'][:10], alpha=0.7, label='Umpire 1')
plt.bar(umpire2_counts['Umpire'][:10], umpire2_counts['Matches Officiated'][:10], alpha=0.7, label='Umpire 2')
plt.xlabel('Umpires')
plt.ylabel('Matches Officiated')
plt.title('Top Umpires and Matches Officiated')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# In[ ]:




