# <ASSIGNMENT 2.4: Complete the feature proposal>
Feature: Recommend investment opportunities
    In order to get the most suitable investment
    As a investor
    I want to receive the notification immediately after login

    Scenarios:
        Evaluate opportunities:
        Run the current database
        When it is midnight
        system Compare to the historical record
        and analyze the most valuable investment
        evaluate the investments per district

    raise opportunity notification:
        Evaluate current database
        And compared to the historical database
        When the extraordinary opportunity appear
        And user login
        push notification


# </ASSIGNMENT 2.4>

# <ASSIGNMENT 2.5: Answer the open questions>
#How will the proposed recommender system affect the dataset?
# The previous dataset is the base of future recommendation. If the system changed for some reason(like add some features)
# the dataset will also need to change.
# If developer do not upload the dataset. Next time, the result will be wrong.
#If database changed, the system also need to make changes. Therefore, they are the whole part.

#What sort of model would be suited for predicting housing price development?
# It should be a supervised learning model. There are labels for all inputs.
# The model can make the linear regression. We need to make a prediction
# The model should support multi-variance input. There should be various different input to
# classify the difference of houses.

# reference: Predicting House Price in India Using Linear Regression Machine Learning Algorithms

#How can you monitor and evaluate recommendation performance once the system is deployed?
# we can set training dataset and validation dataset.
# In running record, we can see if there is any errors during the system running.
# Receive the feedback from clients, we can know whether system work or not.

# </ASSIGNMENT 2.5>
