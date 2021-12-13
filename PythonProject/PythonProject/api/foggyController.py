#Imported libraries
import numpy as np
from keras.models import load_model
from keras.preprocessing import image
#The saved model is loaded 
saved_model = load_model("model/fogmodel.pkl")
# predicting  the image with drowsiness or fogginess
def foggyPrediction(path):
    img = image.load_img(path, target_size=(300, 300)) 
    # Scaling the images to array size to represent in numbers
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)

    images = np.vstack([x])
    classes = saved_model.predict(images, batch_size=10)
    print(classes[0])
    # predicting classes
    if classes[0] < 0.5:
        result = "Image shows Drowsiness"
    else:
        result = "Image is Foggy"
 
    return result