# Secure-Remote-ML-Prediction
Remote machine learning prediction on encrypted data
## Technologies used
1. **Homoencryption** - For encrypting user data and predicted result, before sending it on channel.<br>
2. **Socket Programming** - For sending and receiving data between client and server.<br>
3. **Machine Learning** - For creating a machine learning model - Linear Regression.<br>
## Project Files
This project mainly contains three files. <br>
1. **Client.py** - This file sits on the user machine and includes the following:-<br>
               1. Methods to generate and store a private/public key pair.<br>
               2. Method to create a json object, containing encrypted data and public key, that is to be send to the server.<br>
               3. Methods to help decrypt the answer onces received from the remote company server.<br>
2. **Server.py** - This file sits on the company's cloud or server machine that provides machine learning services. It includes the following:-
               1. Method to receive and unpack a json object, containing encrypted data and public key.
               2. Method to predict the desired result based on user input. 
               3. Method to pack up the encrypted result and return it back to the customer.
3. **Linmodel.py** - This file also sits on the company's site that provides ML services. It contains the machine learning model. The Server.py file uses weights generated through this file for making prediction on user data.

