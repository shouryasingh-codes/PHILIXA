import joblib

model = joblib.load("philixa_model.pkl")
scaler = joblib.load("scaler.pkl")
user_input = [[20, 5.2, 0.7, 3.1, 4, 1]]
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