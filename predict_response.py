# Bibliotecas de pré-processamento de dados de texto
import nltk
nltk.download('punkt')
nltk.download('wordnet')

# palavras a serem ignoradas ao criar o conjunto de dados
ignore_words = ['?', '!',',','.', "'s", "'m"]

import json
import pickle

import numpy as np
import random

# Biblioteca load_model
import tensorflow
from data_preprocessing import get_stem_words

model = tensorflow.keras.models.load_model('./chatbot_model.h5')

# Carregue os arquivos de dados
intents = json.loads(open('./intents.json').read())
words = pickle.load(open('./words.pkl','rb'))
classes = pickle.load(open('./classes.pkl','rb'))


def preprocess_user_input(user_input):

    #Tokenize a entrada do usuário use a variável input_word_token_1 
   
    
    #Converta a palavra em sua forma raiz: stemização. Use a variável input_word_token_2
   
    
    #Remova as duplicidades e classifique a entrada
   

    bag=[]
    bag_of_words = []
   
    # Codificação dos dados de entrada 
    for word in words:            
        if word in input_word_token_2:              
            bag_of_words.append(1)
        else:
            bag_of_words.append(0) 
    bag.append(bag_of_words)
  
    return np.array(bag)
    
def bot_class_prediction(user_input):
    inp = preprocess_user_input(user_input)
  
    prediction = model.predict(inp)
   
    predicted_class_label = np.argmax(prediction[0])
    
    return predicted_class_label


def bot_response(user_imput):

   predicted_class_label =  bot_class_prediction(user_input)
 
   predicted_class = classes[predicted_class_label]

   for intent in intents['intents']:
    if intent['tag']==predicted_class:

        #Selecione uma resposta aleatória do robô
        
    
        return bot_response
    


print("Oi, eu sou a Estela, como posso ajudar?")

while True:
    #Obtenha a entrada do usuário
    
    print("Entrada do Usuário: ", user_input)

    response = bot_response(user_input)
    print("Resposta do Robô: ", response)
