import csv
import os

def load_cities_from_csv(filename="cities.csv"):
    cities = {}
    
    # Check if file exists before trying to open it
    if not os.path.exists(filename):
        print(f"Error: Could not find '{filename}'.")
        print("Please ensure the CSV file is in the same folder as this script.")
        return None

    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            city_name = row['City']
            # Convert the string values from the CSV into integers
            traits = [
                int(row['Warm Winters']),
                int(row['Affordable']),
                int(row['Nature Access']),
                int(row['Coastal']),
                int(row['Walkable']),
                int(row['Relaxed Pace']),
                int(row['Top Healthcare']),
                int(row['Progressive']),
                int(row['Low Noise']),
                int(row['Strong Job Market']),
                int(row['High Sunshine']),
                int(row['Strong Arts'])
            ]
            cities[city_name] = traits
            
    return cities

def comprehensive_city_matcher():
    # Load the data from the CSV file
    cities = load_cities_from_csv()
    if not cities:
        return # Stop the script if the CSV didn't load

    questions = [
        "1. Does harsh winter weather or a lack of sunlight negatively impact your mood? (Warm Winters)",
        "2. Does a high cost of living cause you significant daily anxiety? (Affordable)",
        "3. Do you need immediate access to deep nature (forests, mountains) to decompress? (Nature Access)",
        "4. Is living right on or very close to the ocean essential to your peace of mind? (Coastal)",
        "5. Do you hate driving and prefer a community where you can walk or transit everywhere? (Walkable)",
        "6. Do you prefer a relaxed, slow-paced lifestyle over a 'hustle culture' environment? (Relaxed Pace)",
        "7. Is having top-tier hospitals and a high density of mental health professionals crucial? (Top Healthcare)",
        "8. Do you strongly prefer a politically progressive, highly inclusive community? (Progressive)",
        "9. Are you sensitive to sensory overload and prefer a quiet area away from massive crowds? (Low Noise)",
        "10. Is having a highly competitive, massive corporate job market important to you? (Strong Job Market)",
        "11. Do you need almost year-round sunshine to thrive mentally? (High Sunshine)",
        "12. Do you rely on a vibrant arts, music, and cultural scene to feel socially connected? (Strong Arts)"
    ]

    print("\n" + "="*50)
    print("   THE CSV-POWERED CITY & MENTAL HEALTH MATCHER")
    print("="*50)
    print("Answer 'y' or 'n' to the following questions.\n")

    user_prefs = []
    for q in questions:
        while True:
            ans = input(f"{q} (y/n): ").lower().strip()
            if ans in ['y', 'n']:
                user_prefs.append(1 if ans == 'y' else 0)
                break
            print("Please answer with just 'y' or 'n'.")

    # Scoring mechanism
    results = []
    total_factors = len(user_prefs)
    
    for city, traits in cities.items():
        score = sum(1 for i in range(total_factors) if traits[i] == user_prefs[i])
        match_percentage = round((score / total_factors) * 100)
        results.append((city, match_percentage))

    # Sort results by highest match percentage
    results.sort(key=lambda x: x[1], reverse=True)

    print("\n" + "="*50)
    print(f"🌟 YOUR TOP MATCH: {results[0][0]} ({results[0][1]}% Match)")
    print("="*50)
    
    print("\nOther highly compatible cities:")
    for city, match in results[1:6]: # Show top 5 runner-ups
        print(f"- {city}: {match}% Match")

if __name__ == "__main__":
    comprehensive_city_matcher()
