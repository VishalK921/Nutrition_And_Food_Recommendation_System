Here’s the updated README file with your repository link included:

---

# Nutrition and Food Recommendation System

## Project Overview

The objective of this project is to build software that predicts the level of obesity of an individual and suggests suitable meals according to their tastes. The software uses a random forest classifier to analyze dietary habits and lifestyle preferences, achieving a 95% accuracy rate in predicting obesity levels.

## Features

- **Front-end**: Developed using HTML and CSS.
- **Back-end**: Implemented with Flask.
- **Data Preprocessing**: Utilizes Scikit-learn Pipeline for feature engineering, data cleaning, and normalization.
- **Model Training**: Employs a random forest classifier with 95% accuracy, validated against data from WHO and Mexican Normativity.
- **User Analysis**: The application analyzes user responses and classifies obesity levels based on trained models.

## Lessons Learned

- Importance of good data and feature selection.
- Effective use of pipelines in Scikit-learn for data preprocessing.

## Installation

To set up and run this project locally, follow these steps:

1. **Clone the repository:**

    ```sh
    git clone https://github.com/VishalK921/Nutrition_And_Food_Recommendation_System.git
    cd Nutrition_And_Food_Recommendation_System
    ```

2. **Create and activate a virtual environment:**

    ```sh
    python3 -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Run the application:**

    ```sh
    flask run
    ```

5. **Access the application:**

    Open your browser and go to `http://127.0.0.1:5000/`

## Usage

1. **Input**: Users provide their dietary habits and lifestyle preferences through the front-end form.
2. **Prediction**: The application predicts the user's obesity level based on the input data.
3. **Suggestions**: Suitable meal suggestions are provided according to the user's tastes and obesity level.

## Contributing

If you would like to contribute to this project, please follow these guidelines:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature-name`).
3. Make your changes and commit them (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature-name`).
5. Open a pull request.

## License

This project is licensed under the MIT License.

---
