# covid-detection
**WomenWhoCode Hackathon Covid Detection and Antibiotic Resistance Prevention application.**<br>
To run the application clone the repository and run the following command
### **streamlit run app.py**<br>

## Dataset
[[IEEE8023 GitHub Account](https://github.com/ieee8023/covid-chestxray-dataset)]
[[Mendeley](https://data.mendeley.com/datasets/rscbjbr9sj/3)]

## Model:
* DenseNet121. The pre-trained files were obtained from the course [['AI for Medical Diagnosis', in Coursera](https://www.coursera.org/learn/ai-for-medical-diagnosis)]

## Modeling and Deployment Tools
### Modeling
* AWS
* AWS Sagemaker
* AWS S3

### WebAPI and Deployment Tools
* Streamlit
* Heroku 

### Project Demo
The project demonstrates the Covid Detection and Antibiotic Resistance Prevention application built into an interactive Streamlit app.
<p align="center"><img src="appdemo.gif" width="750" height="450"></p>
Lin

<br>The application can be found **<a href="https://covid-wwc-hackathon.herokuapp.com/"> here</a>**.

### Main files description

* Folder DataPreparation
 * Random Selection from ZhangLabData.ipynb
   Function: From thousands of ‘Normal’ and ‘Bacterial Pneumonia’ images, this code randomly selects 490 for each class for our project.
 * Dataset_Creation_Final.ipynb
   Function: It splits images into training, test and validation sets.

* Folder Modeling
 * SageMaker_Model.ipynb
   Function: Generates the model in AWS SageMaker
 * densenet.hdf5
   Function: Pre-trained files, obtained from the course [['AI for Medical Diagnosis', in Coursera](https://www.coursera.org/learn/ai-for-medical-diagnosis)]

* Folder Deployment
 * model_architecture.json and model_weights.h5
   Function: our trained model files
 * model_prediction.py
   Function: generates prediction for images insert by users
 * app.py
   Function: allows users to upload images and to obtain predictions
 * AntibioticResistance.png
   Function: antibiotic resistance awareness image to be displayed in the app
