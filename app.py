import streamlit as st 
from transformers import pipeline


st.write('# Talk to Mi')
st.write("Hey there, I'm Mi. Are you having a hard time writing? Let me help you out!")

@st.cache(allow_output_mutation=True)
def get_text_generator():
    text_generator = pipeline("text-generation")
    return text_generator


text_generator = get_text_generator() 

user_input = st.text_area('Type in a sentence', 'Once upon a time in "Nostalgia Land"')
output_length = st.slider('How many words do you want me to generate?',
                        min_value=20 ,
                        max_value=100,
                        value=50)

button = st.button('Let the magic happen!')

if button:
    st.write(text_generator(user_input, 
                    max_length = output_length)[0]['generated_text'])