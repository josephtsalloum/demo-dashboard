### 10/11/24 ### 
### Dashboard_v2 ### 

### 10/11 Coding Recap 
    # Today was a very productive day as I was able to basically recreate the entire dashboard the way I needed to in order to generate the reports for each KPI and have them deployable from the sidebar of the APP 
    # I might want to call that selectionbox something else like Reports 
    # Make more data visualization files that I can just make functions and call them to the main file so my main isn't so cluttered. I am getting annoyed with all of the functions and the clutter on the worksheet. 

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
kpi_selectbox = st.sidebar.selectbox("Select KPI",["Spend","Sales (7 days)","(ACOS)","Impressions","Clicks","Click-Thru Rate (CTR)","Cost Per Click (CPC)","Clicks"])

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
            st.text("This is your Spend Report")
            chart = px.bar(df_filtered_campaignreport, x="Campaign Name", y="Spend")
            df_report = df_campaignreport(["Campaign Name","Status","Spend",])
            df_report
        
        elif kpi == "Sales (7 days)":
            st.text("This is your Sales (7 days) Report")
            chart = px.bar(df_filtered_campaignreport,x="Campaign Name", y="Sales(7 days)")
            df_report = df_campaignreport(["Campaign Name", "Status","Sales (7 days)"])
            df_report
        
        elif kpi == "(ACOS)":
            st.text("This is your ACOS Report")
            chart = px.bar(df_filtered_campaignreport,x="Campaing Name",y="(ACOS)")
            df_report = df_campaignreport(["Campaign Name","Status","(ACOS)"])
            df_report
        
        elif kpi == "Impressions":
            st.text("This is your Impressions Report")
            chart = px.bar(df_filtered_campaignreport,x="Campaing Name",y="Impressions")
            df_acosreport = df_campaignreport(["Campaign Name","Status","Impresssions"])
            df_report
        
        elif kpi == "Clicks":
            st.text("This is your Campaign Click Report")
            chart = px.bar(df_filtered_campaignreport,x="Campaing Name",y="Clicks")
            df_acosreport = df_campaignreport(["Campaign Name","Status","Impressions","Clicks"])
            df_report

        elif kpi == "Click-Thru Rate (CTR)":
            st.text("This is your Click-Thru Rate Report")
            chart = px.bar(df_filtered_campaignreport,x="Campaing Name",y="Click-Thru Rate(CTR)")
            df_report = df_campaignreport(["Campaign Name","Status","Impressions","Clicks","Click-Thru Rate(CTR)"])
            df_report
     
        elif kpi == "Cost Per Click (CPC)":
            st.text("This is your Cost Per Click Report")
            chart = px.bar(df_filtered_campaignreport,x="Campaing Name",y="Cost Per Click (CPC)")
            df_report = df_campaignreport(["Campaign Name","Status","Impressions","Clicks","Cost Per Click (CPC)"])
            df_report

        print(f'Chart: {chart}')
        print(f'Data of the Report: {df_report}')
    return reports

if st.sidebar.button("Generate Report"):
    reports = generate_report(kpi_selectbox)

    for kpi, report in reports.items():
        st.header(kpi)
        st.plotly_chart(report("chart"))
        st.write(report("df"))




