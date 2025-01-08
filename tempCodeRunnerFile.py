from collections import Counter
import math

def naive_bayes_classifier(training_data, test_data):
    """
    Implements a simple Naïve Bayes classifier.

    Parameters:
        training_data: List of tuples where each tuple contains features and a label.
        test_data: List of feature values for the test instance.
    
    Returns:
        Predicted label for the test instance.
    """
    # Separate data by class
    class_data = {}
    for features, label in training_data:
        if label not in class_data:
            class_data[label] = []
        class_data[label].append(features)

    # Calculate prior probabilities and likelihoods
    priors = {}
    likelihoods = {}
    total_samples = len(training_data)

    for label, samples in class_data.items():
        priors[label] = len(samples) / total_samples
        feature_counts = Counter()
        for sample in samples:
            feature_counts.update(sample)
        
        total_features = sum(feature_counts.values())
        likelihoods[label] = {
            feature: (feature_counts[feature] + 1) / (total_features + len(feature_counts))
            for feature in feature_counts
        }

    # Calculate posterior probabilities
    posteriors = {}
    for label in priors:
        posteriors[label] = math.log(priors[label])  # Start with log prior
        for feature in test_data:
            likelihood = likelihoods[label].get(feature, 1e-6)
            posteriors[label] += math.log(likelihood)

    # Return the label with the highest posterior probability
    return max(posteriors, key=posteriors.get)


def calculate_accuracy(training_data, test_data):
    """
    Calculates the accuracy of the model using test data.

    Parameters:
        training_data: List of tuples for training the model.
        test_data: List of tuples where each tuple contains features and the true label.

    Returns:
        Accuracy of the model as a percentage.
    """
    correct_predictions = 0
    for features, true_label in test_data:
        predicted_label = naive_bayes_classifier(training_data, features)
        if predicted_label == true_label:
            correct_predictions += 1

    accuracy = (correct_predictions / len(test_data)) * 100
    return accuracy


# Example training data (symptoms and condition)
training_data = [
    (["fever", "cough", "fatigue"], "condition"),
    (["fever", "cough"], "condition"),
    (["cough", "sneezing"], "no_condition"),
    (["sneezing", "runny_nose"], "no_condition"),
    (["fever", "fatigue"], "condition"),
]

# Test data for accuracy calculation
test_data = [
    (["fever", "cough"], "condition"),
    (["cough", "sneezing"], "no_condition"),
    (["fever", "fatigue"], "condition"),
    (["sneezing", "runny_nose"], "no_condition"),
    (["fever", "sneezing"], "no_condition"),
]

# Ask user for symptoms
print("Disease Prediction System")
print("-------------------------")
print("Please answer 'yes' or 'no' to the following questions:")

symptoms = ["fever", "cough", "fatigue", "sneezing", "runny_nose"]
user_symptoms = []

for symptom in symptoms:
    response = input(f"Do you have {symptom}? ").strip().lower()
    if response == "yes":
        user_symptoms.append(symptom)

# Predict using the Naïve Bayes classifier
predicted_label = naive_bayes_classifier(training_data, user_symptoms)

# Output result
if predicted_label == "condition":
    print("\nPrediction: The individual is likely to have the disease.")
else:
    print("\nPrediction: The individual is unlikely to have the disease.")

# Calculate and display accuracy
accuracy = calculate_accuracy(training_data, test_data)
print(f"\nModel Accuracy: {accuracy:.2f}%")
