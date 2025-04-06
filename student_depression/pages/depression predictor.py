# -*- coding: utf-8 -*-
"""
Created on Mon Apr  7 00:58:32 2025

@author: VEYDAANT
"""

import streamlit as st
import pandas as pd
import numpy as np

st.title("🧠 Depression Prediction (Simple Logic-Based)")

st.markdown("### Input Student Details")

gender = st.selectbox("Gender", ["Male", "Female", "Other"])
age = st.slider("Age", 18, 40, 22)
academic_pressure = st.slider("Academic Pressure (1-5)", 1, 5, 3)
work_pressure = st.slider("Work Pressure (0-5)", 0, 5, 2)
cgpa = st.slider("CGPA", 0.0, 10.0, 7.0)
study_satisfaction = st.slider("Study Satisfaction (1-5)", 1, 5, 3)
sleep_duration = st.selectbox("Sleep Duration", ["Less than 5 hours", "5-6 hours", "7-8 hours", "More than 8 hours"])
suicidal_thoughts = st.selectbox("Ever had suicidal thoughts?", ["Yes", "No"])
financial_stress = st.slider("Financial Stress (1-5)", 1, 5, 3)
family_history = st.selectbox("Family History of Mental Illness", ["Yes", "No"])

# Simple scoring system
score = 0
score += academic_pressure
score += work_pressure
score += 5 - study_satisfaction
score += financial_stress
if sleep_duration == "Less than 5 hours":
    score += 2
if suicidal_thoughts == "Yes":
    score += 5
if family_history == "Yes":
    score += 2
if cgpa < 6.0:
    score += 1

# Output
if st.button("Check Likelihood"):
    st.markdown("### Result")
    if score >= 13:
        st.error("High likelihood of depression 😟")
    elif score >= 9:
        st.warning("Moderate likelihood of depression 😐")
    else:
        st.success("Low likelihood of depression 🙂")
