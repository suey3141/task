import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
from typing import Dict, List, Any

def scrape_survivor_data() -> List[Dict[str, Any]]:
    """Scrape Survivor show data from Wikipedia."""
    url = "https://en.wikipedia.org/wiki/Survivor_(American_TV_series)"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    seasons_data = []
    # Find the seasons table
    tables = soup.find_all('table', class_='wikitable')
    
    for table in tables:
        if 'Season' in table.text and 'Winner' in table.text:
            rows = table.find_all('tr')[1:]  # Skip header row
            for row in rows:
                cols = row.find_all(['td', 'th'])
                if len(cols) >= 6:
                    season_data = {
                        'Season': cols[0].text.strip(),
                        'Year': cols[1].text.strip(),
                        'Winner': cols[2].text.strip(),
                        'Runner_up': cols[3].text.strip(),
                        'Location': cols[4].text.strip(),
                        'Contestants': cols[5].text.strip() if len(cols) > 5 else 'N/A',
                        'Viewership': cols[6].text.strip() if len(cols) > 6 else 'N/A'
                    }
                    seasons_data.append(season_data)
    
    return seasons_data

def scrape_american_idol_data() -> List[Dict[str, Any]]:
    """Scrape American Idol show data from Wikipedia."""
    url = "https://en.wikipedia.org/wiki/American_Idol"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    seasons_data = []
    # Find the seasons table
    tables = soup.find_all('table', class_='wikitable')
    
    for table in tables:
        if 'Season' in table.text and 'Winner' in table.text:
            rows = table.find_all('tr')[1:]  # Skip header row
            for row in rows:
                cols = row.find_all(['td', 'th'])
                if len(cols) >= 5:
                    season_data = {
                        'Season': cols[0].text.strip(),
                        'Year': cols[1].text.strip(),
                        'Winner': cols[2].text.strip(),
                        'Runner_up': cols[3].text.strip(),
                        'Judges': cols[4].text.strip() if len(cols) > 4 else 'N/A',
                        'Contestants': cols[5].text.strip() if len(cols) > 5 else 'N/A',
                        'Viewership': cols[6].text.strip() if len(cols) > 6 else 'N/A'
                    }
                    seasons_data.append(season_data)
    
    return seasons_data

def main():
    # Scrape data
    survivor_data = scrape_survivor_data()
    idol_data = scrape_american_idol_data()
    
    # Convert to DataFrames
    survivor_df = pd.DataFrame(survivor_data)
    idol_df = pd.DataFrame(idol_data)
    
    # Save to CSV files
    survivor_df.to_csv('survivor_data.csv', index=False)
    idol_df.to_csv('american_idol_data.csv', index=False)
    
    print("Datasets have been created successfully!")

if __name__ == "__main__":
    main()