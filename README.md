# Flight-Fare-Prediction

This project facilitates:

* End to end implementation and deployment of Machine Learning Flight Fare Prediction web application created with Flask and deployed on the Heroku platform.

### Website Link

If you want to view the deployed model, click on the following link:
http://krish-flight-fare-prediction.herokuapp.com/

The UI of the webpage:
![homepage][0]

### Dataset

The dataset for the project is taken from Kaggle and the features of the dataset are explained below.

Airline: The name of the airline.
Date_of_Journey: The date of the journey
Source: The source from which the service begins.
Destination: The destination where the service ends.
Route: The route taken by the flight to reach the destination.
Dep_Time: The time when the journey starts from the source.
Arrival_Time: Time of arrival at the destination.
Duration: Total duration of the flight.
Total_Stops: Total stops between the source and destination.
Additional_Info: Additional information about the flight
Price: The price of the ticket


### Exploratory Data Analysis

#### Analysis of various airlines and their prices in the dataset to find out the premium and cheap airlines.

![airline_price][1]

#### Analysis of various source location and the prices of the airline at that location.

![source_price][2]

### Feature Selection

#### Finding out the best feature which will contribute and have good relation with target variable is very important and following are some of the feature selection methods,

heatmap : Finds correlation between Independent and dependent attributes
feature_importance_ : feature importances for better visualization
SelectKBest

![heatmap][3]

![importance][4]

### Fitting model using Random Forest

#### Distribution plot

![displot][5]

#### Scatter plot

![scatterplot][6]

### Hyperparameter Tuning using RandomizedSearchCV and GridSearchCV

#### Distribution plot after hyperparameter tuning

![displot_after][7]

#### Scatter plot after hyperparameter tuning

![scatterplot_after][8]


[0]: images/homepage.jpg
[1]: images/airline_price.jpg
[2]: images/source_price.jpg
[3]: images/heatmap.png
[4]: images/importance.png
[5]: images/displot.png
[6]: images/scatterplot.png
[7]: images/displot_after.png
[8]: images/scatterplot_after.png