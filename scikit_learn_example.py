from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.datasets import load_iris
import pandas as pd

def demonstrate_sklearn_workflow():
    """Demonstrates a basic Scikit-learn machine learning workflow."""

    print("--- Scikit-learn Demonstration ---")

    # 1. Load a sample dataset (Iris dataset)
    print("\nLoading the Iris dataset...")
    iris = load_iris()
    X = iris.data  # Features (sepal length, sepal width, petal length, petal width)
    y = iris.target # Target variable (species of iris)
    
    # For better understanding, let's see feature names and target names
    print(f"Feature names: {iris.feature_names}")
    print(f"Target names: {iris.target_names}") # 0: setosa, 1: versicolor, 2: virginica
    
    # Convert to a Pandas DataFrame for easier inspection (optional, but good practice)
    df = pd.DataFrame(data=X, columns=iris.feature_names)
    df['species'] = y
    df['species_name'] = df['species'].apply(lambda x: iris.target_names[x])
    print("\nFirst 5 rows of the Iris dataset (as Pandas DataFrame):")
    print(df.head())

    # 2. Split the data into training and testing sets
    print("\nSplitting data into training (80%) and testing (20%) sets...")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    # random_state for reproducibility, stratify for maintaining class proportions
    print(f"Training set size: {X_train.shape[0]} samples")
    print(f"Test set size: {X_test.shape[0]} samples")

    # 3. Initialize and train a machine learning model
    # We'll use RandomForestClassifier, a versatile and powerful model.
    print("\nInitializing and training a RandomForestClassifier model...")
    model = RandomForestClassifier(n_estimators=100, random_state=42, class_weight='balanced')
    # n_estimators: number of trees in the forest
    # class_weight='balanced': adjusts weights inversely proportional to class frequencies
    model.fit(X_train, y_train)
    print("Model training complete.")

    # 4. Make predictions on the test set
    print("\nMaking predictions on the test set...")
    y_pred = model.predict(X_test)

    # 5. Evaluate the model
    print("\nEvaluating the model...")
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {accuracy:.4f} (or {accuracy*100:.2f}%)")

    print("\nClassification Report:")
    # Shows precision, recall, f1-score for each class
    print(classification_report(y_test, y_pred, target_names=iris.target_names))
    
    # Example of predicting a new, unseen sample
    # Let's take a sample that could be Iris versicolor or virginica
    # e.g., sepal length=6.0, sepal width=2.9, petal length=4.5, petal width=1.5
    new_sample = [[6.0, 2.9, 4.5, 1.5]] 
    prediction = model.predict(new_sample)
    predicted_species_name = iris.target_names[prediction[0]]
    print(f"\nPrediction for a new sample {new_sample}: Species '{predicted_species_name}' (class {prediction[0]})")


    print("\n--- Scikit-learn Demonstration End ---")

if __name__ == "__main__":
    demonstrate_sklearn_workflow()
