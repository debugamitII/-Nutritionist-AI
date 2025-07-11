### Health Management APP
from dotenv import load_dotenv

load_dotenv() ## load all the environment variables

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load Google Gemini Pro Vision API And get response

def get_gemini_response(input,image,prompt):
    model=genai.GenerativeModel('gemini-2.5-flash')
    response=model.generate_content([input,image[0],prompt])
    return response.text

def input_image_setup(uploaded_file):
    # Check if a file has been uploaded
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")
    
##initialize our streamlit app

st.set_page_config(page_title=" Health App")

st.header(" Health App")
input=st.text_input("Input Prompt: ",key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image=""   
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_container_width=True)


submit=st.button("Tell me the total calories")

input_prompt = (""" you are an amazing pediatrician and nutritionist.
You are an expert in analyzing food items and calculating their calorie content.
                your task is to analyze the image of food items and provide a detailed description of the total calories in the image.
                And details about the food items in the image.
                Follow the given format:
                1. Item 1- no of calories
                2. Item 2- no of calories
                ----
                ----
                you have to mention the food is healthy or not and also mention the ration percentage
                of carbohydrates, protein,fibers, minerals,sugars and fats in the food items.
                if the food is processed show a warning.
                if the food is healthy, show a green tick mark.
                Also mention required nutrition  for the person in a diet.

                """

)
## If submit button is clicked

if submit:
    image_data=input_image_setup(uploaded_file)
    response=get_gemini_response(input_prompt,image_data,input)
    st.subheader("The Response is")
    st.write(response)


