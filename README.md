# Corona-Classifier
Corona Classifier is a tool that will take symptoms of user as input and predicts whether the user might be having Corona or any Other Disease or none. 

This tool has mainly 2 modules:
**1. Logistic Regression Model**
**2. Django Website (for user input)**

## **1. Logistic Regression Model (Multiclass)**
Using the Logistric regression and given dataset a multiclass model is trained. This model will internally create multiple classifier models(1 per each class of 'y'). While prediction, the prediction of classifier with highest probability is considered as output of the main classifier.

**Dataset Used for training:** [data.csv](https://github.com/adityap27/Corona-Classifier/blob/master/ML%20model/data.csv)
	

> **4 Classes:**
> 
>     	
> 
>     [Coronavirus, Influenza, None, Seasonal Allergies]

**Model Performance:**

>  **Accuracy:**
> 
> ![Model
> Accuracy](https://raw.githubusercontent.com/adityap27/Corona-Classifier/master/model_accuracy.JPG)


> **Confusion Matrix:** 
> ![Confusion Matrix](https://raw.githubusercontent.com/adityap27/Corona-Classifier/master/confusion_matrix.JPG)


> **Precision and Re-Call:** ![Precision and Recall](https://raw.githubusercontent.com/adityap27/Corona-Classifier/master/precision_recall.JPG)
> 
**Note:** This model is trained on small dataset, so for now it shouldn't be used in real-world. (as COVID-19 is new, it's dataset is being developed with respect to time.)
## **2. Django Website (for user input)**
**Main Form:**
![Main Form](https://raw.githubusercontent.com/adityap27/Corona-Classifier/master/main_form.JPG)

**Prediction as per Logistic Regression Model: (for all input as yes)**
![Output](https://raw.githubusercontent.com/adityap27/Corona-Classifier/master/output.JPG)

**Note:** This model is trained on small dataset, so for now it shouldn't be used in real-world. (as COVID-19 is new, it's dataset is being developed with respect to time.)

