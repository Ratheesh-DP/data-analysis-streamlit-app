# Multi-Purpose Data Analysis Web Application

## Overview

This is a Streamlit-based web application that provides two distinct data analysis tools:

1. **Mean-Variance-Standard Deviation Calculator**: Performs statistical calculations on 3x3 matrices from 9 input numbers
2. **Demographic Data Analyzer**: Analyzes census demographic data using pandas to answer specific questions about demographics, education, income, and geographic patterns

The application uses a sidebar navigation system to switch between the two tools.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Frontend Architecture
- **Framework**: Streamlit - A Python-based web framework for creating data applications
- **Navigation**: Sidebar-based application selection system
- **User Interface**: Two distinct web interfaces:
  1. Matrix calculator with input forms and result visualization
  2. Demographic analyzer with data upload/sample data and comprehensive analysis dashboard
- **Rendering**: Server-side rendering with automatic UI updates

### Backend Architecture
- **Language**: Python 3.11
- **Application Structure**: Multi-app architecture with modular components
- **Core Logic**: 
  1. Statistical calculation functions for 3x3 matrices
  2. Demographic data analysis using pandas operations
- **Data Processing**: 
  - NumPy for matrix operations and statistical calculations
  - Pandas for demographic data manipulation and analysis
- **Modular Design**: Separate modules for different applications (demographic_analyzer.py)

### Data Processing Pipeline
1. User inputs 9 numbers through the Streamlit interface
2. Input validation ensures exactly 9 numbers are provided
3. Numbers are converted to a NumPy array and reshaped into a 3x3 matrix
4. Statistical calculations are performed along different axes:
   - Axis 0: Column-wise calculations
   - Axis 1: Row-wise calculations
   - Flattened: Overall matrix calculations

## Key Components

### Application 1: Matrix Statistical Calculator

#### Statistical Calculator (`calculate` function)
- **Purpose**: Core computational logic for matrix statistics
- **Input**: List of 9 numbers
- **Output**: Dictionary containing statistical measures
- **Error Handling**: Validates input length and raises ValueError for invalid inputs

#### Statistical Measures
- Mean: Average values along axes and flattened
- Variance: Measure of data spread
- Standard Deviation: Square root of variance
- Maximum: Largest values
- Minimum: Smallest values
- Sum: Total values along axes and flattened

### Application 2: Demographic Data Analyzer

#### Core Analysis Function (`calculate_demographic_data`)
- **Purpose**: Performs comprehensive demographic analysis on census data
- **Input**: Pandas DataFrame with demographic data
- **Output**: Dictionary containing analysis results
- **Features**: Race distribution, education-income correlation, work patterns, geographic analysis

#### Analysis Categories
- **Demographics**: Race distribution and age patterns by gender
- **Education & Income**: Bachelor's degree prevalence, education level impact on income
- **Work Patterns**: Minimum work hours analysis, income correlation with hours worked
- **Geographic Analysis**: Country-wise earning patterns, occupation analysis by region

## Data Flow

1. **Input Collection**: Streamlit interface collects 9 numerical values from user
2. **Validation**: Function validates that exactly 9 numbers are provided
3. **Matrix Conversion**: List is converted to 3x3 NumPy matrix
4. **Statistical Processing**: Calculations performed along columns, rows, and entire matrix
5. **Result Display**: Results formatted and displayed in Streamlit interface

## External Dependencies

### Core Libraries
- **Streamlit**: Web application framework for creating the user interface
- **NumPy**: Numerical computing library for matrix operations and statistical calculations
- **Pandas**: Data manipulation library (imported but not actively used in current implementation)

### Deployment Considerations
- Python 3.x runtime required
- Dependencies managed through standard Python package management
- Streamlit provides built-in development server for local testing

## Deployment Strategy

### Development Environment
- Streamlit development server for local testing and development
- Hot reloading for rapid development cycles

### Production Deployment
- Can be deployed on platforms supporting Python web applications
- Streamlit Cloud, Heroku, or similar platforms are suitable options
- Requires minimal configuration due to Streamlit's simplicity

## Implementation Notes

### Current State
- The application appears to be partially implemented
- The `calculate` function is complete but the Streamlit UI integration is not shown in the provided code
- The statistical calculations are comprehensive, covering multiple axes and measures

### Architecture Decisions
1. **Streamlit Choice**: Selected for rapid development and ease of creating data-focused web applications
2. **NumPy Integration**: Chosen for efficient matrix operations and built-in statistical functions
3. **3x3 Matrix Constraint**: Specific requirement that shapes the entire application logic
4. **Axis-based Calculations**: Provides comprehensive statistical analysis from different perspectives

### Potential Enhancements
- Complete Streamlit UI implementation
- Error handling for non-numeric inputs
- Input validation for better user experience
- Result visualization with charts or graphs
- Export functionality for calculated results