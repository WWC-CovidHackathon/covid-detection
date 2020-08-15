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

* Folder DataPreparation <br>
 * Random Selection from ZhangLabData.ipynb <br>
   Function: From thousands of ‘Normal’ and ‘Bacterial Pneumonia’ images, this code randomly selects 490 for each class for our project. <br>
 * Dataset_Creation_Final.ipynb <br>
   Function: It splits images into training, test and validation sets. <br>
<br>
* Folder Modeling <br>
 * SageMaker_Model.ipynb <br>
   Function: Generates the model in AWS SageMaker <br>
 * densenet.hdf5 <br>
   Function: Pre-trained files, obtained from the course [['AI for Medical Diagnosis', in Coursera](https://www.coursera.org/learn/ai-for-medical-diagnosis)] <br>
<br>
* Folder Deployment <br>
	* model_architecture.json and model_weights.h5 <br>
	Function: our trained model files <br>
	* model_prediction.py <br>
	Function: generates prediction for images insert by users <br>
	* app.py <br>
   	Function: allows users to upload images and to obtain predictions <br>
	* AntibioticResistance.png <br>
   	Function: antibiotic resistance awareness image to be displayed in the app <br>
