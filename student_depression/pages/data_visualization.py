# -*- coding: utf-8 -*-
"""
Created on Mon Apr  7 00:58:23 2025

@author: VEYDAANT
"""

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("📊 Data Visualization")

df = pd.read_csv("student_depression/student_depression.csv")
df['Sleep Duration'] = df['Sleep Duration'].str.replace("'", "").str.strip()

st.markdown("### 1. Depression by Gender")
fig1, ax1 = plt.subplots()
sns.countplot(data=df, x='Gender', hue='Depression', ax=ax1)
st.pyplot(fig1)

st.markdown("### 2. Academic Pressure vs Depression")
fig2, ax2 = plt.subplots()
sns.boxplot(data=df, x='Depression', y='Academic Pressure', ax=ax2)
st.pyplot(fig2)

st.markdown("### 3. CGPA vs Depression")
fig3, ax3 = plt.subplots()
sns.boxplot(data=df, x='Depression', y='CGPA', ax=ax3)
st.pyplot(fig3)

st.markdown("### 4. Sleep Duration vs Depression")
fig4, ax4 = plt.subplots()
order = ['Less than 5 hours', '5-6 hours', '7-8 hours', 'More than 8 hours']
sns.countplot(data=df, x='Sleep Duration', hue='Depression', order=order, ax=ax4)
st.pyplot(fig4)

st.markdown("### 5. Financial Stress vs Depression")
fig5, ax5 = plt.subplots()
sns.countplot(data=df, x='Financial Stress', hue='Depression', ax=ax5)
st.pyplot(fig5)

st.markdown("### 6. Correlation Heatmap")
fig6, ax6 = plt.subplots()
num_cols = ['Age', 'Academic Pressure', 'Work Pressure', 'CGPA', 'Study Satisfaction', 'Job Satisfaction', 'Work/Study Hours', 'Depression']
sns.heatmap(df[num_cols].corr(), annot=True, cmap="coolwarm", ax=ax6)
st.pyplot(fig6)
