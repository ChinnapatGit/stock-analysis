import pandas as pd

def analyze_stock_data(input_file, output_file):
    try:
        # Read stock data from CSV
        data = pd.read_csv(input_file)
        
        # Ensure required columns exist
        if 'Date' not in data.columns or 'Close' not in data.columns:
            raise ValueError("CSV file must contain 'Date' and 'Close' columns.")
        
        # Convert Date column to datetime
        data['Date'] = pd.to_datetime(data['Date'])
        
        # Calculate daily price change
        data['Daily Change'] = data['Close'].diff()
        
        # Calculate average closing price
        avg_close = data['Close'].mean()
        
        # Find the highest and lowest closing prices
        highest_close = data['Close'].max()
        lowest_close = data['Close'].min()
        
        # Write analysis results to a file
        with open(output_file, 'w') as file:
            file.write("Market Analysis Results\n")
            file.write("=======================\n")
            file.write(f"Average Closing Price: {avg_close:.2f}\n")
            file.write(f"Highest Closing Price: {highest_close:.2f}\n")
            file.write(f"Lowest Closing Price: {lowest_close:.2f}\n")
            file.write("\nDaily Price Changes:\n")
            file.write(data[['Date', 'Daily Change']].to_string(index=False))
        
        print(f"Analysis complete. Results saved to {output_file}.")
    except Exception as e:
        print(f"An error occurred: {e}")

# File paths
input_csv = "stock_data.csv"
output_txt = "market_analysis.txt"

# Run analysis
analyze_stock_data(input_csv, output_txt)
