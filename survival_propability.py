"""
A program that uses given data and checks the
accuracy of various predictions.

Project from Udacity.
"""

# Importing pandas -- no need for more imports 
import pandas as pd

# Get data from csv and store them in a vector and a matrix: 
# the vector with all the observations (survived) and the matrix of all data
df = pd.read_csv('titanic_data.csv', delimiter=',')

outcomes = df['Survived']
data = df.drop('Survived', axis = 1)

# Given function that returns a string message with the accuracy score of input
def accuracy_score(truth, pred):
    """ Returns accuracy score for input truth and predictions. """
    
    # Ensure that the number of predictions matches number of outcomes
    if len(truth) == len(pred): 
        
        # Calculate and return the accuracy as a percent
        return "Predictions have an accuracy of {:.2f}%.".format((truth == pred).mean()*100)
    
    else:
        return "Number of predictions does not match number of outcomes!"

'''
# Question 1
#   How accurate would a prediction be that none of the passengers survived?
'''
def predictions_0(data):
    """ Model with no features. Always predicts a passenger did not survive. """

    predictions = []
    for _, passenger in data.iterrows():
        
        # Predict the survival of 'passenger'
        # We append 0, meaning that they all died. Otherwise we append 1
        # i.e. 0 := Died, 1 := Survived
        predictions.append(0)
    
    # Return predictions
    return pd.Series(predictions)

# Initialize predictions vector as above, and compute the accuracy
predictions = predictions_0(data)
print("\nQuestion 1:")
print(accuracy_score(outcomes, predictions), "\n")
'''
#
# Answer 1: Predictions have an accuracy of 61.62%.
#
#####################################################
'''

'''
# Question 2
#   How accurate would a prediction be that all female passengers survived 
#   and the remaining passengers did not survive?
'''
def predictions_1(data):
    """ Model with one feature: 
            - Predict a passenger survived if they are female. """
    
    predictions = []
    for _, passenger in data.iterrows():
        
        if passenger['Sex'] == 'female' :
            predictions.append(1)
        else :    
            predictions.append(0)
        
    
    # Return our predictions
    return pd.Series(predictions)

# Initialize predictions vector as above, and compute the accuracy
predictions = predictions_1(data)
print("Question 2:")
print(accuracy_score(outcomes, predictions), "\n")
'''
#
# Answer 2: Predictions have an accuracy of 78.68%.
#
#####################################################
'''

'''
# Question 3
#   How accurate would a prediction be that all female passengers 
#   and all male passengers younger than 10 survived?
'''
def predictions_2(data):
    """ Model with two features: 
            - Predict a passenger survived if they are female.
            - Predict a passenger survived if they are male and younger than 10. """
    
    predictions = []
    for _, passenger in data.iterrows():
        
        if passenger['Sex'] == 'female' or (passenger['Sex'] == 'male' and passenger['Age'] < 10) :
            predictions.append(1)
        else :    
            predictions.append(0)
        
    
    # Return our predictions
    return pd.Series(predictions)

# Initialize predictions vector as above, and compute the accuracy
predictions = predictions_2(data)
print("Question 3:")
print(accuracy_score(outcomes, predictions), "\n")
'''
#
# Answer 3: Predictions have an accuracy of 79.35%.
#
#####################################################
'''

'''
# Question 4
#   Implement a final prediction model so that it gets an accuracy of at least 80%.
'''
def predictions_3(data):
    """ Model with multiple features. Makes a prediction with an accuracy of at least 80%. """
    
    predictions = []
    for _, passenger in data.iterrows():
        
        # If female
        if passenger['Sex'] == 'female':
            # Parametrize the females further
            # If female between 40 and 50 and 3rd class, predict death
            if passenger['Age'] > 40 and passenger['Age'] < 50 and passenger['Pclass'] > 2:
                predictions.append(0)
            else:
                # else predict survival
                predictions.append(1)
        # If male
        else:
            # If male from first class and under 40, or under 8 in general, predict survival
            if (passenger['Pclass'] == 1 and passenger['Age'] < 40) or passenger['Age'] < 8 :
                predictions.append(1)
            else:
                # else predict death
                predictions.append(0)
        
    # Return our predictions
    return pd.Series(predictions)

# Initialize predictions vector as above, and compute the accuracy
predictions = predictions_3(data)
print("Question 4:")
print(accuracy_score(outcomes, predictions), "\n")
'''
#
#
# Answer 4: Predictions have an accuracy of 80.25%.
#
# Steps: To get a model with an accuracy of at least 80%, the result was derived by trial and error.
#        Testing various parameters and their values showed which groups would have an increased
#        probability of survival. Those parameters were implemented as conditions.
#
#       I looked at Age, Gender, and Pclass, as these features would mostly increase the probabilities. 
#       I also noticed that Sex == female needed extra parametrization, cause the probability of survival
#       of females was already contributing much to the result. Thus, instead of trying to increase accuracy
#       by adding (pressumably) favorable parameters, I decided to add unfavorable parameters
#       and instead record them as probability of death -- exclude them from the value space. 
#
#       The conditions as shown above were to split the population in 2: male and female, 
#       since this was the obvious largest deterministic factor of survival. Then, I looked 
#       into ages and class for both groups, and exluded (or included) the most likely events 
#       for death or survival, respectively. 
#
#       My predictions are 80.25% accurate. By parametrizing further, I would probably
#       hit higher accuracy. 
#
#####################################################
'''
