import streamlit as st
import pandas as pd
import helper, preprocessor
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.figure_factory as ff

df = pd.read_csv('athlete_events.csv')
region_df = pd.read_csv('noc_regions')

df = preprocessor.preprocess(df, region_df)
