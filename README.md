Multi-Purpose Data Analysis Web Application
A comprehensive Streamlit-based web application that provides two distinct data analysis tools for statistical calculations and demographic analysis.

Features
🧮 Mean-Variance-Standard Deviation Calculator
Transforms 9 numbers into statistical analysis of a 3x3 matrix
Calculates mean, variance, standard deviation, max, min, and sum
Provides analysis along different axes (columns, rows, flattened)
Interactive input with quick example buttons
Visual matrix representation with pandas DataFrame
📊 Demographic Data Analyzer
Analyzes census demographic data using pandas
Supports CSV file upload or sample data generation
Comprehensive analysis including:
Race distribution and demographics
Education level impact on income
Work patterns and hour analysis
Geographic earning patterns
Occupation analysis by region
Live Demo
🌐 Try the Application

Installation
Clone this repository:
git clone <your-repo-url>
cd <repo-name>
Install dependencies:
pip install streamlit numpy pandas
Run the application:
streamlit run app.py --server.port 5000
Usage
Matrix Calculator
Select "Mean-Variance-Standard Deviation Calculator" from the sidebar
Enter 9 numbers separated by commas (e.g., 0,1,2,3,4,5,6,7,8)
Use quick example buttons for testing
View the 3x3 matrix representation and statistical results
Demographic Analyzer
Select "Demographic Data Analyzer" from the sidebar
Choose between sample data or upload your own CSV file
View comprehensive demographic analysis with interactive charts
Explore different analysis categories through tabs
Project Structure
├── app.py                    # Main Streamlit application
├── demographic_analyzer.py   # Demographic analysis module
├── .streamlit/
│   └── config.toml          # Streamlit configuration
├── pyproject.toml           # Project dependencies
└── README.md                # Project documentation
Technical Details
Matrix Calculator
Input: List of 9 numbers
Processing: NumPy array reshaping and statistical calculations
Output: Comprehensive statistics along multiple axes
Validation: Input validation with error handling
Demographic Analyzer
Data Processing: Pandas-based analysis
Sample Data: Generates realistic census-like data for testing
Analysis Questions:
Race representation in dataset
Average age demographics
Education level statistics
Income correlation with education
Work hour patterns
Geographic income distribution
Requirements
Python 3.11+
Streamlit
NumPy
Pandas
Configuration
The application is configured to run on 0.0.0.0:5000 for deployment compatibility. Configuration is managed through .streamlit/config.toml.

Development
Adding New Features
For matrix calculator: Modify functions in app.py
For demographic analyzer: Update demographic_analyzer.py
Add navigation options in the main sidebar
Testing
Use the provided sample data for demographic analysis
Test matrix calculator with various number combinations
Verify error handling with invalid inputs
Contributing
Fork the repository
Create a feature branch
Make your changes
Test thoroughly
Submit a pull request
