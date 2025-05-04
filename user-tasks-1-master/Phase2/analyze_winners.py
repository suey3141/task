import pandas as pd

def count_unique_winners():
    # Read the datasets
    survivor_df = pd.read_csv('survivor_data.csv')
    idol_df = pd.read_csv('american_idol_data.csv')
    
    # Count unique winners up to Survivor's 44th season
    survivor_winners = survivor_df.iloc[:44]['Winner'].nunique()
    idol_winners = idol_df['Winner'].nunique()
    
    # Calculate the difference
    difference = survivor_winners - idol_winners
    
    # Create the result text
    result_text = f"""Unique Winners Analysis (up to Survivor Season 44):
Survivor unique winners: {survivor_winners}
American Idol unique winners: {idol_winners}
Difference (Survivor - American Idol): {difference}
"""
    
    # Write to result.txt
    with open('result.txt', 'w') as f:
        f.write(result_text)
    
    print("Analysis complete! Results written to result.txt")

if __name__ == "__main__":
    count_unique_winners()