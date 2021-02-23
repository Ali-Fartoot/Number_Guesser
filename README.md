# Itroduction

A number recognizer application with almost***95% accuracy***  written by ***Scikit-learn*** (sklearn) library as core of processes, ***pygame*** module used for draw app and ***Pillow*** library for editing images.

# How to use?

I) First of all, while you are running the code, you have to be ***online***.

II) Check  you have this library in your enviroment:
1. sklearn
2. numpy
3. PIL
4. pygame
5. scipy(usually by installing sklearn you installed numpy and scipy by default)

III) Then run ***main.py***

After ***taking 6 or 7 minutes*** (depends on your system), you will see small window (280 × 280) and you can draw a number between ***0 to 9***. 
And by pressing ***Enter*** you will send your image to program and it return it's guess and it continues till you close program by ***close button***.

# How program works?

First program gets ***MNIST dataset*** from internet and after  ***AUGMENTING DATA*** (shifting image into left, right, down and up), program add them to our training dataset.
Program starts to find best hyperparameters for ***KNN CLASSIFIER*** by ***GRIDSEARCHCV***. Then it makes new class for  knn classifier and pass  best parameter into  constructor of knn classifier.
Afterward  program run ***draw app.*** and gets images from user. It resizes image to 28 * 28 and converts images to numpy array to pass it into **knn_clf.predict()** function and it returns 
the anwser.
