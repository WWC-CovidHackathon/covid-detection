# covid-detection
**WomenWhoCode Hackathon Covid Detection and Antibiotic Resistance Prevention application.**<br>
<br><b>The application can be found <a href="https://covid-wwc-hackathon.herokuapp.com/"> here</a></b>.<br>

To run the application clone the repository and follow these steps :<br>
1. Clone the repository to your local machine.
2. Create a new python virtual environment.<br>
3. Got to the Deployment directory and open terminal.<br>
4. Run **pip install -r requiremnts.txt** to install the required dependencies.<br>
5. Run **streamlit run app.py** to run the application.<br>

## Dataset
[[IEEE8023 GitHub Account](https://github.com/ieee8023/covid-chestxray-dataset)]
[[Mendeley](https://data.mendeley.com/datasets/rscbjbr9sj/3)]

## Model
* DenseNet121. The pre-trained files were obtained from the course ['AI for Medical Diagnosis', in Coursera](https://www.coursera.org/learn/ai-for-medical-diagnosis)

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


### Main files description

#### Folder DataPreparation 
* Random Selection from ZhangLabData.ipynb<br>
Function: From thousands of ‘Normal’ and ‘Bacterial Pneumonia’ images in [Mendeley](https://data.mendeley.com/datasets/rscbjbr9sj/3), this code randomly selects 490 for each class for our project. <br>
* Dataset_Creation_Final.ipynb<br>
Function: It splits all images into training, test and validation sets using stratified random sampling in order to ensure that all sets come from a similar distribution.

#### Folder Modeling 
* SageMaker_Model.ipynb <br>
Function: It generates our model in AWS SageMaker. <br>
* densenet.hdf5<br>
Function: These are the pre-trained weights, obtained from the course ['AI for Medical Diagnosis', in Coursera](https://www.coursera.org/learn/ai-for-medical-diagnosis). <br>

#### Folder Deployment 
* model_architecture.json and model_weights.h5<br>
Function: These are our trained model files. <br>
* model_prediction.py<br>
Function: It generates predictions using our model for the X-rays uploaded in the streamlit application.<br>
* app.py<br>
Function: This is the main streamlit application that generates prediction for an uploaded X-ray image and also provide antibiotic resistance guidelines. <br>
* requirements.txt <br>
Function: It contains all the package versions used for deployment.
