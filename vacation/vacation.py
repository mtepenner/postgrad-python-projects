import json
import os
from datetime import datetime

class GlobalVacationEngine:
    def __init__(self, home_airport: str, energy_state: str, budget_tier: str):
        self.home_airport = home_airport.upper()
        self.energy_state = energy_state.lower()
        self.budget_tier = budget_tier.lower()

    def _simulate_api_fetch(self) -> dict:
        """
        Simulates fetching global data based on user constraints.
        """
        if self.energy_state == "wiped" and self.budget_tier in ["splurge", "high"]:
            return {
                "destination": "Maldives (North Malé Atoll)",
                "vibe": "Ultimate Passive Recovery",
                "logistics": {
                    "departure": self.home_airport,
                    "arrival": "MLE (Velana International Airport)",
                    "transportation": "Speedboat or Seaplane transfer directly to resort (No car rental needed)."
                },
                "lodging": "Gili Lankanfushi (Overwater Villas)",
                "dining": ["Kashiveli (Beachfront dining)", "By the Sea (Japanese fine dining)"],
                "itinerary": [
                    f"Day 1: Depart {self.home_airport}, arrive MLE, seaplane transfer.",
                    "Day 2: Complete rest. In-villa dining and Ayurvedic spa treatments.",
                    "Day 3: Sunset dolphin cruise, otherwise zero obligations.",
                    "Day 4: Depart MLE and begin the journey home."
                ]
            }
        elif self.energy_state == "wired" and self.budget_tier in ["value", "low"]:
            return {
                "destination": "Oaxaca City, Mexico",
                "vibe": "High-Stimulation Cultural Immersion",
                "logistics": {
                    "departure": self.home_airport,
                    "arrival": "OAX (Xoxocotlán International)",
                    "transportation": "Walkable city center; local taxis for ruins."
                },
                "lodging": "Boutique Airbnb in Centro Histórico",
                "dining": ["Mercado 20 de Noviembre (Street food)", "Boulenc (Bakery/Cafe)", "Los Danzantes (Upscale regional)"],
                "itinerary": [
                    f"Day 1: Fly from {self.home_airport} to OAX. Evening mezcal tasting.",
                    "Day 2: Early morning trip to Monte Albán ruins. Afternoon exploring markets.",
                    "Day 3: Full day cooking class and exploring artisan villages.",
                    "Day 4: Morning coffee in the plaza, fly home."
                ]
            }
        else:
            return {
                "destination": "Reykjavik, Iceland",
                "vibe": "Balanced Nature Exploration",
                "logistics": {
                    "departure": self.home_airport,
                    "arrival": "KEF (Keflavík International)",
                    "transportation": "4x4 SUV Rental at KEF (Essential for winter/remote areas)"
                },
                "lodging": "Ion Adventure Hotel",
                "dining": ["Matur og Drykkur", "Bæjarins Beztu Pylsur (Famous hot dogs)"],
                "itinerary": [
                    f"Day 1: Fly out of {self.home_airport}, arrive KEF. Blue Lagoon soak on the way to the hotel.",
                    "Day 2: Drive the Golden Circle at your own pace.",
                    "Day 3: Glacier hiking or simply watching the Northern Lights from the hotel.",
                    "Day 4: Return rental car to KEF, fly home."
                ]
            }

    def generate_and_save_report(self):
        """Fetches the data, formats it beautifully, and saves it to a text file."""
        print("\nGenerating your custom global itinerary...")
        trip_data = self._simulate_api_fetch()
        
        report = []
        report.append("="*50)
        report.append(f" YOUR PRESCRIPTION VACATION ")
        report.append("="*50)
        report.append(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append(f"Home Base: {self.home_airport}")
        report.append(f"Energy State: {self.energy_state.capitalize()}")
        report.append(f"Budget Tier: {self.budget_tier.capitalize()}\n")
        
        report.append(f"DESTINATION: {trip_data['destination']}")
        report.append(f"VIBE: {trip_data['vibe']}\n")
        
        report.append("--- LOGISTICS ---")
        for key, val in trip_data['logistics'].items():
            report.append(f"* {key.capitalize()}: {val}")
        
        report.append("\n--- ACCOMMODATIONS & DINING ---")
        report.append(f"* Lodging: {trip_data['lodging']}")
        report.append(f"* Dining Highlights: {', '.join(trip_data['dining'])}")
        
        report.append("\n--- RECOMMENDED ITINERARY ---")
        for day in trip_data['itinerary']:
            report.append(day)
            
        report.append("="*50)
        
        final_text = "\n".join(report)
        
        # Static filename as requested
        filename = "vacation.txt"
        
        try:
            with open(filename, "w", encoding="utf-8") as file:
                file.write(final_text)
            print(f"Success! Your itinerary has been saved to your current directory as: {filename}\n")
        except Exception as e:
            print(f"Error saving file: {e}\n")

# --- Interactive Execution Block ---
if __name__ == "__main__":
    print("="*50)
    print(" WELCOME TO THE GLOBAL VACATION ENGINE ")
    print("="*50)
    print("Let's find exactly where you need to go.\n")
    
    # 1. Ask for the airport
    user_airport = input("Enter your 3-letter home airport code (e.g., PDX, LAX, JFK): ").strip()
    
    # 2. Ask for energy state with validation
    user_energy = ""
    while user_energy not in ["wired", "wiped"]:
        user_energy = input("At the end of a long week, are you 'wired' or 'wiped'? ").strip().lower()
        if user_energy not in ["wired", "wiped"]:
            print("  -> Invalid input. Please type 'wired' or 'wiped'.")
            
    # 3. Ask for budget with validation
    user_budget = ""
    while user_budget not in ["splurge", "value"]:
        user_budget = input("Is your budget a 'splurge' or are you looking for 'value'? ").strip().lower()
        if user_budget not in ["splurge", "value"]:
            print("  -> Invalid input. Please type 'splurge' or 'value'.")
    
    # Run the engine
    engine = GlobalVacationEngine(user_airport, user_energy, user_budget)
    engine.generate_and_save_report()
