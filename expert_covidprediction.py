def covid_expert_system():
    print("COVID-19 Prediction Expert System")
    print("---------------------------------")

    # Symptoms questions
    fever = input("Do you have a fever? (yes/no): ").strip().lower()
    cough = input("Do you have a persistent cough? (yes/no): ").strip().lower()
    fatigue = input("Do you feel fatigue? (yes/no): ").strip().lower()
    taste_loss = input("Have you experienced loss of taste or smell? (yes/no): ").strip().lower()
    difficulty_breathing = input("Do you have difficulty breathing? (yes/no): ").strip().lower()
    travel_history = input("Have you traveled to a high-risk area recently? (yes/no): ").strip().lower()
    contact_history = input("Have you been in contact with a confirmed COVID-19 case? (yes/no): ").strip().lower()

    # Rule-based analysis
    symptoms = [fever, cough, fatigue, taste_loss, difficulty_breathing]
    high_risk_factors = [travel_history, contact_history]

    symptom_score = symptoms.count("yes")
    risk_score = high_risk_factors.count("yes")

    # Predictions
    if symptom_score >= 3 and risk_score >= 1:
        print("\nPrediction: High likelihood of COVID-19. Please get tested and consult a doctor immediately.")
    elif symptom_score >= 3:
        print("\nPrediction: Moderate likelihood of COVID-19. Consider getting tested.")
    elif symptom_score >= 1 or risk_score >= 1:
        print("\nPrediction: Low likelihood of COVID-19, but monitor your symptoms closely.")
    else:
        print("\nPrediction: Unlikely to have COVID-19. Stay safe and follow health guidelines.")


# Run the system
if __name__ == "__main__":
    covid_expert_system()
