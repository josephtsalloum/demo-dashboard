### 10/11/24 ### 
### Dashboard_v2 ### 
### Todays dev plan 
    ### build funcitons that can call all of the graphs of make each kpi their own function so that editing a compenent of the dash is optimized
    ### make KPI functions with indepdent df. 


import streamlit as st 
import pandas as pd 
import plotly_express as px 
import math 
import os 
import time 
import warnings 



### Browser Tab Info ### 
st.set_page_config(page_title= "Liberty Trade Corp", page_icon =":candy:", layout="wide")


### Center Console ### 

### This will be where the user can find the Campaign Report ### 
st.header("This is the Campaign Report for Sunny Island")

### File path and data collection ### 
file_path = "C:/Users/Admin/Python_Projects/app3.csv"

### Setting up the data frame from the entire report and having the report print out in general ###
### This way the user can just look at the report if the wanted too ### 
df = pd.read_csv(file_path,
                 skiprows = 0,
                 nrows = 550)

### Making the Campaign Report  and calling it within the APP ## 
df_campaignreport = df 
### this is how you call the campaign report before the filter affects it #df_campaignreport

### Pre Report ### 



### Side bar ### 

### Filter collection for the campaign report ### 
status_filter = st.sidebar.multiselect("Status",
                                       options = df_campaignreport["Status"].unique(),
                                       default = df_campaignreport["Status"].unique())
### This section is the part that updates the the original data frame with the status filter ### 
df_filtered_campaignreport = df_campaignreport[df_campaignreport["Status"].isin(status_filter)]
df_filtered_campaignreport

### Report View Filter ### 

### This filter will generate the Users Desired Report to help them make certain marketing Decisions ### 
kpi_selectbox = st.sidebar.selectbox("Select KPI",["Spend","Sales (7 days)","(ACOS)"])

def generate_report(kpis):
    # Dictionary that will house all the reports
    reports = {
    "Spend": "Spend",
    "(ACOS)" : "(ACOS)",
    "Sales (7 days)": "Sales (7 days)",
    "Impressions": "Impressions",
    "Click-Thru Rate (CTR)":"Click-Thru Rate (CTR)",
    "Cost Per Click (CPC)":"Cost Per Click (CPC)",
    "Clicks":"Clicks",
    "Campaign Type":"Campaign Type"
    }

    ## loop that will collect all the user input and generate the reports ## 
    for kpi in kpis:
        if kpi == "Spend":
            chart = px.bar(df_filtered_campaignreport, x="Campaign Name", y="Spend")
            df_spendreport = df_campaignreport(["Campaign Name","Status","Spend",])
            df_spendreport
        elif kpi == "Sales (7 days)":
            chart = px.bar(df_filtered_campaignreport,x="Campaign Name", y="Sales(7 days)")
            df_salesreport = df_campaignreport(["Campaign Name", "Status","Sales (7 days)"])
            df_salesreport
        elif kpi == "(ACOS)":
            chart = px.bar(df_filtered_campaignreport,x="Campaing Name",y="(ACOS)")
            df_acosreport = df_campaignreport(["Campaign Name","Status","(ACOS)"])







