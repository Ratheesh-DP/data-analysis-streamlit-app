import streamlit as st
import numpy as np
import pandas as pd
from demographic_analyzer import main as demographic_main, calculate_demographic_data

def calculate(list_input):
    """
    Calculate mean, variance, standard deviation, max, min, and sum
    for a 3x3 matrix along different axes.
    
    Args:
        list_input (list): List of 9 numbers
        
    Returns:
        dict: Dictionary containing statistical calculations
        
    Raises:
        ValueError: If input doesn't contain exactly 9 numbers
    """
    if len(list_input) != 9:
        raise ValueError("List must contain nine numbers.")
    
    # Convert to numpy array and reshape to 3x3 matrix
    matrix = np.array(list_input).reshape(3, 3)
    
    # Calculate statistics
    calculations = {
        'mean': [
            matrix.mean(axis=0).tolist(),  # mean of columns
            matrix.mean(axis=1).tolist(),  # mean of rows
            matrix.mean().tolist()         # mean of flattened
        ],
        'variance': [
            matrix.var(axis=0).tolist(),   # variance of columns
            matrix.var(axis=1).tolist(),   # variance of rows
            matrix.var().tolist()          # variance of flattened
        ],
        'standard deviation': [
            matrix.std(axis=0).tolist(),   # std dev of columns
            matrix.std(axis=1).tolist(),   # std dev of rows
            matrix.std().tolist()          # std dev of flattened
        ],
        'max': [
            matrix.max(axis=0).tolist(),   # max of columns
            matrix.max(axis=1).tolist(),   # max of rows
            matrix.max().tolist()          # max of flattened
        ],
        'min': [
            matrix.min(axis=0).tolist(),   # min of columns
            matrix.min(axis=1).tolist(),   # min of rows
            matrix.min().tolist()          # min of flattened
        ],
        'sum': [
            matrix.sum(axis=0).tolist(),   # sum of columns
            matrix.sum(axis=1).tolist(),   # sum of rows
            matrix.sum().tolist()          # sum of flattened
        ]
    }
    
    return calculations

def parse_input(input_string):
    """
    Parse comma-separated input string into list of numbers.
    
    Args:
        input_string (str): Comma-separated numbers
        
    Returns:
        list: List of float numbers
        
    Raises:
        ValueError: If input cannot be parsed or doesn't contain 9 numbers
    """
    try:
        # Split by comma and convert to float
        numbers = [float(x.strip()) for x in input_string.split(',')]
        return numbers
    except ValueError as e:
        raise ValueError("Please enter valid numbers separated by commas.")

def display_matrix(numbers):
    """Display the 3x3 matrix in a formatted way."""
    matrix = np.array(numbers).reshape(3, 3)
    
    # Create a DataFrame for better display
    df = pd.DataFrame(matrix, 
                     columns=['Column 0', 'Column 1', 'Column 2'],
                     index=['Row 0', 'Row 1', 'Row 2'])
    
    st.subheader("3x3 Matrix Representation")
    st.dataframe(df, use_container_width=True)

def display_results(calculations):
    """Display the statistical calculations in an organized format."""
    st.subheader("Statistical Analysis Results")
    
    # Create tabs for different views
    tab1, tab2 = st.tabs(["Detailed Results", "Summary Table"])
    
    with tab1:
        for stat_name, values in calculations.items():
            st.write(f"**{stat_name.title()}:**")
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.write("*Axis 0 (Columns):*")
                st.write(values[0])
            
            with col2:
                st.write("*Axis 1 (Rows):*")
                st.write(values[1])
            
            with col3:
                st.write("*Flattened:*")
                st.write(values[2])
            
            st.write("---")
    
    with tab2:
        # Create a summary DataFrame
        summary_data = []
        for stat_name, values in calculations.items():
            summary_data.append({
                'Statistic': stat_name.title(),
                'Axis 0 (Columns)': str(values[0]),
                'Axis 1 (Rows)': str(values[1]),
                'Flattened': str(values[2])
            })
        
        summary_df = pd.DataFrame(summary_data)
        st.dataframe(summary_df, use_container_width=True)

def main():
    # App selection
    st.sidebar.title("Choose Application")
    app_choice = st.sidebar.radio(
        "Select an application:",
        ["Mean-Variance-Standard Deviation Calculator", "Demographic Data Analyzer"]
    )
    
    if app_choice == "Mean-Variance-Standard Deviation Calculator":
        matrix_calculator_app()
    else:
        demographic_main()

def matrix_calculator_app():
    st.title("Mean-Variance-Standard Deviation Calculator")
    st.write("Transform 9 numbers into statistical analysis of a 3x3 matrix")
    
    # Educational content
    with st.expander("ℹ️ How it works"):
        st.write("""
        This calculator takes 9 numbers and arranges them into a 3x3 matrix, then calculates various statistics:
        
        - **Axis 0 (Columns)**: Calculations performed down the columns (vertically)
        - **Axis 1 (Rows)**: Calculations performed across the rows (horizontally) 
        - **Flattened**: Calculations performed on all 9 numbers as a single array
        
        **Statistics calculated:**
        - Mean: Average value
        - Variance: Measure of spread from the mean
        - Standard Deviation: Square root of variance
        - Max: Maximum value
        - Min: Minimum value
        - Sum: Total of all values
        """)
    
    # Example section
    with st.expander("📝 Example"):
        st.write("""
        **Input:** `0, 1, 2, 3, 4, 5, 6, 7, 8`
        
        **Matrix:**
        ```
        [0, 1, 2]
        [3, 4, 5]
        [6, 7, 8]
        ```
        
        **Example Results:**
        - Mean axis 0 (columns): [3.0, 4.0, 5.0] (average of each column)
        - Mean axis 1 (rows): [1.0, 4.0, 7.0] (average of each row)
        - Mean flattened: 4.0 (average of all numbers)
        """)
    
    # Input section
    st.subheader("Input")
    input_text = st.text_input(
        "Enter 9 numbers separated by commas:",
        placeholder="e.g., 0, 1, 2, 3, 4, 5, 6, 7, 8",
        help="Enter exactly 9 numbers separated by commas"
    )
    
    # Quick example buttons
    st.write("**Quick Examples:**")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("Sequential (0-8)"):
            st.session_state.example_input = "0, 1, 2, 3, 4, 5, 6, 7, 8"
    
    with col2:
        if st.button("Random Example"):
            st.session_state.example_input = "1, 5, 3, 9, 2, 8, 4, 7, 6"
    
    with col3:
        if st.button("All Same"):
            st.session_state.example_input = "5, 5, 5, 5, 5, 5, 5, 5, 5"
    
    # Use example input if button was clicked
    if 'example_input' in st.session_state:
        input_text = st.session_state.example_input
        # Clear the session state to allow manual editing
        del st.session_state.example_input
        st.rerun()
    
    # Calculate button and results
    if st.button("Calculate Statistics", type="primary") or input_text:
        if input_text:
            try:
                # Parse input
                numbers = parse_input(input_text)
                
                # Validate exactly 9 numbers
                if len(numbers) != 9:
                    st.error(f"Please enter exactly 9 numbers. You entered {len(numbers)} numbers.")
                    return
                
                # Display the matrix
                display_matrix(numbers)
                
                # Calculate statistics
                results = calculate(numbers)
                
                # Display results
                display_results(results)
                
                # Success message
                st.success("✅ Calculations completed successfully!")
                
            except ValueError as e:
                st.error(f"❌ Error: {str(e)}")
            except Exception as e:
                st.error(f"❌ An unexpected error occurred: {str(e)}")
        else:
            st.info("👆 Please enter 9 numbers to get started")
    
    # Reset button
    if st.button("Reset"):
        st.rerun()
    
    # Footer
    st.write("---")
    st.write("Built with Streamlit and NumPy")

if __name__ == "__main__":
    main()
