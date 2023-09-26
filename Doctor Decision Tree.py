import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import pydotplus
import matplotlib.pyplot as plt
import matplotlib.image as pltimg

# Read the data from CSV files
df = pd.read_csv("drug.csv")
df2 = df.tail(100)

# Preprocess the data
df2['Sex'] = df2['Sex'].map({'F': 0, 'M': 1})
df2['BP'] = df2['BP'].map({'HIGH': 0, 'LOW': 1, 'NORMAL': 2})
df2['Cholesterol'] = df2['Cholesterol'].map({'HIGH': 0, 'NORMAL': 1})
df2['Drug'] = df2['Drug'].map({'drugY': 4, 'drugX': 3, 'drugC': 2, 'drugA': 0, 'drugB': 1})

# Select features and target
features = ['Age', 'Sex', 'BP', 'Na_to_K', 'Cholesterol']
X = df2[features]
y = df2['Drug']

# Train a Decision Tree Classifier
dtree = DecisionTreeClassifier(criterion='entropy')
dtree.fit(X, y)

# Export the decision tree as an image
data = tree.export_graphviz(dtree, out_file=None, feature_names=features)
graph = pydotplus.graph_from_dot_data(data)
graph.write_png('doctor_decision_tree.png')

# Display the decision tree image
img = pltimg.imread('doctor_decision_tree.png')
plt.imshow(img)
plt.show()

# Make predictions
patient_data = [
    float(input("Enter the age of the patient: ")),
    int(input("Enter the sex of the patient (Female = 1, Male = 0): ")),
    int(input("Enter the BP of the patient (High = 2, Normal = 1, Low = 0): ")),
    int(input("Enter the cholesterol of the patient (High = 1, Normal = 0): ")),
    float(input("Enter the sodium/potassium: "))
]

prediction = dtree.predict([patient_data])[0]

# Map the prediction to drug names
drug_names = {0: "Drug A", 1: "Drug B", 2: "Drug C", 3: "Drug X", 4: "Drug Y"}
predicted_drug = drug_names[prediction]

print(f"You have been assigned {predicted_drug}")
