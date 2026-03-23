def comprehensive_city_matcher():
    # Database Attributes:
    # 1. Warm Winters (SAD prevention)
    # 2. Affordable (Financial stress reduction)
    # 3. Nature Access (Green space for mental health)
    # 4. Coastal (Ocean proximity)
    # 5. Walkable (Incidental exercise & social collision)
    # 6. Relaxed Pace (Burnout prevention)
    # 7. Top Healthcare (Access to medical/mental health professionals)
    # 8. LGBTQ+ Friendly / Progressive (Belonging and safety)
    # 9. Low Noise/Crowds (Sensory overload prevention)
    # 10. Strong Job Market (Economic security)
    # 11. High Sunshine Year-Round (Mood regulation)
    # 12. Strong Arts/Culture (Mental stimulation/community)

    # 1 = True/High, 0 = False/Low
    cities = {
        # --- MAJOR HUBS ---
        "New York, NY":       [0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1],
        "Los Angeles, CA":    [1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1],
        "Chicago, IL":        [0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1],
        "San Francisco, CA":  [1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1],
        "Seattle, WA":        [0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
        "Boston, MA":         [0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1],
        "Denver, CO":         [0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0],
        "Austin, TX":         [1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1],
        "Atlanta, GA":        [1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1],
        "Miami, FL":          [1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1],
        
        # --- MID-SIZE & RELAXED MAJOR CITIES ---
        "Portland, OR":       [0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1],
        "San Diego, CA":      [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
        "Honolulu, HI":       [1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0],
        "Minneapolis, MN":    [0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
        "Salt Lake City, UT": [0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0],
        "Raleigh, NC":        [1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0],
        "Madison, WI":        [0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],

        # --- SMALLER / RELAXED COASTAL CITIES ---
        "Santa Barbara, CA":  [1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1],
        "Monterey, CA":       [1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0],
        "Portland, ME":       [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1],
        "Charleston, SC":     [1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1],
        "Savannah, GA":       [1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1],
        "Wilmington, NC":     [1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0],
        "St. Petersburg, FL": [1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1],
        "Key West, FL":       [1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1],
        "Newport, RI":        [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1],
        "Cape May, NJ":       [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
        "Galveston, TX":      [1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0],
        "Virginia Beach, VA": [1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0],
        "Providence, RI":     [0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
        "New Orleans, LA":    [1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1],
        "Anchorage, AK":      [0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0],
    }

    # Questions mapped directly to the traits array above
    questions = [
        "1. Does harsh winter weather or a lack of sunlight negatively impact your mood? (Warm Winters)",
        "2. Does a high cost of living cause you significant daily anxiety? (Affordable)",
        "3. Do you need immediate access to deep nature (forests, mountains) to decompress? (Nature Access)",
        "4. Is living right on or very close to the ocean essential to your peace of mind? (Coastal)",
        "5. Do you hate driving and prefer a community where you can walk or transit everywhere? (Walkable)",
        "6. Do you prefer a relaxed, slow-paced lifestyle over a 'hustle culture' environment? (Relaxed Pace)",
        "7. Is having top-tier hospitals and a high density of mental health professionals crucial? (Top Healthcare)",
        "8. Do you strongly prefer a politically progressive, highly inclusive, or LGBTQ+ friendly community? (Progressive)",
        "9. Are you sensitive to sensory overload and prefer a quiet area away from massive crowds? (Low Noise/Crowds)",
        "10. Is having a highly competitive, massive corporate job market important to you? (Strong Job Market)",
        "11. Do you need almost year-round sunshine to thrive mentally? (High Sunshine)",
        "12. Do you rely on a vibrant arts, music, and cultural scene to feel socially connected? (Strong Arts/Culture)"
    ]

    print("\n" + "="*50)
    print("   THE HOLISTIC CITY & MENTAL HEALTH MATCHER")
    print("="*50)
    print("Answer 'y' or 'n' to the following questions to find your ideal environment.\n")

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
    
    print("\nOther highly compatible cities for your well-being:")
    for city, match in results[1:6]:
        print(f"- {city}: {match}% Match")

if __name__ == "__main__":
    comprehensive_city_matcher()
