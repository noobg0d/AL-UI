import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import plotly.express as px
import streamlit as st
from PyPDF2 import PdfMerger

merger = PdfMerger() 


def plot_graphs(df1, df2, df3):  
    
    #custom colors
    custom_colors = ["crimson","yellowgreen","mediumblue"]
    
    st.title(":bookmark_tabs: KMPL Comparison Report for 3 Vehicles")
     


    
    #---------------------------------------------------------------------------------
    # ENGINE SPEED vs VEHICLE SPEED [SCATTER PLOT] - VIN 1
    fig_rpm_vs_oilPress = px.scatter(
        df1,
        x="Wheel-Based Vehicle Speed(54)",
        y="Engine Speed(55)",
        title="<b> ENGINE SPEED vs VEHICLE SPEED for VIN-1 </b>",
        color_discrete_sequence=[custom_colors[0],],  
        template="plotly_white"
        )
    fig_rpm_vs_oilPress.update_xaxes(title_text='Wheel-Based Vehicle Speed (kmph)')
    fig_rpm_vs_oilPress.update_yaxes(title_text='Engine Speed (rpm)')
    st.plotly_chart(fig_rpm_vs_oilPress)
    
    # ENGINE SPEED vs VEHICLE SPEED [SCATTER PLOT] - VIN 2
    fig_rpm_vs_oilPress = px.scatter(
        df2,
        x="Wheel-Based Vehicle Speed(54)",
        y="Engine Speed(55)",
        title="<b> ENGINE SPEED vs VEHICLE SPEED for VIN-2 </b>",
        color_discrete_sequence=[custom_colors[1],],  
        template="plotly_white",
        )
    fig_rpm_vs_oilPress.update_xaxes(title_text='Wheel-Based Vehicle Speed (kmph)')
    fig_rpm_vs_oilPress.update_yaxes(title_text='Engine Speed (rpm)')
    st.plotly_chart(fig_rpm_vs_oilPress)
    
    # ENGINE SPEED vs VEHICLE SPEED [SCATTER PLOT] - VIN 3
    fig_rpm_vs_oilPress = px.scatter(
        df3,
        x="Wheel-Based Vehicle Speed(54)",
        y="Engine Speed(55)",
        title="<b> ENGINE SPEED vs VEHICLE SPEED for VIN-3 </b>",
        color_discrete_sequence=[custom_colors[2],],  
        template="plotly_white",
        )
    fig_rpm_vs_oilPress.update_xaxes(title_text='Wheel-Based Vehicle Speed (kmph)')
    fig_rpm_vs_oilPress.update_yaxes(title_text='Engine Speed (rpm)')
    st.plotly_chart(fig_rpm_vs_oilPress)
    
    
    #---------------------------------------------------------------------------------
    # ENGINE RPM UTILIZATION [VIN-1 vs VIN-2 vs VIN-3]
    bins = [0, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600, df1['Engine Speed(55)'].max()]
    bins = list(set(bins))
    bins.sort()
    labels = ['<600', '600-800', '800-1000', '1000-1200', '1200-1400', '1400-1600', '1600-1800', '1800-2000', '2000-2200', '2200-2400', '2400-2600', '2600+']
    # Calculate percentages for df1
    df1['Bin'] = pd.cut(df1['Engine Speed(55)'], bins=bins, labels=labels)
    grand_total1 = df1['Engine Speed(55)'].sum()
    df1['Percentage'] = (df1['Engine Speed(55)'] / grand_total1) * 100
    # Calculate percentages for df2
    df2['Bin'] = pd.cut(df2['Engine Speed(55)'], bins=bins, labels=labels)
    grand_total2 = df2['Engine Speed(55)'].sum()
    df2['Percentage'] = (df2['Engine Speed(55)'] / grand_total2) * 100
    # Calculate percentages for df3
    df3['Bin'] = pd.cut(df3['Engine Speed(55)'], bins=bins, labels=labels)
    grand_total3 = df3['Engine Speed(55)'].sum()
    df3['Percentage'] = (df3['Engine Speed(55)'] / grand_total3) * 100
    # Create pivot tables for all dataframes
    pivot_table_percentage1 = pd.pivot_table(df1,values='Percentage',index='Bin', aggfunc='sum').reset_index()
    pivot_table_percentage2 = pd.pivot_table(df2,index='Bin',values='Percentage', aggfunc='sum').reset_index()
    pivot_table_percentage3 = pd.pivot_table(df3, index='Bin',values='Percentage', aggfunc='sum').reset_index()
    # Merge the pivot tables
    merged_pivot_table = pivot_table_percentage1.merge(pivot_table_percentage2, on='Bin')
    merged_pivot_table = merged_pivot_table.merge(pivot_table_percentage3, on='Bin')
    # Assuming you have a 'df' DataFrame for plotting
    # Convert the DataFrame from wide to long format
    df_melt = merged_pivot_table.melt(id_vars='Bin', var_name='VIN Numbers', value_name='Percentage')
    # Create a grouped bar chart using Plotly Express
    fig = px.bar(df_melt, x='Bin', y='Percentage', color='VIN Numbers', barmode='group',
                 color_discrete_sequence = custom_colors)
    fig.update_xaxes(title_text='Engine Speed (rpm)')
    fig.update_layout(title='Engine RPM Utilization')
    # Show the combined figure using Streamlit
    st.plotly_chart(fig)
    
    
    #---------------------------------------------------------------------------------
    # VEHICLE SPEED UTILIZATION [VIN-1 vs VIN-2 vs VIN-3]
    # Define the bins with duplicates and then remove duplicates using set()
    bins = [0, 10, 20, 30, 40, 50, 60, 70, df1['Wheel-Based Vehicle Speed(54)'].max()]
    bins = list(set(bins))
    bins.sort()
    labels = ['0-10', '10-20', '20-30', '30-40', '40-50', '50-60', '60-70', '70-80']
    # Calculate percentages for df1
    df1['Bin'] = pd.cut(df1['Wheel-Based Vehicle Speed(54)'], bins=bins, labels=labels)
    grand_total1 = df1['Wheel-Based Vehicle Speed(54)'].sum()
    df1['Percentage'] = (df1['Wheel-Based Vehicle Speed(54)'] / grand_total1) * 100
    # Calculate percentages for df2
    df2['Bin'] = pd.cut(df2['Wheel-Based Vehicle Speed(54)'], bins=bins, labels=labels)
    grand_total2 = df2['Wheel-Based Vehicle Speed(54)'].sum()
    df2['Percentage'] = (df2['Wheel-Based Vehicle Speed(54)'] / grand_total2) * 100
    # Calculate percentages for df3
    df3['Bin'] = pd.cut(df3['Wheel-Based Vehicle Speed(54)'], bins=bins, labels=labels)
    grand_total3 = df3['Wheel-Based Vehicle Speed(54)'].sum()
    df3['Percentage'] = (df3['Wheel-Based Vehicle Speed(54)'] / grand_total3) * 100
    # Create pivot tables for all dataframes
    pivot_table_percentage1 = pd.pivot_table(df1,values='Percentage', index='Bin', aggfunc='sum').reset_index()
    pivot_table_percentage2 = pd.pivot_table(df2,values='Percentage',  index='Bin', aggfunc='sum').reset_index()
    pivot_table_percentage3 = pd.pivot_table(df3,values='Percentage', index='Bin', aggfunc='sum').reset_index()
    # Merge the pivot tables on the 'Bin' column
    merged_pivot_table = pivot_table_percentage1.merge(pivot_table_percentage2, on='Bin')
    merged_pivot_table = merged_pivot_table.merge(pivot_table_percentage3, on='Bin')
    # Convert the DataFrame from wide to long format
    df_melt = merged_pivot_table.melt(id_vars='Bin', var_name='VIN Numbers', value_name='Percentage')
    # Create a grouped bar chart using Plotly Express
    fig = px.bar(df_melt, x='Bin', y='Percentage', text=df_melt['Percentage'].round(2), color='VIN Numbers', barmode='group',
                 color_discrete_sequence = custom_colors)
    fig.update_xaxes(title_text='Wheel-Based Vehicle Speed (kmph)')
    fig.update_layout(title='Vehicle Speed Utilization')
    # Show the combined figure using Streamlit
    st.plotly_chart(fig)


    #---------------------------------------------------------------------------------
    # ENGINE TORQUE UTILIZATION [VIN-1 vs VIN-2]
    # Define the bins with duplicates and then remove duplicates using set()
    bins = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, df1['Actual Engine - Percent Torque(59)'].max()]
    bins = list(set(bins))
    bins.sort()
    labels = ['1-10', '11-20', '21-30', '31-40', '41-50', '51-60', '61-70', '71-80', '81-90', '91-100']
    # Calculate percentages for df1
    df1['Bin'] = pd.cut(df1['Actual Engine - Percent Torque(59)'], bins=bins, labels=labels)
    grand_total1 = df1['Actual Engine - Percent Torque(59)'].sum()
    df1['Percentage'] = (df1['Actual Engine - Percent Torque(59)'] / grand_total1) * 100
    # Calculate percentages for df2
    df2['Bin'] = pd.cut(df2['Actual Engine - Percent Torque(59)'], bins=bins, labels=labels)
    grand_total2 = df2['Actual Engine - Percent Torque(59)'].sum()
    df2['Percentage'] = (df2['Actual Engine - Percent Torque(59)'] / grand_total2) * 100
    # Calculate percentages for df3
    df3['Bin'] = pd.cut(df3['Actual Engine - Percent Torque(59)'], bins=bins, labels=labels)
    grand_total3 = df3['Actual Engine - Percent Torque(59)'].sum()
    df3['Percentage'] = (df3['Actual Engine - Percent Torque(59)'] / grand_total3) * 100
    # Create pivot tables for all dataframes
    pivot_table_percentage1 = pd.pivot_table(df1,values='Percentage',index='Bin', aggfunc='sum').reset_index()
    pivot_table_percentage2 = pd.pivot_table(df2,values='Percentage',index='Bin', aggfunc='sum').reset_index()
    pivot_table_percentage3 = pd.pivot_table(df3,values='Percentage',index='Bin', aggfunc='sum').reset_index()
    # Merge the pivot tables on the 'Bin' column
    merged_pivot_table = pivot_table_percentage1.merge(pivot_table_percentage2, on='Bin')
    merged_pivot_table = merged_pivot_table.merge(pivot_table_percentage3, on='Bin')
    # Convert the DataFrame from wide to long format
    df_melt = merged_pivot_table.melt(id_vars='Bin', var_name='VIN Numbers', value_name='Percentage')
    # Create a grouped bar chart using Plotly Express
    fig = px.bar(df_melt, x='Bin', y='Percentage', text=df_melt['Percentage'].round(2), color='VIN Numbers', barmode='group',
                 color_discrete_sequence = custom_colors)
    fig.update_xaxes(title_text='Actual Engine - Percent Torque (%)')
    fig.update_layout(title='Engine Torque Utilization')
    # Show the combined figure using Streamlit
    st.plotly_chart(fig)
    
    
    #---------------------------------------------------------------------------------
    # ACCELERATION PEDAL UTILIZATION [VIN-1 vs VIN-2 vs VIN-3]
    # Define the bins with duplicates and then remove duplicates using set()
    bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, df1['Throttle Position(58)'].max()]
    bins = list(set(bins))
    bins.sort()
    labels = ['0-10', '10-20', '20-30', '30-40', '40-50', '50-60', '60-70', '70-80', '80-90', '90-100']
    # Calculate percentages for df1
    df1['Bin'] = pd.cut(df1['Throttle Position(58)'], bins=bins, labels=labels)
    grand_total1 = df1['Throttle Position(58)'].sum()
    # Calculate percentages for df2
    df2['Bin'] = pd.cut(df2['Throttle Position(58)'], bins=bins, labels=labels)
    grand_total2 = df2['Throttle Position(58)'].sum()
    # Calculate percentages for df3
    df3['Bin'] = pd.cut(df3['Throttle Position(58)'], bins=bins, labels=labels)
    grand_total3 = df3['Throttle Position(58)'].sum()
    # Create pivot tables for all dataframes
    pivot_table_percentage1 = pd.pivot_table(df1,values='Percentage',index='Bin', aggfunc='sum').reset_index()
    pivot_table_percentage2 = pd.pivot_table(df2,values='Percentage',index='Bin', aggfunc='sum').reset_index()
    pivot_table_percentage3 = pd.pivot_table(df3,values='Percentage',index='Bin', aggfunc='sum').reset_index()
    # Merge the pivot tables on the 'Bin' column
    # Merge the pivot tables with different suffixes
    merged_pivot_table = pivot_table_percentage1.merge(pivot_table_percentage2, on='Bin')
    merged_pivot_table = merged_pivot_table.merge(pivot_table_percentage3, on='Bin')
    # Convert the DataFrame from wide to long format
    df_melt = merged_pivot_table.melt(id_vars='Bin', var_name='VIN Numbers', value_name='Percentage')
    # Create a grouped bar chart using Plotly Express
    fig = px.bar(df_melt, x='Bin', y='Percentage', text=df_melt['Percentage'].round(2), color='VIN Numbers', barmode='group',
                 color_discrete_sequence = custom_colors)
    fig.update_xaxes(title_text='Throttle Position (%)')
    fig.update_layout(title='Acceleration Pedal Utilization')
    # Show the combined figure using Streamlit
    st.plotly_chart(fig)
    
    
    #---------------------------------------------------------------------------------
    # GEAR UTILIZATION [VIN-1 vs VIN-2 vs VIN-3]
    # Define the labels
    labels = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    # Calculate percentages for df1, df2, and df3
    total_count_1 = df1['Transmission_Current_Gear(99)'].count()
    total_count_2 = df2['Transmission_Current_Gear(99)'].count()
    total_count_3 = df3['Transmission_Current_Gear(99)'].count()
    gear1 = [(df1['Transmission_Current_Gear(99)'] == i).sum() / total_count_1 * 100 for i in range(10)]
    gear2 = [(df2['Transmission_Current_Gear(99)'] == i).sum() / total_count_2 * 100 for i in range(10)]
    gear3 = [(df3['Transmission_Current_Gear(99)'] == i).sum() / total_count_3 * 100 for i in range(10)]
    # Create a DataFrame for the chart
    data = {'Label':labels,'gear1':gear1,'gear2':gear2,'gear3':gear3}
    df = pd.DataFrame(data)
    # Convert the DataFrame from wide to long format
    df_melt = df.melt(id_vars='Label', var_name='VIN Numbers', value_name='gear')
    # Create the grouped bar chart
    fig = px.bar(df_melt, x='Label', y='gear', text=df_melt['gear'].round(2), color='VIN Numbers', barmode='group',
                 color_discrete_sequence = custom_colors)
    # Set a title for the chart
    fig.update_xaxes(title_text='Transmission_Current_Gear')
    fig.update_layout(title='Gear Utilization')
    # Show the chart using Streamlit
    st.plotly_chart(fig)
    
    #---------------------------------------------------------------------------------
   # ENGINE SPEED vs VEHICLE SPEED [SCATTER PLOT] - VIN 1
    plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
    plt.scatter(df1["Wheel-Based Vehicle Speed(54)"], df1["Engine Speed(55)"], color='crimson', label='VIN-1')
    plt.title('ENGINE SPEED vs VEHICLE SPEED for VIN-1', fontsize=16)
    plt.xlabel('Wheel-Based Vehicle Speed', fontsize=12)
    plt.ylabel('Engine Speed', fontsize=12)
    plt.legend()
    # Show the plot for VIN 1
    plt.savefig('engine speed vs vehicle speed.pdf', format='pdf')

    
    # ENGINE SPEED vs VEHICLE SPEED [SCATTER PLOT] - VIN 2
    plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
    plt.scatter(df2["Wheel-Based Vehicle Speed(54)"], df2["Engine Speed(55)"], color='yellowgreen', label='VIN-2')
    plt.title('ENGINE SPEED vs VEHICLE SPEED for VIN-2', fontsize=16)
    plt.xlabel('Wheel-Based Vehicle Speed', fontsize=12)
    plt.ylabel('Engine Speed', fontsize=12)
    plt.legend()
    # Show the plot for VIN 2
    plt.savefig('engine speed vs vehicle speed1.pdf', format='pdf')

       
       # ENGINE SPEED vs VEHICLE SPEED [SCATTER PLOT] - VIN 3
    plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
    plt.scatter(df3["Wheel-Based Vehicle Speed(54)"], df3["Engine Speed(55)"], color='mediumblue', label='VIN-3')
    plt.title('ENGINE SPEED vs VEHICLE SPEED for VIN-3', fontsize=16)
    plt.xlabel('Wheel-Based Vehicle Speed', fontsize=12)
    plt.ylabel('Engine Speed', fontsize=12)
    plt.legend()
    # Show the plot for VIN 3
    plt.savefig('engine speed vs vehicle speed2.pdf', format='pdf')

       
       #---------------------------------------------------------------------------------
       # ENGINE RPM UTILIZATION [VIN-1 vs VIN-2 vs VIN-3]
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
    # Calculate percentages for df3
    df3['Bin'] = pd.cut(df3['Engine Speed(55)'], bins=bins, labels=labels)
    grand_total3 = df3['Engine Speed(55)'].sum()
    df3['Percentage_VIN3'] = (df3['Engine Speed(55)'] / grand_total3) * 100
    # Create pivot tables for all dataframes
    pivot_table_percentage1 = pd.pivot_table(df1, values='Percentage_VIN1', index='Bin', aggfunc='sum').reset_index()
    pivot_table_percentage2 = pd.pivot_table(df2, values='Percentage_VIN2', index='Bin', aggfunc='sum').reset_index()
    pivot_table_percentage3 = pd.pivot_table(df3, values='Percentage_VIN3', index='Bin', aggfunc='sum').reset_index()
    # Merge the pivot tables
    merged_pivot_table = pivot_table_percentage1.merge(pivot_table_percentage2, on='Bin')
    merged_pivot_table = merged_pivot_table.merge(pivot_table_percentage3, on='Bin')
    # Set up the figure
    fig, ax = plt.subplots(figsize=(10, 6))    
    # Define the width of each bar
    bar_width = 0.2  # Reduced bar width to fit three bars side by side
    index = range(len(merged_pivot_table))    
    # Create bars for VIN1
    bar1 = ax.bar(index, merged_pivot_table['Percentage_VIN1'], bar_width,color='crimson')    
    # Create bars for VIN2 (staggered by bar_width)
    bar2 = ax.bar([i + bar_width for i in index], merged_pivot_table['Percentage_VIN2'], bar_width, color='yellowgreen')    
    # Create bars for VIN3 (staggered by 2 * bar_width)
    bar3 = ax.bar([i + 2 * bar_width for i in index], merged_pivot_table['Percentage_VIN3'], bar_width, color='mediumblue')    
    # Set labels, title, and ticks
    ax.set_xlabel('Bins')
    ax.set_ylabel('Percentage')
    ax.set_title('Engine RPM Utilization')
    ax.set_xticks([i + bar_width for i in index])
    ax.set_xticklabels(merged_pivot_table['Bin'], rotation=45, ha='right') 
    # Add data labels above each bar
    for bars in [bar1, bar2, bar3]:
        for bar, percentage in zip(bars, merged_pivot_table['Percentage_VIN1' if bars == bar1 else('Percentage_VIN2' if bars  == bar2 else 'Percentage_VIN3')]):
            height = bar.get_height()
            ax.annotate(f'{percentage:.2f}',
                        xy=(bar.get_x() + bar.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom', fontsize=6)
    # Add legend
    
    
    ax.legend()
    plt.savefig('Engine RPM Utilization.pdf', format='pdf')
 
    
       #---------------------------------------------------------------------------------
    # VEHICLE SPEED UTILIZATION [VIN-1 vs VIN-2 vs VIN-3]
    # Define the bins with duplicates and then remove duplicates using set()
    bins = [0, 10, 20, 30, 40, 50, 60, 70, df1['Wheel-Based Vehicle Speed(54)'].max()]
    bins = list(set(bins))
    bins.sort()
    labels = ['0-10', '10-20', '20-30', '30-40', '40-50', '50-60', '60-70', '70-80']
    # Calculate percentages for df1
    df1['Bin'] = pd.cut(df1['Wheel-Based Vehicle Speed(54)'], bins=bins, labels=labels)
    grand_total1 = df1['Wheel-Based Vehicle Speed(54)'].sum()
    df1['Percentage_VIN1'] = (df1['Wheel-Based Vehicle Speed(54)'] / grand_total1) * 100
    # Calculate percentages for df2
    df2['Bin'] = pd.cut(df2['Wheel-Based Vehicle Speed(54)'], bins=bins, labels=labels)
    grand_total2 = df2['Wheel-Based Vehicle Speed(54)'].sum()
    df2['Percentage_VIN2'] = (df2['Wheel-Based Vehicle Speed(54)'] / grand_total2) * 100 
    # Calculate percentages for df3
    df3['Bin'] = pd.cut(df3['Wheel-Based Vehicle Speed(54)'], bins=bins, labels=labels)
    grand_total3 = df3['Wheel-Based Vehicle Speed(54)'].sum()
    df3['Percentage_VIN3'] = (df3['Wheel-Based Vehicle Speed(54)'] / grand_total3) * 100
    # Create pivot tables for all dataframes
    pivot_table_percentage1 = pd.pivot_table(df1, values='Percentage_VIN1', index='Bin', aggfunc='sum').reset_index()
    pivot_table_percentage2 = pd.pivot_table(df2, values='Percentage_VIN2', index='Bin', aggfunc='sum').reset_index()
    pivot_table_percentage3 = pd.pivot_table(df3, values='Percentage_VIN3', index='Bin', aggfunc='sum').reset_index()
    # Merge the pivot tables on the 'Bin' column
    merged_pivot_table = pivot_table_percentage1.merge(pivot_table_percentage2, on='Bin')
    merged_pivot_table = merged_pivot_table.merge(pivot_table_percentage3, on='Bin')
    # Set up the figure
    fig, ax = plt.subplots(figsize=(10, 6))    
    # Define the width of each bar
    bar_width = 0.2  # Reduced bar width to fit three bars side by side
    index = range(len(merged_pivot_table))    
    # Create bars for VIN1
    bar1 = ax.bar(index, merged_pivot_table['Percentage_VIN1'], bar_width, color='crimson')    
    # Create bars for VIN2 (staggered by bar_width)
    bar2 = ax.bar([i + bar_width for i in index], merged_pivot_table['Percentage_VIN2'], bar_width, color='yellowgreen')    
    # Create bars for VIN3 (staggered by 2 * bar_width)
    bar3 = ax.bar([i + 2 * bar_width for i in index], merged_pivot_table['Percentage_VIN3'], bar_width, color='mediumblue')    
    # Set labels, title, and ticks
    ax.set_xlabel('Bins')
    ax.set_ylabel('Percentage')
    ax.set_title('Vehicle Speed Utilization')
    ax.set_xticks([i + bar_width for i in index])
    ax.set_xticklabels(merged_pivot_table['Bin'], rotation=45, ha='right') 
    # Add data labels above each bar
    for bars in ([bar1, bar2, bar3]):
        for bar, percentage in zip(bars, merged_pivot_table['Percentage_VIN1' if bars == bar1 else('Percentage_VIN2' if bars  == bar2 else 'Percentage_VIN3')]):
            height = bar.get_height()
            ax.annotate(f'{percentage:.2f}',
                        xy=(bar.get_x() + bar.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom', fontsize=6)
    # Add legend
    ax.legend()
    # Add to pdf (if pdf_pages is defined)
    plt.savefig('Vehicle Speed Utilization.pdf', format='pdf')
    
    #---------------------------------------------------------------------------------
    # ENGINE TORQUE UTILIZATION [VIN-1 vs VIN-2 vs VIN-3]
    # Define the bins with duplicates and then remove duplicates using set()
    bins = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, df1['Actual Engine - Percent Torque(59)'].max()]
    bins = list(set(bins))
    bins.sort()
    labels = ['1-10', '11-20', '21-30', '31-40', '41-50', '51-60', '61-70', '71-80', '81-90', '91-100']
    # Calculate percentages for df1
    df1['Bin'] = pd.cut(df1['Actual Engine - Percent Torque(59)'], bins=bins, labels=labels)
    grand_total1 = df1['Actual Engine - Percent Torque(59)'].sum()
    df1['Percentage_VIN1'] = (df1['Actual Engine - Percent Torque(59)'] / grand_total1) * 100
    # Calculate percentages for df2
    df2['Bin'] = pd.cut(df2['Actual Engine - Percent Torque(59)'], bins=bins, labels=labels)
    grand_total2 = df2['Actual Engine - Percent Torque(59)'].sum()
    df2['Percentage_VIN2'] = (df2['Actual Engine - Percent Torque(59)'] / grand_total2) * 100
    # Calculate percentages for df3
    df3['Bin'] = pd.cut(df3['Actual Engine - Percent Torque(59)'], bins=bins, labels=labels)
    grand_total3 = df3['Actual Engine - Percent Torque(59)'].sum()
    df3['Percentage_VIN3'] = (df3['Actual Engine - Percent Torque(59)'] / grand_total3) * 100
    # Create pivot tables for all dataframes
    pivot_table_percentage1 = pd.pivot_table(df1, values='Percentage_VIN1', index='Bin', aggfunc='sum').reset_index()
    pivot_table_percentage2 = pd.pivot_table(df2, values='Percentage_VIN2', index='Bin', aggfunc='sum').reset_index()
    pivot_table_percentage3 = pd.pivot_table(df3, values='Percentage_VIN3', index='Bin', aggfunc='sum').reset_index()
    # Merge the pivot tables on the 'Bin' column
    merged_pivot_table = pivot_table_percentage1.merge(pivot_table_percentage2, on='Bin')
    merged_pivot_table = merged_pivot_table.merge(pivot_table_percentage3, on='Bin')
    # Set up the figure
    fig, ax = plt.subplots(figsize=(10, 6))    
    # Define the width of each bar
    bar_width = 0.2  # Reduced bar width to fit three bars side by side
    index = range(len(merged_pivot_table))    
    # Create bars for VIN1
    bar1 = ax.bar(index, merged_pivot_table['Percentage_VIN1'], bar_width, color='crimson')    
    # Create bars for VIN2 (staggered by bar_width)
    bar2 = ax.bar([i + bar_width for i in index], merged_pivot_table['Percentage_VIN2'], bar_width, color='yellowgreen')    
    # Create bars for VIN3 (staggered by 2 * bar_width)
    bar3 = ax.bar([i + 2 * bar_width for i in index], merged_pivot_table['Percentage_VIN3'], bar_width, color='mediumblue')    
    # Set labels, title, and ticks
    ax.set_xlabel('Bins')
    ax.set_ylabel('Percentage')
    ax.set_title('Engine Torque Utilization')
    ax.set_xticks([i + bar_width for i in index])
    ax.set_xticklabels(merged_pivot_table['Bin'], rotation=45, ha='right') 
    # Add data labels above each bar
    for bars in ([bar1, bar2, bar3]):
        for bar, percentage in zip(bars, merged_pivot_table['Percentage_VIN1' if bars == bar1 else('Percentage_VIN2' if bars  == bar2 else 'Percentage_VIN3')]):
            height = bar.get_height()
            ax.annotate(f'{percentage:.2f}',
                        xy=(bar.get_x() + bar.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom', fontsize=6)
    # Add legend
    ax.legend()
    plt.savefig('Engine Torque Utilization.pdf', format='pdf')
    
    #---------------------------------------------------------------------------------
    # ACCELERATION PEDAL UTILIZATION [VIN-1 vs VIN-2 vs VIN-3]
    # Define the bins with duplicates and then remove duplicates using set()
    bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, df1['Throttle Position(58)'].max()]
    bins = list(set(bins))
    bins.sort()
    labels = ['0-10', '10-20', '20-30', '30-40', '40-50', '50-60', '60-70', '70-80', '80-90', '90-100']
    # Calculate percentages for df1
    df1['Bin'] = pd.cut(df1['Throttle Position(58)'], bins=bins, labels=labels)
    grand_total1 = df1['Throttle Position(58)'].sum()
    df1['Percentage_VIN1'] = (df1['Throttle Position(58)'] / grand_total1) * 100
    # Calculate percentages for df2
    df2['Bin'] = pd.cut(df2['Throttle Position(58)'], bins=bins, labels=labels)
    grand_total2 = df2['Throttle Position(58)'].sum()
    df2['Percentage_VIN2'] = (df2['Throttle Position(58)'] / grand_total2) * 100
    # Calculate percentages for df3
    df3['Bin'] = pd.cut(df3['Throttle Position(58)'], bins=bins, labels=labels)
    grand_total3 = df3['Throttle Position(58)'].sum()
    df3['Percentage_VIN3'] = (df3['Throttle Position(58)'] / grand_total3) * 100
    # Create pivot tables for all dataframes
    pivot_table_percentage1 = pd.pivot_table(df1, values='Percentage_VIN1', index='Bin', aggfunc='sum').reset_index()
    pivot_table_percentage2 = pd.pivot_table(df2, values='Percentage_VIN2', index='Bin', aggfunc='sum').reset_index()
    pivot_table_percentage3 = pd.pivot_table(df3, values='Percentage_VIN3', index='Bin', aggfunc='sum').reset_index()
    # Merge the pivot tables on the 'Bin' column
    # Merge the pivot tables with different suffixes
    merged_pivot_table = pivot_table_percentage1.merge(pivot_table_percentage2, on='Bin')
    merged_pivot_table = merged_pivot_table.merge(pivot_table_percentage3, on='Bin')
    # Set up the figure
    fig, ax = plt.subplots(figsize=(10, 6))    
    # Define the width of each bar
    bar_width = 0.2  # Reduced bar width to fit three bars side by side
    index = range(len(merged_pivot_table))    
    # Create bars for VIN1
    bar1 = ax.bar(index, merged_pivot_table['Percentage_VIN1'], bar_width,color='crimson')    
    # Create bars for VIN2 (staggered by bar_width)
    bar2 = ax.bar([i + bar_width for i in index], merged_pivot_table['Percentage_VIN2'], bar_width, color='yellowgreen')    
    # Create bars for VIN3 (staggered by 2 * bar_width)
    bar3 = ax.bar([i + 2 * bar_width for i in index], merged_pivot_table['Percentage_VIN3'], bar_width,  color='mediumblue')    
    # Set labels, title, and ticks
    ax.set_xlabel('Bins')
    ax.set_ylabel('Percentage')
    ax.set_title('Acceleration Pedal Utilization')
    ax.set_xticks([i + bar_width for i in index])
    ax.set_xticklabels(merged_pivot_table['Bin'], rotation=45, ha='right') 
    # Add data labels above each bar
    for bars in ([bar1, bar2, bar3]):
        for bar, percentage in zip(bars, merged_pivot_table['Percentage_VIN1' if bars == bar1 else('Percentage_VIN2' if bars  == bar2 else 'Percentage_VIN3')]):
            height = bar.get_height()
            ax.annotate(f'{percentage:.2f}',
                        xy=(bar.get_x() + bar.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom', fontsize=6)
    # Add legend
    ax.legend()
    # Add to pdf (if pdf_pages is defined)
    plt.savefig('Acceleration Pedal Utilization.pdf', format='pdf')
    #---------------------------------------------------------------------------------
    # GEAR UTILIZATION [VIN-1 vs VIN-2 vs VIN-3]
    # Define the labels
    labels = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    # Calculate percentages for df1, df2, and df3
    total_count_1 = df1['Transmission_Current_Gear(99)'].count()
    total_count_2 = df2['Transmission_Current_Gear(99)'].count()
    total_count_3 = df3['Transmission_Current_Gear(99)'].count()
    gear1 = [(df1['Transmission_Current_Gear(99)'] == i).sum() / total_count_1 * 100 for i in range(10)]
    gear2 = [(df2['Transmission_Current_Gear(99)'] == i).sum() / total_count_2 * 100 for i in range(10)]
    gear3 = [(df3['Transmission_Current_Gear(99)'] == i).sum() / total_count_3 * 100 for i in range(10)]
    # Create a DataFrame for the chart
    data = {'Label': labels, 'gear_VIN1': gear1,  'gear_VIN2': gear2,  'gear_VIN3': gear3}
    df = pd.DataFrame(data)
    # Create the grouped bar chart using Matplotlib
    fig, ax = plt.subplots(figsize=(10, 6))
    width = 0.2  # Reduced bar width to fit three bars side by side
    x = np.arange(len(labels))
    bar1 = ax.bar(x - width, df['gear_VIN1'], width, color='crimson')
    bar2 = ax.bar(x, df['gear_VIN2'], width, color='yellowgreen')
    bar3 = ax.bar(x + width, df['gear_VIN3'], width, color='mediumblue')
    ax.set_xlabel('Transmission_Current_Gear')
    ax.set_ylabel('Percentage')
    ax.set_title('Gear Utilization')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    # Add percentage labels on top of the bars
    for bars in ([bar1, bar2, bar3]):
        for bar, percentage in zip(bars, df['gear_VIN1' if bars == bar1 else('gear_VIN2' if bars  == bar2 else 'gear_VIN3')]):
            height = bar.get_height()
            ax.annotate(f'{percentage:.2f}%', xy=(bar.get_x() + bar.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom', fontsize=6)
    # Add legend without '_nolegend_'
    ax.legend(loc='upper left')
    plt.savefig('Gear Utilization.pdf', format='pdf')
    
    
    merger.append('Engine RPM Utilization.pdf')
    merger.append('engine speed vs vehicle speed.pdf')
    merger.append('engine speed vs vehicle speed1.pdf')
    merger.append('engine speed vs vehicle speed2.pdf')
    merger.append('Vehicle Speed Utilization.pdf')
    merger.append('Engine Torque Utilization.pdf')
    merger.append('Acceleration Pedal Utilization.pdf')
    merger.append('Gear Utilization.pdf')
    
    
    # Save the merged PDF as a single file
    merger.write('merged_plots.pdf')
    
