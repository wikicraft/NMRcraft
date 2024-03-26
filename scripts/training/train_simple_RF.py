from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

from nmrcraft.analysis import plot_predicted_vs_ground_truth
from nmrcraft.data import load_data, split_data
from nmrcraft.utils import set_seed

set_seed()


def main():
    """Train a simple random forest model."""
    # Load the data
    dataset = load_data()

    # Only take 1% of the dataset
    dataset = dataset.sample(frac=0.01)

    # Extract features and target variables
    X = dataset[["E_sigmaiso_ppm", "M_sigmaiso_ppm"]].to_numpy()
    y = dataset["bond_length_M_E"].to_numpy()

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = split_data(X, y)

    # Create a pipeline with data preprocessing and random forest regressor
    pipe = make_pipeline(StandardScaler(), RandomForestRegressor())

    # Fit the pipeline to the training data
    pipe.fit(X_train, y_train)

    # Evaluate the model on the testing data
    score = pipe.score(X_test, y_test)

    # Print the R^2 score
    print(f"R^2 score: {score}")

    # Plot the predicted vs ground truth values
    plot_predicted_vs_ground_truth(y_test, pipe.predict(X_test))


if __name__ == "__main__":
    main()
