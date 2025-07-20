import streamlit as st
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Initialize chatbot
chatbot = ChatBot('ResumeRankerBot')

# Train with English corpus if no database exists
trainer = ChatterBotCorpusTrainer(chatbot)
try:
    trainer.train('chatterbot.corpus.english')
except Exception as e:
    st.write("Error training chatbot:", e)

st.title('ResumeRanker Chatbot')

user_input = st.text_input('You:')
if st.button('Send') and user_input:
    response = chatbot.get_response(user_input)
    st.write('Bot:', response)
