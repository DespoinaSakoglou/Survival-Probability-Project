# Survival Probability Project
A program that uses given data and checks the accuracy of various predictions.

## Description

In 1912, the ship RMS Titanic struck an iceberg on its maiden voyage and sank, resulting in the deaths of most of its passengers and crew. This project will explore a subset of the RMS Titanic passenger manifest to determine which features best predict whether someone survived or did not survive.

## Data

From a sample of the RMS Titanic data, we can see the various features present for each passenger on the ship:


Survived: Outcome of survival (0 = No; 1 = Yes)

Pclass: Socio-economic class (1 = Upper class; 2 = Middle class; 3 = Lower class)

Name: Name of passenger

Sex: Sex of passenger

Age: Age of passenger (Some entries contain NaN)

SibSp: Number of siblings and spouses of the passenger aboard

Parch: Number of parents and children of the passenger aboard

Ticket: Ticket number of the passenger

Fare: Fare paid by the passenger

Cabin Cabin number of the passenger (Some entries contain NaN)

Embarked: Port of embarkation of the passenger (C = Cherbourg; Q = Queenstown; S = Southampton)


Since we're interested in the outcome of survival for each passenger or crew member, we can remove the Survived feature from this dataset and store it as its own separate variable outcomes. We will use these outcomes as our prediction targets.

## How to run the project

To run the project, create a local directory and save the titanic\survival_probability.py and titanic\_data.csv there. Then simply run the script and see the results as output. Only pandas are used from external libraries. See the questions below to make sense of the output of the script. 


## Questions 

### Question 1

Using the RMS Titanic data, how accurate would a prediction be that none of the passengers survived?

### Question 2

How accurate would a prediction be that all female passengers survived and the remaining passengers did not survive?

### Question 3

How accurate would a prediction be that all female passengers and all male passengers younger than 10 survived?

### Question 4

Implement the final prediction model so that it gets an accuracy of at least 80%. Describe the features to look at and the conditions to use in order to split the survival outcomes in the data. How accurate are your predictions?
