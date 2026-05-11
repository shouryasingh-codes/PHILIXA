import joblib

model = joblib.load("philixa_model.pkl")
scaler = joblib.load("scaler.pkl")
user_input = [[20, 4.7, 0.8, 1, 2, 1]]
scaled_input = scaler.transform(user_input)
prediction = model.predict(scaled_input)
probability = model.predict_proba(scaled_input)
print(prediction)
print(probability)
if prediction[0] == 1:
    print("Answer Quality: Good")

else:
    print("Answer Quality: Needs Improvement")

confidence = probability[0][1]

if confidence > 0.8:
    print("Excellent confidence")

elif confidence > 0.6:
    print("Moderate confidence")

else:
    print("Low confidence")


def generate_feedback(word_count,avg_word_length,strong_verbs_count,grammar_error_count):

    feedback = []

    if word_count<18:
        feedback.append( "Try explaining your answer in more detail.")

    if avg_word_length< 4.5:
        feedback.append("Use more descriptive vocabulary")


    if strong_verbs_count == 0:
        feedback.append("Use stronger action-oriented words.")

    if grammar_error_count >= 2:
        feedback.append( "Your answer contains multiple grammar issues.")
    elif grammar_error_count == 1:
        feedback.append( "Small grammar improvement possible.")
    return feedback






word_count = user_input[0][0]
avg_word_length = user_input[0][1]
strong_verbs_count = user_input[0][4]
grammar_error_count = user_input[0][5]

# Generate feedback
feedback = generate_feedback(
    word_count,
    avg_word_length,
    strong_verbs_count,
    grammar_error_count
)
if len(feedback) == 0:
    print("Your answer is well structured.")
else:
    print("\nFeedback:")

    for item in feedback:
        print("-", item)