# Pima Indian Diabetes Prediction App

This Streamlit web application predicts whether a person has diabetes based on medical inputs such as glucose level, BMI, and insulin level.

## Features

- User-friendly input interface for providing medical features.
- Uses a pre-trained machine learning model for accurate predictions.
- Outputs whether the person is "Diabetic" or "Non-Diabetic".

## Setup Instructions

1. Clone this repository:
    ```bash
    git clone https://github.com/your-username/pima-diabetes-predictor.git
    cd pima-diabetes-predictor
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Ensure that the `pima_diabetes_model.pkl` file is in the same directory as `app.py`.

4. Run the application:
    ```bash
    streamlit run app.py
    ```

5. Open the application in your web browser (usually at `http://localhost:8501`).

## Files

- **app.py**: The main application script for the Streamlit app.
- **pima_diabetes_model.pkl**: The serialized machine learning model trained on the Pima Indian Diabetes dataset.
- **requirements.txt**: A list of Python dependencies for the project.
- **README.md**: Documentation and setup instructions for the project.

## Model Information

The model is a Random Forest Classifier trained on the Pima Indian Diabetes dataset, predicting the likelihood of diabetes.

## Contribution

Feel free to contribute by forking the repository and submitting pull requests.

---

**Author**: Bilal Rafique

