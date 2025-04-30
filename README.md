# 🚚 Vehicle Mileage Analyzer Module

**Advanced KMPL Comparison Dashboard for Commercial Vehicles**

## Overview

The Vehicle Mileage Analyzer Module is a comprehensive tool designed to compare the mileage performance of 2 to 4 vehicles. This dashboard provides detailed analytics and visualizations to help understand vehicle performance factors affecting fuel efficiency.

## Key Features

- ✅ **Multi-Vehicle Comparison**: Compare between 2 to 4 vehicles simultaneously
- 📊 **Comprehensive Analysis**: Evaluate multiple performance factors affecting mileage
- 🔍 **Band-wise Engine Analysis**: Engine Speed vs Vehicle Speed scatter plots with operational bands
- 📈 **Performance Factors**: Analysis of GSAS compliance, coasting, neutral driving, and more
- 💾 **Exportable Reports**: Download analysis in PDF format and data in Excel
- 💻 **User-friendly Interface**: Built with Streamlit for easy navigation
- 🛠️ **Configurable Parameters**: Select vehicle type, gearbox type, and RAR values

## Performance Factors Analyzed

The system analyzes the following key performance indicators:

- GSAS Compliance
- Coasting distance
- Neutral driving hours
- Engine hours
- Engine RPM Utilization
- Vehicle Speed Utilization
- Engine Torque Utilization
- Acceleration Pedal Utilization
- Gear Utilization

## Software Requirements

- Python 3.x
- Required modules:
  - streamlit
  - pandas
  - numpy
  - reportlab
  - os
  - plotly.express
  - matplotlib
  - PyPDF2

## Project Structure

```
vehicle_mileage_analyzer/
├── kmpl_dashboard.py          # Main application file
├── graphs_for_2_VIN.py        # Plotting functions for 2 vehicles
├── graphs_for_3_VIN.py        # Plotting functions for 3 vehicles
├── graphs_for_4_VIN.py        # Plotting functions for 4 vehicles
├── report_for_2_VIN.py        # PDF report generation for 2 vehicles
├── report_for_3_VIN.py        # PDF report generation for 3 vehicles
├── report_for_4_VIN.py        # PDF report generation for 4 vehicles
└── band_wise_scatter_plot.py  # Band-wise scatter plot functions
```

## How to Access and Use the Application

### Opening the Application

For first-time users:
1. Make sure Python 3.x is installed on your system
2. Install required packages using: `pip install streamlit pandas numpy reportlab plotly matplotlib PyPDF2`
3. Clone the repository: `git clone https://github.com/shwetam2004/kmpl_dashbaord_al.git`
4. Navigate to project directory: `cd kmpl_dashbaord_al`
5. Run the application: `streamlit run kmpl_dashboard.py`
6. Access the dashboard in your web browser at `http://localhost:8501`

For returning users:
1. Navigate to the project directory: `cd path/to/kmpl_dashbaord_al`
2. Run the application: `streamlit run kmpl_dashboard.py`
3. Access the dashboard in your browser at `http://localhost:8501`

### Using the Dashboard

1. **Select Configuration**:
   - Choose the number of vehicles to compare (2, 3, or 4)
   - Select vehicle type
   - Select gearbox type
   - Enter RAR value

2. **Upload Vehicle Data**:
   - Upload raw data files for each vehicle
   - Enter VIN numbers for all vehicles

3. **View Analysis**:
   - The dashboard will generate performance metrics
   - Band-wise scatter plots show Engine Speed vs. Vehicle Speed
   - Color-coded bands indicate optimal and suboptimal operating zones

4. **Export Results**:
   - Download complete analysis as PDF report
   - Export data tables in Excel format

5. **Review Recommendations**:
   - The system provides suggestions for vehicles operating in yellow or red bands
   - Follow recommendations to improve vehicle mileage performance

### Dashboard Features

- **Multiple Vehicle Comparison**: Side-by-side analysis makes it easy to spot performance differences
- **Intuitive Visualizations**: Color-coded graphs help identify issues quickly
- **Detailed Performance Metrics**: Comprehensive analysis of factors affecting fuel efficiency
- **Actionable Insights**: Clear recommendations for improving vehicle performance

## Repository

GitHub link: https://github.com/shwetam2004/kmpl_dashbaord_al.git Commercial Vehicles**

## Overview

The Vehicle Mileage Analyzer Module is a comprehensive tool designed to compare the mileage performance of 2 to 4 vehicles. This dashboard provides detailed analytics and visualizations to help understand vehicle performance factors affecting fuel efficiency.

## Key Features

- ✅ **Multi-Vehicle Comparison**: Compare between 2 to 4 vehicles simultaneously
- 📊 **Comprehensive Analysis**: Evaluate multiple performance factors affecting mileage
- 🔍 **Band-wise Engine Analysis**: Engine Speed vs Vehicle Speed scatter plots with operational bands
- 📈 **Performance Factors**: Analysis of GSAS compliance, coasting, neutral driving, and more
- 💾 **Exportable Reports**: Download analysis in PDF format and data in Excel
- 💻 **User-friendly Interface**: Built with Streamlit for easy navigation
- 🛠️ **Configurable Parameters**: Select vehicle type, gearbox type, and RAR values

## Performance Factors Analyzed

The system analyzes the following key performance indicators:

- GSAS Compliance
- Coasting distance
- Neutral driving hours
- Engine hours
- Engine RPM Utilization
- Vehicle Speed Utilization
- Engine Torque Utilization
- Acceleration Pedal Utilization
- Gear Utilization
