import pandas as pd
import math
import tensorflow as tf

def main():
    embarked = {'C': 0, 'Q':1, 'S':2}
    training_data = pd.read_csv("train.csv", header=0)
    mean = training_data["Fare"].mean()
    std =  training_data["Fare"].std()

    training_data = training_data.drop(["Name", "Ticket", "Cabin"], 1)
    training_data = training_data[pd.notnull(training_data["Embarked"])]
    training_data = training_data[pd.notnull(training_data["Age"])]
    training_data = training_data[pd.notnull(training_data["Fare"])]
    training_data["Sex"] = training_data["Sex"].map(
        lambda x: 1 if x == "male" else 0)
    training_data["Embarked"] = training_data["Embarked"].map(
        lambda x: embarked[x])
    training_data["Fare"] = training_data["Fare"].map(
        lambda x: 0.5*(((x - mean)/std) + 1))

    print training_data.head(10)
    import ipdb; ipdb.set_trace()

if __name__== '__main__':
    main()
