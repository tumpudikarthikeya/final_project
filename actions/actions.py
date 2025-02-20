# import json
# from rasa_sdk import Action

# class ActionRecommendMeal(Action):
#     def name(self):
#         return "action_recommend_meal"

#     def run(self, dispatcher, tracker, domain):
#         # Open file in append mode and write logs manually
#         with open("actions_log.txt", "a") as log_file:
#             log_file.write("🔍 Action `action_recommend_meal` triggered!\n")

#         diabetes_level = tracker.get_slot("diabetes_level")
#         day = tracker.get_slot("day")
#         meal_type = tracker.get_slot("meal_type")
#         meal_time = tracker.get_slot("meal_time")

#         # Log extracted slot values
#         with open("actions_log.txt", "a") as log_file:
#             log_file.write(f"🔹 Extracted Slots - Diabetes Level: {diabetes_level}, Day: {day}, Meal Type: {meal_type}, Meal Time: {meal_time}\n")

#         try:
#             with open("in_data.json") as file:
#                 meals = json.load(file)
#                 with open("actions_log.txt", "a") as log_file:
#                     log_file.write("✅ Successfully loaded `in_data.json`\n")
#         except Exception as e:
#             with open("actions_log.txt", "a") as log_file:
#                 log_file.write(f"❌ Failed to load `in_data.json`. Error: {e}\n")
#             dispatcher.utter_message("Sorry, I couldn't retrieve meal recommendations right now.")
#             return []

#         # Fetch meal recommendation
#         if diabetes_level in meals and day in meals[diabetes_level]:
#             if meal_time in meals[diabetes_level][day]:
#                 if meal_type in meals[diabetes_level][day][meal_time]:
#                     meal_options = meals[diabetes_level][day][meal_time][meal_type]
#                     meal_suggestions = ", ".join(meal_options)
#                     response = f"For {diabetes_level} diabetes on {day}, {meal_time} ({meal_type}) options are: {meal_suggestions}."
#                     with open("actions_log.txt", "a") as log_file:
#                         log_file.write(f"✅ Debug: Meal Recommendation Found: {response}\n")
#                 else:
#                     response = f"❌ No {meal_time} options available for {meal_type} on {day}."
#             else:
#                 response = f"❌ No meal data found for {meal_time} on {day}."
#         else:
#             response = "❌ No meal recommendations available for your request."

#         # Log final response
#         with open("actions_log.txt", "a") as log_file:
#             log_file.write(f"✅ Final Response: {response}\n")

#         dispatcher.utter_message(text=response)
#         return []
import json
from rasa_sdk import Action

class ActionRecommendMeal(Action):
    def name(self):
        return "action_recommend_meal"

    def run(self, dispatcher, tracker, domain):
        # Open file in append mode and write logs manually
        # with open("actions_log.txt", "a") as log_file:
        #     log_file.write("🔍 Action `action_recommend_meal` triggered!\n")

        diabetes_level = tracker.get_slot("diabetes_level")
        day = tracker.get_slot("day")
        meal_type = tracker.get_slot("meal_type")
        meal_time = tracker.get_slot("meal_time")

        # Log extracted slot values
        # with open("actions_log.txt", "a") as log_file:
        #     log_file.write(f"🔹 Extracted Slots - Diabetes Level: {diabetes_level}, Day: {day}, Meal Type: {meal_type}, Meal Time: {meal_time}\n")

        try:
            with open("in_data.json") as file:
                meals = json.load(file)
                # with open("actions_log.txt", "a") as log_file:
                #     log_file.write("✅ Successfully loaded `in_data.json`\n")
        except Exception as e:
            # with open("actions_log.txt", "a") as log_file:
            #     log_file.write(f"❌ Failed to load `in_data.json`. Error: {e}\n")
            dispatcher.utter_message("Sorry, I couldn't retrieve meal recommendations right now.")
            return []

        # Fetch meal recommendation
        if diabetes_level in meals and day in meals[diabetes_level]:
            if meal_time in meals[diabetes_level][day]:
                if meal_type in meals[diabetes_level][day][meal_time]:
                    meal_options = meals[diabetes_level][day][meal_time][meal_type]
                    meal_suggestions = "\n ".join(meal_options)
                    response = {
                        "status": "success",
                        "message": f"For {diabetes_level} diabetes on {day}, {meal_time} ({meal_type}) options are: {meal_suggestions}."
                    }
                    # with open("actions_log.txt", "a") as log_file:
                    #     log_file.write(f"✅ Debug: Meal Recommendation Found: {response['message']}\n")
                else:
                    response = {
                        "status": "error",
                        "message": f"No {meal_time} options available for {meal_type} on {day}."
                    }
            else:
                response = {
                    "status": "error",
                    "message": f"No meal data found for {meal_time} on {day}."
                }
        else:
            response = {
                "status": "error",
                "message": "No meal recommendations available for your request."
            }

        # Log final response
        # with open("actions_log.txt", "a") as log_file:
        #     log_file.write(f"✅ Final Response: {response['message']}\n")

        # Send structured response to the frontend
        dispatcher.utter_message(text=response["message"])
        return []