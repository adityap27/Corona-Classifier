from django.shortcuts import render
import pickle
# Create your views here.
def home(request):
    return render(request,'index.html',{})

def result(request):
    if request.method == 'GET':
            trip = int(request.GET['trip'])
            fever = int(request.GET['fever'])
            eye = int(request.GET['eye'])
            nose = int(request.GET['nose'])
            breath = int(request.GET['breath'])
            cough = int(request.GET['cough'])
            
           # load the model from disk
            filename="ML model/finalized_model.sav"
            classifier = pickle.load(open(filename, 'rb'))

            #Get Prediction        
            y_output_probab = classifier.predict_proba([[trip, fever, eye, nose, breath, cough]])
            result_probab=[]
            print("\nProbabilities")
            for i,p in enumerate(y_output_probab[0]):
                result_probab.append([classifier.classes_[i],str(round(p*100,2))])
                

            y_output = classifier.predict([[trip, fever, eye, nose, breath, cough]])
            print(y_output)
            result=y_output[0]
            return render(request, 'result.html',{'result':result,'result_probab':result_probab})

    else:
        return render(request, 'index.html')