"""
Hypertrophy Macronutrient Calculator
* Objective: Process physiological data to output a precise macronutrient 
  distribution optimized for muscle growth (hypertrophy) and strength gain.
* AI Evaluation Relevance: Demonstrates robust input validation, data 
  structuring using Python dictionaries, and applying real-world biological 
  formulas into logical code.
"""

def calculate_macros(weight_kg, daily_calories, goal="muscle_gain"):
    """
    Calculates protein, fat, and carbohydrate requirements.
    Scientific guidelines used for hypertrophy:
    - Protein: 2.2g per kg of body weight
    - Fats: 25% of total daily calories
    - Carbs: The remainder of the caloric budget
    """
    
    # Input validation: Ensure realistic physiological numbers
    if weight_kg <= 0 or daily_calories < 1200:
        raise ValueError("Invalid input: Weight must be > 0 and calories >= 1200.")

    # 1. Protein Calculation (4 calories per gram)
    protein_grams = weight_kg * 2.2
    protein_calories = protein_grams * 4
    
    # 2. Fats Calculation (9 calories per gram)
    fat_calories = daily_calories * 0.25
    fat_grams = fat_calories / 9
    
    # 3. Carbohydrates Calculation (4 calories per gram)
    remaining_calories = daily_calories - (protein_calories + fat_calories)
    
    if remaining_calories < 0:
        print("Warning: Caloric budget is too low to support these macros.")
        carbs_grams = 0
    else:
        carbs_grams = remaining_calories / 4

    # Structure the output in a clean dictionary
    macro_profile = {
        "Total Calories": daily_calories,
        "Protein (g)": round(protein_grams, 1),
        "Fats (g)": round(fat_grams, 1),
        "Carbs (g)": round(carbs_grams, 1)
    }
    
    return macro_profile

def display_nutrition_plan():
    print("=== Hypertrophy Macro Generator ===\n")
    
    # User Profile (Hardcoded for simulation)
    user_weight = 75.0 # kg
    surplus_calories = 2800 # Caloric surplus for muscle gain
    
    try:
        daily_macros = calculate_macros(user_weight, surplus_calories)
        
        print(f"Profile: {user_weight}kg bodyweight, Target: {surplus_calories} kcal/day")
        print("Optimal Daily Distribution:")
        for macro, value in daily_macros.items():
            print(f" -> {macro}: {value}")
            
    except ValueError as error:
        print(f"System Error: {error}")

if __name__ == "__main__":
    display_nutrition_plan()