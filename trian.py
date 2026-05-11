import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score , classification_report, confusion_matrix
import joblib

# 1. Load data
df = pd.read_csv("featured_data_v9.csv")

# 2. Features & Label
X = df[["word_count","avg_word_length","unique_word_ratio","sentence_complexity_score","strong_verbs_count","grammar_error_count"]]
y = df["label"]
# print(df.iloc[0])



# 3. Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

#standardscalling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)   

# 4. Model
model = LogisticRegression()

# 5. Train
model.fit(X_train, y_train)

# 6. Prediction
y_pred = model.predict(X_test)

# 7. Accuracy

print("Accuracy:", accuracy_score(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

probabilities = model.predict_proba(X_test)

print(probabilities[:5])
print(y_pred[:5])
for actual, predicted in zip(y_test[:10], y_pred[:10]):
    print("Actual:", actual, "Predicted:", predicted)


print("///////////////////////////////////////////////////////////////////////////////")

for actual, predicted in zip(y_test, y_pred):

    if actual != predicted:
        print("Actual:", actual, "Predicted:", predicted)
print("/////////////////////////////////////////////////////////////////////////////////")
probabilities = model.predict_proba(X_test)

for actual, predicted, prob in zip(y_test, y_pred, probabilities):

    if actual != predicted:
        print("Actual:", actual,
              "Predicted:", predicted,
              "Probability:", prob)
        
# Save the model
joblib.dump(scaler,"scaler.pkl")
joblib.dump(model,"philixa_model.pkl")
