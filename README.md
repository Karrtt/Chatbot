# Chatbot-

This chatbot is a conversational agent created using NLP techniques and PyTorch, a powerful deep learning framework. It has been trained using a dataset called "intents.json" to understand and respond to user inputs accurately.
The intents file in this project contains information related to few medical conditions and it can be changed according to the required behaviour of the chatbot.
This model should work fine on any intents.json, and can be tuned by adjusting the hidden layer size and number of layers.

By leveraging NLP, the chatbot can effectively process and analyze natural language inputs from users. It uses techniques such as tokenization, stemming and bag of words to extract meaning from the messages it receives. In addition it sets the context to whatever condition the user has been diagnosed with so they can ask the corresponding treatment for that condition.

The UI is built using a Flask.


To run this project, clone the repo and install the required dependencies.
The chatbot can be run on command line using chat.py or as a flask app using app.py.

![image](https://github.com/Karrtt/Chatbot-/assets/79457820/2e3ddf04-3b5d-4cab-8093-2eb65f697bb8)
![image](https://github.com/Karrtt/Chatbot-/assets/79457820/05a02533-0065-4d01-8c3b-f0356e14c675)
![image](https://github.com/Karrtt/Chatbot-/assets/79457820/0906cf2f-447f-4374-80e7-cb7e81e78799)
