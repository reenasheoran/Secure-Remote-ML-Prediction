# Secure-Remote-ML-Prediction
Remote machine learning prediction on encrypted data
## Motivation
Data privacy is a central issue now a days, especially ones that train and infer on sensitive data. In order to comply with the four pillars of perfectly privacy-preserving AI, input user data and resulting model outputs inferred from that data should not be visible to any parties except for the user.  Preserving user data privacy is not only beneficial for the users themselves, but also for the companies processing potentially sensitive information. Privacy goes hand in hand with security. Having proper security in place means that data leaks are much less likely to occur, leading to the ideal scenario: no loss of user trust and no fines for improper data management.
## Objective 
In this project I tried to meet the following data privacy: - <br>
1. **Input Privacy**: The guarantee that a user’s input data cannot be observed by other parties, including the model creator.<br>
2. **Output Privacy**: The guarantee that the output of a model is not visible by anyone except for the user whose data is being inferred upon.<br>
## Technologies used
1. **Homomorphic Encryption** - For encrypting user data and predicted result, before sending it on channel.<br>
2. **Socket Programming** - For sending and receiving data between client and server.<br>
3. **Machine Learning** - For creating a machine learning model - Linear Regression.<br>
## Installation

## Project Files
This project mainly contains three files. <br>
1. **Client.py** - This file sits on the user machine and includes the following:-<br>
               1. Methods to generate and store a private/public key pair.<br>
               2. Method to create a json object, containing encrypted data and public key, that is to be send to the server.<br>
               3. Methods to help decrypt the answer onces received from the remote company server.<br>
2. **Server.py** - This file sits on the company's cloud or server machine that provides machine learning services. It includes the following:-<br>
               1. Method to receive and unpack a json object, containing encrypted data and public key.<br>
               2. Method to predict the desired result based on user input. <br>
               3. Method to pack up the encrypted result and return it back to the customer.<br>
3. **Linmodel.py** - This file also sits on the company's site that provides ML services. It contains the machine learning model. The Server.py file uses weights generated through this file for making prediction on user data.<br><br>
The communication between client and server is done using socket programming, to test the project in real-time scenario.
## References
1. Aslett, Louis JM, Pedro M. Esperança, and Chris C. Holmes, Encrypted statistical machine learning: new privacy preserving methods (2015), arXiv preprint arXiv:1508.06845.<br>
2. Graepel, Thore, et al., Machine Learning on Encrypted Data (2012), ICISC 2012, LNCS 7839.<br>
