import streamlit as st
import numpy as np
import pandas as pd

st.title("Lending Risk Scoring Simulation")

# Sliders for thresholds
LOW = st.slider("Low threshold", 0.0, 0.1, 0.02)
HIGH = st.slider("High threshold", 0.0, 0.2, 0.08)

# Simulate probability of default scores
scores = np.random.beta(2, 10, 50)

def apply_decision(score):
    if score < LOW:
        return 'approve'
    elif score > HIGH:
        return 'decline'
    else:
        return 'manual_review'

decisions = [apply_decision(s) for s in scores]
df = pd.DataFrame({"Score": scores, "Decision": decisions})

st.table(df)

