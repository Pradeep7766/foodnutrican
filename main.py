import streamlit as st
import tensorflow as tf
import numpy as np

#tensorflow Model Prediction
def model_prediction(test_image):
    model = tf.keras.models.load_model("trained_model.keras")
    image = tf.keras.preprocessing.image.load_img(test_image,target_size=(64,64))
    input_arr = tf.keras.preprocessing.image.img_to_array(image)
    input_arr = np.array([input_arr])  #convert single image to batch
    predictions = model.predict(input_arr)
    return np.argmax(predictions)


# Sidebar Navigation
st.sidebar.title("Navigation")
menu = st.sidebar.radio("Go to", ["Home", "About", "Predict"])

# Home Page
if menu == "Home":
    st.header("FoodNutriScan")
    st.image("D:\SE main project\web mage.jpg", caption="Dashboard Overview")

# About Page
elif menu == "About":
    st.title("About FoodNutriScan")
    st.image(
        "D:\SE main project\images\intro.jpg", 
        caption="Your Guide to Better Eating", 
    )
    
    # Introduction section
    st.subheader("What is FoodNutriScan?")
    st.write("""
    **FoodNutriScan** is a cutting-edge application designed to make your food choices smarter and healthier. 
    Using advanced **image processing technology** and **nutritional databases**, FoodNutriScan provides instant 
    and reliable nutritional information for your meals, especially focusing on diverse and traditional **Indian cuisine**.
    """)
    
    # Mission statement
    st.image(
        "D:\SE main project\images\mission.jpg", 
        caption="Making Healthier Choices Easy",
        width=600
    )
    st.subheader("Our Mission")
    st.write("""
    To empower individuals with the knowledge they need to make informed dietary decisions, promoting healthier 
    lifestyles while respecting diverse food traditions.
    """)
    
    # Why Choose Us section
    st.image(
        "D:\SE main project\images\choose us.jpg", 
        caption="Empowering You Through Food Insights",
        width=600
    )
    st.subheader("Why Choose FoodNutriScan?")
    st.write("""
    - **User-Friendly Interface**: Scan and retrieve information in seconds.
    - **Customizable**: Input your own ingredients for tailored results.
    - **Health-Centric**: Focused on improving dietary habits through awareness.
    """)
    
    st.write("FoodNutriScan is more than an app—it's your personal guide to better eating!")

# Predict Page
elif menu == "Predict":
    st.title("Model Prediction")

    test_image = st.file_uploader("Choose an image:")
    if(st.button("Show Image")):
        st.image(test_image)
    #Predict button
    if(st.button("Predict")):
        st.write("Our Prediction")
        result_index= model_prediction(test_image)
        with open("labels.txt") as f :
            content = f.readlines()
        label = []
        for i in content:
            label.append(i[:-1])
        st.success("It is a {}".format(label[result_index]))

