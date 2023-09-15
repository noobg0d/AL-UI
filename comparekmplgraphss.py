
# coding: utf-8

# In[1]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import plotly.express as px
import streamlit as st
from PyPDF2 import PdfMerger

merger = PdfMerger() 

# In[2]:
def plot_graphs(df1,df2):
    
    #pdf object creation
    
    bins = [0, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600, df1['Engine Speed(55)'].max()]
    bins = list(set(bins))
    bins.sort()
    labels = ['<600', '600-800', '800-1000', '1000-1200', '1200-1400', '1400-1600', '1600-1800', '1800-2000', '2000-2200', '2200-2400', '2400-2600', '2600+']
    # Calculate percentages for df1
    df1['Bin'] = pd.cut(df1['Engine Speed(55)'], bins=bins, labels=labels)
    grand_total1 = df1['Engine Speed(55)'].sum()
    df1['Percentage_VIN1'] = (df1['Engine Speed(55)'] / grand_total1) * 100
    # Calculate percentages for df2
    df2['Bin'] = pd.cut(df2['Engine Speed(55)'], bins=bins, labels=labels)
    grand_total2 = df2['Engine Speed(55)'].sum()
    df2['Percentage_VIN2'] = (df2['Engine Speed(55)'] / grand_total2) * 100
    # Create pivot tables for both dataframes
    pivot_table_percentage1 = pd.pivot_table(df1, values='Percentage_VIN1', index='Bin', aggfunc='sum').reset_index()
    pivot_table_percentage2 = pd.pivot_table(df2, values='Percentage_VIN2', index='Bin', aggfunc='sum').reset_index()
    # Merge the two pivot tables on the 'Bin' column
    merged_pivot_table = pivot_table_percentage1.merge(pivot_table_percentage2, on='Bin')
    # Set up the figure
    fig, ax = plt.subplots(figsize=(10, 6))
    # Set up the figure
    fig, ax = plt.subplots(figsize=(10, 6))
    # Define the width of each bar
    bar_width = 0.35
    index = range(len(merged_pivot_table))
    # Create bars for VIN1
    bar1 = ax.bar(index, merged_pivot_table['Percentage_VIN1'], bar_width,color='crimson')
    # Create bars for VIN2
    bar2 = ax.bar([i + bar_width for i in index], merged_pivot_table['Percentage_VIN2'], bar_width, color='yellowgreen')
    # Set labels, title, and ticks
    ax.set_xlabel('Bins')
    ax.set_ylabel('Percentage')
    ax.set_title('Engine RPM Utilization')
    ax.set_xticks([i + bar_width / 2 for i in index])
    ax.set_xticklabels(merged_pivot_table['Bin'], rotation=45, ha='right')
    # Add data labels above each bar
    for bars in [bar1, bar2]:
        for bar, percentage in zip(bars, merged_pivot_table['Percentage_VIN1' if bars == bar1 else 'Percentage_VIN2']):
            height = bar.get_height()
            ax.annotate(f'{percentage:.2f}',
                        xy=(bar.get_x() + bar.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom',fontsize=6)
    ax.legend()
    st.pyplot(fig)
            
    plt.savefig('Engine RPM Utilization.pdf', format='pdf')

    
  

    # In[6]:


    plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
    plt.scatter(df1["Wheel-Based Vehicle Speed(54)"], df1["Engine Speed(55)"], color='crimson', label='VIN-1')
    plt.title('ENGINE SPEED vs VEHICLE SPEED for VIN-1', fontsize=16)
    plt.xlabel('Wheel-Based Vehicle Speed', fontsize=12)
    plt.ylabel('Engine Speed', fontsize=12)
    plt.legend()
    # Show the plot for VIN 1
    st.pyplot(fig)
    plt.savefig('engine speed vs vehicle speed.pdf', format='pdf')

   
    

    # In[24]:


    plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
    plt.scatter(df1["Wheel-Based Vehicle Speed(54)"], df2["Engine Speed(55)"], color='crimson', label='VIN-1')
    plt.title('ENGINE SPEED vs VEHICLE SPEED for VIN-2', fontsize=16)
    plt.xlabel('Wheel-Based Vehicle Speed', fontsize=12)
    plt.ylabel('Engine Speed', fontsize=12)
    plt.legend()
    # Show the plot for VIN 1
    st.pyplot(fig)
    plt.savefig('engine speed vs vehicle speed.pdf', format='pdf')
    

    # In[31]:


 # VEHICLE SPEED UTILIZATION [VIN-1 vs VIN-2]
    bins = [0,10,20,30,40,50,60,70, df1['Wheel-Based Vehicle Speed(54)'].max()]
    bins = list(set(bins))
    bins.sort()
    labels = ['0-10','10-20','20-30','30-40','40-50','50-60','60-70','70-80']
    # Calculate percentages for df1
    df1['Bin'] = pd.cut(df1['Wheel-Based Vehicle Speed(54)'], bins=bins, labels=labels)
    grand_total1 = df1['Wheel-Based Vehicle Speed(54)'].sum()
    df1['Percentage_VIN1'] = (df1['Wheel-Based Vehicle Speed(54)'] / grand_total1) * 100
    # Calculate percentages for df2
    df2['Bin'] = pd.cut(df2['Wheel-Based Vehicle Speed(54)'], bins=bins, labels=labels)
    grand_total2 = df2['Wheel-Based Vehicle Speed(54)'].sum()
    df2['Percentage_VIN2'] = (df2['Wheel-Based Vehicle Speed(54)'] / grand_total2) * 100
    # Create pivot tables for both dataframes
    pivot_table_percentage1 = pd.pivot_table(df1, values='Percentage_VIN1', index='Bin', aggfunc='sum').reset_index()
    pivot_table_percentage2 = pd.pivot_table(df2, values='Percentage_VIN2', index='Bin', aggfunc='sum').reset_index()
    # Merge the two pivot tables on the 'Bin' column
    merged_pivot_table = pivot_table_percentage1.merge(pivot_table_percentage2, on='Bin')
    # Set up the figure
    fig, ax = plt.subplots(figsize=(10, 6))
    # Set up the figure
    fig, ax = plt.subplots(figsize=(10, 6))
    # Define the width of each bar
    bar_width = 0.35
    index = range(len(merged_pivot_table))
    # Create bars for VIN1
    bar1 = ax.bar(index, merged_pivot_table['Percentage_VIN1'], bar_width,  color='crimson')
    # Create bars for VIN2
    bar2 = ax.bar([i + bar_width for i in index], merged_pivot_table['Percentage_VIN2'], bar_width,color='yellowgreen')
    # Set labels, title, and ticks
    ax.set_xlabel('Bins')
    ax.set_ylabel('Percentage')
    ax.set_title('Vehicle Speed Utilization')
    ax.set_xticks([i + bar_width / 2 for i in index])
    ax.set_xticklabels(merged_pivot_table['Bin'], rotation=45, ha='right')
    # Add data labels above each bar
    for bars in [bar1, bar2]:
        for bar, percentage in zip(bars, merged_pivot_table['Percentage_VIN1' if bars == bar1 else 'Percentage_VIN2']):
            height = bar.get_height()
            ax.annotate(f'{percentage:.2f}',
                        xy=(bar.get_x() + bar.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom',fontsize=6)
    # Add legend
    ax.legend()
    st.pyplot(fig)
    plt.savefig('Vehicle Speed Utilization.pdf', format='pdf')
    # Add in pdf
    #save table to excel
    



  # ENGINE TORQUE UTILIZATION [VIN-1 vs VIN-2]
    bins = [1,10,20,30,40,50,60,70,80,90, df1['Actual Engine - Percent Torque(59)'].max()]
    bins = list(set(bins))
    bins.sort()
    labels = ['1-10','11-20','21-30','31-40','41-50','51-60','61-70','71-80','81-90','91-100']
    # Calculate percentages for df1
    df1['Bin'] = pd.cut(df1['Actual Engine - Percent Torque(59)'], bins=bins, labels=labels)
    grand_total1 = df1['Actual Engine - Percent Torque(59)'].sum()
    df1['Percentage_VIN1'] = (df1['Actual Engine - Percent Torque(59)'] / grand_total1) * 100
    # Calculate percentages for df2
    df2['Bin'] = pd.cut(df2['Actual Engine - Percent Torque(59)'], bins=bins, labels=labels)
    grand_total2 = df2['Actual Engine - Percent Torque(59)'].sum()
    df2['Percentage_VIN2'] = (df2['Actual Engine - Percent Torque(59)'] / grand_total2) * 100
    # Create pivot tables for both dataframes
    pivot_table_percentage1 = pd.pivot_table(df1, values='Percentage_VIN1', index='Bin', aggfunc='sum').reset_index()
    pivot_table_percentage2 = pd.pivot_table(df2, values='Percentage_VIN2', index='Bin', aggfunc='sum').reset_index()
    # Merge the two pivot tables on the 'Bin' column
    merged_pivot_table = pivot_table_percentage1.merge(pivot_table_percentage2, on='Bin')
    # Set up the figure
    fig, ax = plt.subplots(figsize=(10, 6))
    # Set up the figure
    fig, ax = plt.subplots(figsize=(10, 6))
    # Define the width of each bar
    bar_width = 0.35
    index = range(len(merged_pivot_table))
    # Create bars for VIN1
    bar1 = ax.bar(index, merged_pivot_table['Percentage_VIN1'], bar_width,  color='crimson')
    # Create bars for VIN2
    bar2 = ax.bar([i + bar_width for i in index], merged_pivot_table['Percentage_VIN2'], bar_width,  color='yellowgreen')
    # Set labels, title, and ticks
    ax.set_xlabel('Bins')
    ax.set_ylabel('Percentage')
    ax.set_title('Engine Torque Utilization')
    ax.set_xticks([i + bar_width / 2 for i in index])
    ax.set_xticklabels(merged_pivot_table['Bin'], rotation=45, ha='right')
    # Add data labels above each bar
    for bars in [bar1, bar2]:
        for bar, percentage in zip(bars, merged_pivot_table['Percentage_VIN1' if bars == bar1 else 'Percentage_VIN2']):
            height = bar.get_height()
            ax.annotate(f'{percentage:.2f}',
                        xy=(bar.get_x() + bar.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom',fontsize=6)
    # Add legend
    ax.legend()
    st.pyplot(fig)
    plt.savefig('Engine Torque Utilization.pdf', format='pdf')
    # Add in pdf
    
    
    
    # In[43]:




    # In[46]:


   # ACCELERATION PEDAL UTILIZATION [VIN-1 vs VIN-2]
    bins = [0,10,20,30,40,50,60,70,80,90, df1['Throttle Position(58)'].max()]
    bins = list(set(bins))
    bins.sort()
    labels = ['0-10','10-20','20-30','30-40','40-50','50-60','60-70','70-80','80-90','90-100']
    # Calculate percentages for df1
    df1['Bin'] = pd.cut(df1['Throttle Position(58)'], bins=bins, labels=labels)
    grand_total1 = df1['Throttle Position(58)'].sum()
    df1['Percentage_VIN1'] = (df1['Throttle Position(58)'] / grand_total1) * 100
    # Calculate percentages for df2
    df2['Bin'] = pd.cut(df2['Throttle Position(58)'], bins=bins, labels=labels)
    grand_total2 = df2['Throttle Position(58)'].sum()
    df2['Percentage_VIN2'] = (df2['Throttle Position(58)'] / grand_total2) * 100
    # Create pivot tables for both dataframes
    pivot_table_percentage1 = pd.pivot_table(df1, values='Percentage_VIN1', index='Bin', aggfunc='sum').reset_index()
    pivot_table_percentage2 = pd.pivot_table(df2, values='Percentage_VIN2', index='Bin', aggfunc='sum').reset_index()
    # Merge the two pivot tables on the 'Bin' column
    merged_pivot_table = pivot_table_percentage1.merge(pivot_table_percentage2, on='Bin')
    # Set up the figure
    fig, ax = plt.subplots(figsize=(10, 6))
    # Set up the figure
    fig, ax = plt.subplots(figsize=(10, 6))
    # Define the width of each bar
    bar_width = 0.35
    index = range(len(merged_pivot_table))
    # Create bars for VIN1
    bar1 = ax.bar(index, merged_pivot_table['Percentage_VIN1'], bar_width,  color='crimson')
    # Create bars for VIN2
    bar2 = ax.bar([i + bar_width for i in index], merged_pivot_table['Percentage_VIN2'], bar_width,color='yellowgreen')
    # Set labels, title, and ticks
    ax.set_xlabel('Bins')
    ax.set_ylabel('Percentage')
    ax.set_title('Acceleration Pedal Utilization')
    ax.set_xticks([i + bar_width / 2 for i in index])
    ax.set_xticklabels(merged_pivot_table['Bin'], rotation=45, ha='right')
    # Add data labels above each bar
    for bars in [bar1, bar2]:
        for bar, percentage in zip(bars, merged_pivot_table['Percentage_VIN1' if bars == bar1 else 'Percentage_VIN2']):
            height = bar.get_height()
            ax.annotate(f'{percentage:.2f}',
                        xy=(bar.get_x() + bar.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom',fontsize=6)
    # Add legend
    ax.legend()
    st.pyplot(fig)
    # Add in pdf
    plt.savefig('Acceleration Pedal Utilization.pdf', format='pdf')
    


  

   #---------------------------------------------------------------------------------
    #  GEAR UTILIZATION [VIN-1 vs VIN-2]
    # Your existing data and calculations
    labels = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    total_count_1 = df1['Transmission_Current_Gear(99)'].count()
    total_count_2 = df2['Transmission_Current_Gear(99)'].count()
    gear1 = [(df1['Transmission_Current_Gear(99)'] == i).sum() / total_count_1 * 100 for i in range(10)]
    gear2 = [(df2['Transmission_Current_Gear(99)'] == i).sum() / total_count_2 * 100 for i in range(10)]
    # Create a DataFrame for the chart
    data = {'Label': labels, 'gear_VIN1': gear1, 'gear_VIN2': gear2}
    df = pd.DataFrame(data)
    # Create the grouped bar chart using Matplotlib
    fig, ax = plt.subplots(figsize=(10, 6))
    width = 0.35
    x = np.arange(len(labels))
    bars1 = ax.bar(x - width/2, df['gear_VIN1'], width, color='crimson')
    bars2 = ax.bar(x + width/2, df['gear_VIN2'], width,  color='yellowgreen')
    ax.set_xlabel('Transmission_Current_Gear')
    ax.set_ylabel('Percentage')
    ax.set_title('Gear Utilization')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()
    # Add percentage labels on top of the bars
    for bar in bars1 + bars2:
        height = bar.get_height()
        ax.annotate(f'{height:.2f}%', xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom',fontsize=6)
    ax.legend()
    st.pyplot(fig)
    plt.savefig('Gear Utilization.pdf', format='pdf')
    
        
        
    merger.append('Engine RPM Utilization.pdf')
    merger.append('engine speed vs vehicle speed.pdf')
    merger.append('engine speed vs vehicle speed1.pdf')
    merger.append('Vehicle Speed Utilization.pdf')
    merger.append('Engine Torque Utilization.pdf')
    merger.append('Acceleration Pedal Utilization.pdf')
    merger.append('Gear Utilization.pdf')
    
    
    # Save the merged PDF as a single file
    merger.write('merged_plots.pdf')
    #merger.close()
    
    
        
    
    
