from PaintAPP import init, return_resume
from ScalingDataTest import resize_image
from ProcessorUnit import find_best_param
from sklearn.neighbors import KNeighborsClassifier
from SplitDataSet import x_train, y_train, x_train_augmented,y_train_augmented ,x_test, y_test
import numpy as np
from PIL import Image

# find best parameter
best_param = find_best_param()

knn_clf = KNeighborsClassifier(**best_param)

'''
# you can test accuracy with this code
from sklearn.metrics import accuracy_score
y_predicted = knn_clf.predict(x_test)
print(accuracy_score(y_test, y_predicted))

'''

# initialize "MYPaintApp"
init()
while return_resume():
    # resize image to 28 X 28 pixel
    resize_image()
    knn_clf.fit(x_train, y_train)

    # convert image to array
    im = Image.open('resized_image.png')
    image_sequence = im.getdata()
    # In this part we have a 3D array that items in each column are same, so we get one of them
    temp = np.array(image_sequence)[:, 0]
    result = knn_clf.predict([temp])[0]
    print(f"your number is '{result}'")
    # run again program until program closed
    init()
