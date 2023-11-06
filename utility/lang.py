import streamlit as st
from google.cloud import translate

# Initialize the Google Cloud Translation client
client = translate.TranslationServiceClient()

# Function to translate text from English to Traditional Chinese
def translate_to_chinese(text):
    target_language = "zh-TW"  # Language code for Traditional Chinese
    response = client.translate_text(
        parent="projects/[YOUR_PROJECT_ID]",  # Replace with your project ID
        contents=[text],
        target_language_code=target_language,
    )
    return response.translations[0].translated_text

# Streamlit app
st.title("Multi-Lingual Streamlit App")

# Input box for the English text
input_text = st.text_area("Enter text in English", "Hello, world!")

# Translate button
if st.button("Translate to Traditional Chinese"):
    translated_text = translate_to_chinese(input_text)
    st.write("Translated text (Traditional Chinese):", translated_text)

st.sidebar.markdown("**Additional Options**")
# You can add more features or widgets to your app in the sidebar

