# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import streamlit as st


st.header('Billionaire Dataset')

file = r'C:\Users\Asif Iqbal\Desktop\Python\class 2\folder1\Billionaire.csv'
df = pd.read_csv(file)

#df = st.file_uploader(lebele= 'upload your file', type='csv')
#button = st.button('upload')


#find count of billionares by country

#Total_billionaires = df.groupby('Country')['Name'].count().sort_values()
#st.bar_chart(Total_billionaires)

#find the most popular source of income

#popular_source = df.groupby('Source')['Name'].count().nlargest(5)
#st.dataframe(popular_source)

#find the cumulative wealth of billionaries belonging to US

#df['Networth'].apply(lambda x: float(x.replace('$', '').replace(' B',)))
#cumulative_wealth_usa = df.groupby('Country')['Networth'].sum().


#interactivity
#all_countries = df['Country'].unique()

#selection = st.selectbox('Select Country', all_countries)
#subset = df[df['Country'] == selection]
#st.dataframe(subset)

#find count of billionares by country
#total_billionares = df.groupby('Country')['Name'].count()


all_countries =sorted(df['Country'].unique())
col1, col2 = st.columns(2)

# col1
# Display on Streamlit
selected_country = col1.selectbox('Select Your Country', all_countries)
# subset on selected country
subset_Country = df[df['Country'] == Selected_Country]

# get unique sources from the selected country
sources = sorted(subset_Country['source'].unique())

# display multi select option on source
selected_source = col1.multiselect('Select Source of Income', sources)

# subset on selected source
subset_source = subset_country[subset_country['Source'].isin(selected_source)

# column 2
main_string = '{} - Billionaires'.format(Selected_Country)
# main_string = selected_country + ' -Billionares
col2.header(main_string)
col2.table(subset_Country)
col2.header('source wise info')
col2.table(subset_source)