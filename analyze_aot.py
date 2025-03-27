import pandas as pd

def analyze_aot_stock_data(input_file, output_file):
    try:
        # Read stock data from CSV
        data = pd.read_csv(input_file)
        
        # Filter data for AOT
        aot_data = data[data['Stock'] == 'AOT']
        
        # Ensure required columns exist
        if 'Date' not in aot_data.columns or 'Close' not in aot_data.columns:
            raise ValueError("CSV file must contain 'Date' and 'Close' columns for AOT.")
        
        # Convert Date column to datetime
        aot_data['Date'] = pd.to_datetime(aot_data['Date'])
        
        # Calculate daily price change
        aot_data['Daily Change'] = aot_data['Close'].diff()
        
        # Calculate average closing price
        avg_close = aot_data['Close'].mean()
        
        # Find the highest and lowest closing prices
        highest_close = aot_data['Close'].max()
        lowest_close = aot_data['Close'].min()
        
        # Write analysis results to a file
        with open(output_file, 'w') as file:
            file.write("AOT Stock Analysis Results\n")
            file.write("===========================\n")
            file.write(f"Average Closing Price: {avg_close:.2f}\n")
            file.write(f"Highest Closing Price: {highest_close:.2f}\n")
            file.write(f"Lowest Closing Price: {lowest_close:.2f}\n")
            file.write("\nDaily Price Changes:\n")
            file.write(aot_data[['Date', 'Daily Change']].to_string(index=False))
        
        print(f"AOT analysis complete. Results saved to {output_file}.")
    except Exception as e:
        print(f"An error occurred: {e}")

# File paths
input_csv = "stock_data.csv"
output_txt = "aot_analysis.txt"

# Run analysis
analyze_aot_stock_data(input_csv, output_txt)