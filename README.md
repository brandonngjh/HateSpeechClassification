# Hate Speech Classification Project: 50.007 Machine Learning - Summer 2024

This project aims to classify social media posts as hateful or non-hateful using various machine learning models. It is part of the SUTD 50.007 Machine Learning course.

### Tasks

#### Task 1: Implement Logistic Regression
- Implemented a logistic regression model from scratch without using any predefined packages.
- Added L2 regularization, convergence check, and increased epochs to improve performance.

#### Task 2: Apply Dimension Reduction Techniques
- Applied PCA to reduce dimensionality and evaluated the performance using KNN.
- Experimented with 100, 500, 1000, and 2000 principal components.

#### Task 3: Other Machine Learning Models
- Explored various models including SVM, Decision Trees, Random Forests, AdaBoost, Extra Trees, Gradient Boosting, XGB, and different Naive Bayes classifiers.
- Best model was a Voting Classifier combining Random Forest, Extra Trees, and Logistic Regression.
- **Best Score:** 0.71870 (`Voting_Predictions.csv`)

### Results
- **First Attempt Score (PCA + Logistic Regression):** 0.69386
- **Random Forest Classifier Score:** 0.71254
- **Extra Trees Classifier Score:** 0.71424
- **Best Score (Voting Classifier):** 0.71870

### Classifiers Experimented With and Tuned
- Logistic Regression: Dimension reduction with PCA and TruncatedSVD
- SVM: Dimension reduction with PCA
- Decision Tree
- Random Forest: Dimension reduction with PCA
- AdaBoost
- Extra Trees
- GradientBoostingClassifier
- XGBClassifier
- Multinomial Naive Bayes
- Complement Naive Bayes
- Bernoulli Naive Bayes
- Voting Classifier of various other classifiers
