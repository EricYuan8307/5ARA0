Feature: Predict housing prices
    In order to make accurate taxations
    As a realtor
    I want to obtain estimated housing prices

    Scenario: Pre-process a data set
        Given a data set
        When I pre-process the data set for analysis
        Then I obtain a pre-processed data set

    Scenario: Obtain predictions for new data
        Given a trained model on a pre-processed training set
        When I use the trained model for prediction on new data
        Then I obtain estimated housing prices
