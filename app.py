from model_prediction import load_model,predict_pathology,preprocess
import streamlit as st
import os
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly.express as px
import numpy as np

allowed_image_extensions=["jpg","png","jpeg"]

home_image="AntibioticResistance.png"
model_json_file=os.path.abspath("model_architecture.json")
model_weights_file=os.path.abspath("model_weights.h5")
model=load_model(model_json_file,model_weights_file)

def run_web_app():
    st.markdown(
        "<h2 style='text-align: center; color: black;'>X-Ray Classification for Smart Use of Antibiotics  <br /> "
        "during COVID-19 Pandemic</h2>",
        unsafe_allow_html=True)
    st.write("")

    st.sidebar.header("Upload Chest X-Ray Image")
    xray_file=st.sidebar.file_uploader("Upload X-ray",type=allowed_image_extensions,key="f1")
    st.sidebar.markdown(
        "**Medical Disclaimer:** This tool is not a substitute for professional medical advice, diagnosis or treatment.")

    if xray_file is None:
        st.markdown(
            "To obtain a model prediction for a patient, upload the X-ray chest image (jpeg, png or jpg) to the "
            "left. The output will show the probabilities of Covid-19, Bacterial Pneumonia or a Normal chest.")
        st.markdown("Meanwhile, you can learn how antiobitc resitance happens and how to prevent it in your healthcare location.")
        st.image(home_image)
        st.markdown("**Health professionals**<br>To prevent and control the spread of antibiotic resistance, health professionals can:" 
        "<br>- Prevent infections by ensuring your hands, instruments, and environment are clean."
        "<br>- Only prescribe and dispense antibiotics when they are needed, according to current guidelines."
        "<br>- Report antibiotic-resistant infections to surveillance teams."
        "<br>- Talk to your patients about how to take antibiotics correctly, antibiotic resistance and the dangers of misuse."
        "<br>- Talk to your patients about preventing infections (for example, vaccination, hand washing, safer sex, and covering nose and mouth when sneezing).",unsafe_allow_html=True)
        st.markdown("**Policy makers**<br>To prevent and control the spread of antibiotic resistance, policy makers can:"
        "<br>- Ensure a robust national action plan to tackle antibiotic resistance is in place."
        "<br>- Improve surveillance of antibiotic-resistant infections."
        "<br>- Strengthen policies, programmes, and implementation of infection prevention and control measures."
        "<br>- Regulate and promote the appropriate use and disposal of quality medicines."
        "<br>- Make information available on the impact of antibiotic resistance.",unsafe_allow_html=True)
        st.markdown("Source: [World Health Organization](https://www.who.int/news-room/fact-sheets/detail/antibiotic-resistance).")


    if xray_file is not None:

        ######################################################
        ############### Getting model output #################
        ######################################################

        xray_file = preprocess(xray_file)
        pathology_prediction = predict_pathology(xray_file, model)
        pathology_prediction_round = np.around((pathology_prediction*100),2)

        ######################################################
        ################# Visual Diagnosis ###################
        ######################################################

        condition = ['COVID-19', 'Normal', 'Bacterial<br>Pneumonia']
        condition_text = ['COVID-19', 'Normal', 'Bacterial Pneumonia']
        colors = px.colors.qualitative.Prism[0:3]

        fig = make_subplots(rows=1, cols=2, shared_yaxes=False, shared_xaxes=True, horizontal_spacing=0.13)
        fig.add_trace(go.Image(z=xray_file,hoverinfo="skip"), row=1, col=1)
        fig.add_trace(go.Bar(x=condition, y=pathology_prediction_round, marker_color=colors,
                             name='condition', hovertemplate='%{x} <br>Probability: %{y}%'), row=1, col=2)
        fig.update_layout(autosize=False, width=850, height=500, title=dict(text="X-Ray Diagnosis Results", \
                                                                            yanchor="middle", xanchor="auto", x=0.5), \
                          titlefont=dict(family="Calibri", size=40))
        fig['layout']['xaxis1'].update(title='Input Chest X-Ray', autorange="reversed", \
                                       showticklabels=False)
        fig['layout']['yaxis1'].update(showticklabels=False)
        fig['layout']['xaxis1'].update(autorange=True, showticklabels=False)
        fig['layout']['yaxis2'].update(title_text='Model Output Probability (%)', autorange=True, \
                                       )
        fig.update_layout(template='plotly_white')
        fig.update_yaxes(automargin=True)
        fig.update_layout(
            hoverlabel=dict(
                bgcolor="white",
                font_size=16,
                font_family="Rockwell"
            )
        )
        st.plotly_chart(fig)

        ######################################################
        ############## Interpretating output #################
        ######################################################

        # Getting the highest probability
        hg_prob = np.around(np.amax(pathology_prediction_round),2)

        # Getting the highest probability index
        hg_ix = np.where(pathology_prediction_round == hg_prob)

        # Checking how many classes had the highest probability
        hg_n = len(hg_ix)

        # Generating a text for the case when only one class presented highest prob
        if hg_n == 1:
            hg_class = condition_text[hg_ix[0][0]]

            # In case of COVID-19 (0) or Bacterial Pneumonia (2)
            if hg_ix[0][0] in (0, 2):
                st.markdown(
                    "Result description: The model predicted that the patient in the X-Ray most likely has "+str(hg_class)+", with a probability of "+str(hg_prob)+"%.")

            # In case of Normal (1)
            if hg_ix[0][0] == 1:
                st.markdown(
                    "Result description: The model predicted that the patient in the X-Ray presents normal conditions, with a probability of "+str(hg_prob)+"%.")

        st.markdown(
            "<h4 style='text-align: center; color: black;'>Recommendations for optimal antibiotic prescribing during the pandemic</h3>",
            unsafe_allow_html=True)

        ######################################################
        ##### Inserting antibiotics resistance awareness #####
        ######################################################

        # Generating a text for the case when only one class presented highest prob
        if hg_n == 1:
            hg_class = condition_text[hg_ix[0][0]]

            # In case of COVID-19 (0)
            if hg_ix[0][0] == (0):
                st.markdown(
                    "The [latest update of WHO’s interim guidance on the clinical management of COVID-19](https://apps.who.int/iris/handle/10665/332196) "
                    "incorporates antibiotic "
                    "stewardship principles with specific recommendations.<br>- The guidance does not recommend antibiotic "
                    "therapy or prophylaxis for patients with mild or moderate COVID-19 unless signs and symptoms of a bacterial "
                    "infection exist. <br>- The use of empiric antibiotic treatment for patients with suspected or confirmed "
                    "severe COVID-19, based on clinical judgement considering patient host factors and local epidemiology, "
                    "along with daily assessments for de-escalation, is recommended. <br>- The guidance further states that "
                    "empiric antibiotic bacterial pneumonia treatment can be considered in older people residing in long-term "
                    "care facilities and in children younger than five years with moderate COVID-19. As these are "
                    "non-hospitalized patients, antibiotics within WHO’s AWaRe (access, watch, reserve) classification of "
                    "antibiotics categorized as access, such as co-amoxicillin, should preferably be administered.",
                    unsafe_allow_html=True)
                st.markdown(
                    "Source: [Tackling antimicrobial resistance in the COVID-19 pandemic](https://www.who.int/bulletin/volumes/98/7/20-268573/en/). "
                    "Bulletin of the World Health Organization 2020;98:442-442A. July 2020.")
			# In case of Normal (1) or Bacterial Pneumonia (2)
            else:
                st.markdown("Follow local antimicrobial stewardship guidelines. [#AntibioticResistance](https://twitter.com/search?q=%23AntibioticResistance)")

        else:
            st.markdown("Follow local antimicrobial stewardship guidelines. [#AntibioticResistance](https://twitter.com/search?q=%23AntibioticResistance)")
                

run_web_app()
