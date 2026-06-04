"""
Travel Weather Planner
Determines whether commuting is possible based on weather conditions, 
travel distance, and available transportation methods.
"""

# 1. Define the required variables with user input
try:
    distance_mi = float(input("Enter distance in miles: "))
except ValueError:
    # If the user types text or leaves it blank, default to 0 to trigger the invalid check
    distance_mi = 0.0                                        

is_raining = input("Is it raining? (yes/no): ").strip().lower() == "yes"                       
has_bike = input("Do you have a bike? (yes/no): ").strip().lower() == "yes"                      
has_car = input("Do you have a car? (yes/no): ").strip().lower() == "yes"                        
has_ride_share_app = input("Do you have a ride-share app? (yes/no): ").strip().lower() == "yes"  

# 2. Evaluate commuting feasibility
if distance_mi <= 0:
    # Safely catches 0, empty inputs, text typos, or negative miles
    print(False)

elif distance_mi <= 1:
    # Distance is 1 mile or less: Commute possible if it's not raining
    if not is_raining:
        print(True)
    else:
        print(False)

elif distance_mi <= 6:
    # Distance is between 1 and 6 miles: Commute possible if user has a bike and it's not raining
    if has_bike and not is_raining:
        print(True)
    else:
        print(False)

else:
    # Distance is greater than 6 miles: Commute possible if user has a car or a ride-share app
    if has_car or has_ride_share_app:
        print(True)
    else:
        print(False)
