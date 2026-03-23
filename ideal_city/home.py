import csv
import os

def load_cities_from_csv(filename="cities.csv"):
    cities = {}
    if not os.path.exists(filename):
        print(f"Error: Could not find '{filename}'.")
        return None

    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            city_name = row['City']
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
    cities = load_cities_from_csv()
    if not cities:
        return

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
    print("   THE CSV-POWERED CITY MATCHER (DEALBREAKER EDITION)")
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

    # The Dealbreaker Prompt
    print("\n" + "-"*50)
    print("DEALBREAKERS")
    print("Are any of your answers absolute dealbreakers?")
    print("For example, if you answered 'y' to Coastal (Question 4) and you MUST live on the water, type 4.")
    print("If you have multiple, separate them with commas (e.g., 1,4,9). If none, just press Enter.")
    
    db_input = input("\nEnter dealbreaker numbers: ").strip()
    
    dealbreaker_indices = []
    if db_input:
        try:
            # Convert user input like "1, 4, 9" into list indices [0, 3, 8]
            dealbreaker_indices = [int(x.strip()) - 1 for x in db_input.split(',')]
        except ValueError:
            print("Invalid input. Proceeding without dealbreakers...")

    # Scoring & Elimination mechanism
    results = []
    total_factors = len(user_prefs)
    
    for city, traits in cities.items():
        failed_dealbreaker = False
        
        # Check if the city fails any of the user's dealbreakers
        for idx in dealbreaker_indices:
            # Make sure the index is valid (0-11)
            if 0 <= idx < total_factors: 
                if traits[idx] != user_prefs[idx]:
                    failed_dealbreaker = True
                    break
        
        # If it failed a dealbreaker, skip scoring it entirely
        if failed_dealbreaker:
            continue

        # If it survived, calculate the match percentage
        score = sum(1 for i in range(total_factors) if traits[i] == user_prefs[i])
        match_percentage = round((score / total_factors) * 100)
        results.append((city, match_percentage))

    # Sort results by highest match percentage
    results.sort(key=lambda x: x[1], reverse=True)

    print("\n" + "="*50)
    if not results:
        print("❌ NO MATCHES FOUND.")
        print("Your dealbreakers were too strict! No city in the database fit your exact requirements.")
    else:
        print(f"🌟 YOUR TOP MATCH: {results[0][0]} ({results[0][1]}% Match)")
        print("="*50)
        
        if len(results) > 1:
            print("\nOther cities that survived your dealbreakers:")
            # Show up to 10 runner-ups since the list is huge
            for city, match in results[1:11]: 
                print(f"- {city}: {match}% Match")

if __name__ == "__main__":
    comprehensive_city_matcher()
