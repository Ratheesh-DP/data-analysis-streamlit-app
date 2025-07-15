import pandas as pd
import streamlit as st
import numpy as np

def calculate_demographic_data(df, print_data=True):
    """
    Analyze demographic data using Pandas to answer specific questions.
    
    Args:
        df (DataFrame): The demographic data
        print_data (bool): Whether to print results to console
        
    Returns:
        dict: Dictionary containing all calculated statistics
    """
    
    # How many of each race are represented in this dataset?
    race_count = df["race"].value_counts()
    
    # What is the average age of men?
    average_age_men = round(df.loc[df["sex"] == "Male", "age"].mean(), 1)
    
    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round(
        100 * len(df.loc[df["education"] == "Bachelors"]) / len(df), 1
    )
    
    # What percentage of people with advanced education make more than 50K?
    # What percentage of people without advanced education make more than 50K?
    
    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df.loc[
        df["education"].isin(["Bachelors", "Masters", "Doctorate"])
    ]
    lower_education = df.loc[
        ~df["education"].isin(["Bachelors", "Masters", "Doctorate"])
    ]
    
    # percentage with salary >50K
    higher_education_rich = round(
        100 * len(higher_education.loc[higher_education["salary"] == ">50K"]) / len(higher_education), 1
    )
    
    lower_education_rich = round(
        100 * len(lower_education.loc[lower_education["salary"] == ">50K"]) / len(lower_education), 1
    )
    
    # What is the minimum number of hours a person works per week?
    min_work_hours = df["hours-per-week"].min()
    
    # What percentage of people who work minimum hours have salary >50K?
    num_min_workers = df.loc[df["hours-per-week"] == min_work_hours]
    rich_percentage = round(
        100 * len(num_min_workers.loc[num_min_workers["salary"] == ">50K"]) / len(num_min_workers), 1
    )
    
    # What country has the highest percentage of people that earn >50K?
    country_stats = df.groupby("native-country").apply(
        lambda x: 100 * len(x[x["salary"] == ">50K"]) / len(x)
    ).sort_values(ascending=False)
    
    highest_earning_country = country_stats.index[0]
    highest_earning_country_percentage = round(country_stats.iloc[0], 1)
    
    # Most popular occupation for those who earn >50K in India
    india_rich = df.loc[(df["native-country"] == "India") & (df["salary"] == ">50K")]
    if len(india_rich) > 0:
        top_IN_occupation = india_rich["occupation"].value_counts().index[0]
    else:
        top_IN_occupation = "No data"
    
    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)
    
    return {
        "race_count": race_count,
        "average_age_men": average_age_men,
        "percentage_bachelors": percentage_bachelors,
        "higher_education_rich": higher_education_rich,
        "lower_education_rich": lower_education_rich,
        "min_work_hours": min_work_hours,
        "rich_percentage": rich_percentage,
        "highest_earning_country": highest_earning_country,
        "highest_earning_country_percentage": highest_earning_country_percentage,
        "top_IN_occupation": top_IN_occupation,
    }

def load_sample_data():
    """Create sample demographic data for demonstration."""
    np.random.seed(42)
    
    # Sample data structure based on the census dataset
    sample_data = {
        'age': np.random.randint(17, 90, 1000),
        'workclass': np.random.choice(['Private', 'Self-emp-not-inc', 'State-gov', 'Federal-gov'], 1000),
        'education': np.random.choice(['Bachelors', 'HS-grad', 'Masters', 'Doctorate', '11th', 'Some-college'], 1000),
        'marital-status': np.random.choice(['Never-married', 'Married-civ-spouse', 'Divorced', 'Widowed'], 1000),
        'occupation': np.random.choice(['Prof-specialty', 'Exec-managerial', 'Adm-clerical', 'Sales'], 1000),
        'relationship': np.random.choice(['Not-in-family', 'Husband', 'Wife', 'Own-child'], 1000),
        'race': np.random.choice(['White', 'Black', 'Asian-Pac-Islander', 'Amer-Indian-Eskimo', 'Other'], 1000, 
                                p=[0.85, 0.10, 0.03, 0.015, 0.005]),
        'sex': np.random.choice(['Male', 'Female'], 1000),
        'capital-gain': np.random.randint(0, 10000, 1000),
        'capital-loss': np.random.randint(0, 1000, 1000),
        'hours-per-week': np.random.randint(1, 80, 1000),
        'native-country': np.random.choice(['United-States', 'India', 'Iran', 'Cuba', 'Mexico'], 1000, 
                                         p=[0.89, 0.04, 0.02, 0.03, 0.02]),
        'salary': np.random.choice(['<=50K', '>50K'], 1000, p=[0.76, 0.24])
    }
    
    return pd.DataFrame(sample_data)

def display_data_overview(df):
    """Display overview of the dataset."""
    st.subheader("Dataset Overview")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Records", len(df))
    with col2:
        st.metric("Number of Features", len(df.columns))
    with col3:
        st.metric("Salary >50K", f"{len(df[df['salary'] == '>50K']) / len(df) * 100:.1f}%")
    
    # Show sample data
    st.subheader("Sample Data")
    st.dataframe(df.head(10), use_container_width=True)

def display_analysis_results(results):
    """Display the demographic analysis results in an organized format."""
    st.subheader("Demographic Analysis Results")
    
    # Create tabs for different categories
    tab1, tab2, tab3, tab4 = st.tabs(["Demographics", "Education & Income", "Work Patterns", "Geographic Analysis"])
    
    with tab1:
        st.write("**Race Distribution:**")
        race_df = pd.DataFrame({
            'Race': results['race_count'].index,
            'Count': results['race_count'].values,
            'Percentage': (results['race_count'].values / results['race_count'].sum() * 100).round(1)
        })
        st.dataframe(race_df, use_container_width=True)
        
        st.write(f"**Average Age of Men:** {results['average_age_men']} years")
    
    with tab2:
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric("Bachelor's Degree Holders", f"{results['percentage_bachelors']}%")
            st.metric("Higher Education >50K Earners", f"{results['higher_education_rich']}%")
        
        with col2:
            st.metric("Lower Education >50K Earners", f"{results['lower_education_rich']}%")
            
        # Education comparison chart
        education_data = pd.DataFrame({
            'Education Level': ['Higher Education', 'Lower Education'],
            'Percentage Earning >50K': [results['higher_education_rich'], results['lower_education_rich']]
        })
        st.bar_chart(education_data.set_index('Education Level'))
    
    with tab3:
        st.metric("Minimum Work Hours per Week", f"{results['min_work_hours']} hours")
        st.write(f"**Percentage of minimum-hour workers earning >50K:** {results['rich_percentage']}%")
        
        if results['rich_percentage'] > 0:
            st.info(f"Even among those working the fewest hours ({results['min_work_hours']} hours/week), {results['rich_percentage']}% still earn more than $50K")
        else:
            st.info("None of the people working minimum hours earn more than $50K")
    
    with tab4:
        st.write(f"**Highest Earning Country:** {results['highest_earning_country']}")
        st.write(f"**Percentage earning >50K:** {results['highest_earning_country_percentage']}%")
        
        st.write(f"**Most Popular Occupation in India (>50K earners):** {results['top_IN_occupation']}")

def main():
    st.title("Demographic Data Analyzer")
    st.write("Analyze census demographic data using pandas")
    
    # Educational content
    with st.expander("ℹ️ About This Analysis"):
        st.write("""
        This analyzer examines demographic data from the 1994 Census database to answer key questions about:
        
        - **Demographics**: Race distribution and age patterns
        - **Education**: Impact of education level on income
        - **Work Patterns**: Hours worked and earning potential
        - **Geography**: Country-wise earning patterns
        
        The analysis uses pandas to process and analyze the data, providing insights into income inequality and demographic patterns.
        """)
    
    # Data source options
    st.subheader("Data Source")
    
    data_option = st.radio(
        "Choose data source:",
        ["Use Sample Data", "Upload CSV File"],
        help="Sample data demonstrates the analyzer with generated census-like data"
    )
    
    df = None
    
    if data_option == "Use Sample Data":
        if st.button("Load Sample Data", type="primary"):
            with st.spinner("Generating sample demographic data..."):
                df = load_sample_data()
                st.success("✅ Sample data loaded successfully!")
    
    elif data_option == "Upload CSV File":
        uploaded_file = st.file_uploader(
            "Upload demographic data CSV",
            type=['csv'],
            help="File should contain columns: age, workclass, education, race, sex, hours-per-week, native-country, salary, etc."
        )
        
        if uploaded_file is not None:
            try:
                df = pd.read_csv(uploaded_file)
                st.success("✅ File uploaded successfully!")
                
                # Validate required columns
                required_columns = ['age', 'education', 'race', 'sex', 'hours-per-week', 'native-country', 'salary']
                missing_columns = [col for col in required_columns if col not in df.columns]
                
                if missing_columns:
                    st.error(f"❌ Missing required columns: {', '.join(missing_columns)}")
                    df = None
                    
            except Exception as e:
                st.error(f"❌ Error loading file: {str(e)}")
    
    # Perform analysis if data is available
    if df is not None:
        # Display data overview
        display_data_overview(df)
        
        # Perform analysis
        with st.spinner("Performing demographic analysis..."):
            try:
                results = calculate_demographic_data(df, print_data=False)
                
                # Display results
                display_analysis_results(results)
                
                # Raw results for developers
                with st.expander("🔧 Raw Analysis Results (JSON)"):
                    # Convert race_count series to dict for JSON display
                    raw_results = results.copy()
                    raw_results['race_count'] = results['race_count'].to_dict()
                    st.json(raw_results)
                
                st.success("✅ Analysis completed successfully!")
                
            except Exception as e:
                st.error(f"❌ Analysis failed: {str(e)}")
                st.write("Please ensure your data has the correct format and column names.")
    
    # Footer
    st.write("---")
    st.write("Built with Streamlit and Pandas for demographic data analysis")

if __name__ == "__main__":
    main()