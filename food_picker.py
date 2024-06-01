import random
def food_selection(weight_category):
    normal_weight_foods = ["Grilled Chicken Salad", "Quinoa and Veggie Bowl", "Salmon with Steamed Vegetables"]
    overweight_level_i_foods = ["Turkey Sandwich on Whole Grain", "Lentil Soup", "Grilled Fish Tacos"]
    overweight_level_ii_foods = ["Vegetable Stir-Fry with Brown Rice", "Chicken and Avocado Salad", "Greek Yogurt with Berries"]
    obesity_type_i_foods=["Quinoa", "barley", "brown rice", "whole wheat pasta"]
    obesity_type_ii_foods=["Whole grain bread", "quinoa", "lentils", "chickpeas", "Brussels sprouts"]
    obesity_type_iii_foods = ["Steamed Broccoli and Carrots", "Baked Chicken Breast", "Mixed Green Salad with Lemon Dressing"]
    if weight_category == "Normal_Weight":
        selected_array = normal_weight_foods
    elif weight_category == "Overweight_Level_I":
        selected_array = overweight_level_i_foods
    elif weight_category == "Overweight_Level_II":
        selected_array = overweight_level_ii_foods
    elif weight_category == "Obesity_Type_I":
        selected_array = obesity_type_i_foods
    elif weight_category == "Obesity_Type_II":
        selected_array = obesity_type_ii_foods
    elif weight_category == "Obesity_Type_III":
        selected_array = obesity_type_iii_foods
    else:
        return "Invalid choice. Please choose a valid weight category."
    selected_food = selected_array
    return selected_food

