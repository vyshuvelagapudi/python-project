# python-project

video link: https://youtu.be/zCO-wi_VSE8

Data set link:https://drive.google.com/drive/folders/1IyuhcNhgUBPHzjVMOGB9tREUOEwa7wp8?usp=sharing


## Driver Drowsiness and Fog Monitoring System using Deep Learning

In this project,  We classied the foggy,drowsiness images and performed prediction.CNN(Convolutional neural networks are used for classification of the images .Sequential method  is used to build layer by layer model.Accuracy is calculated and model is saved to fog model pickel file.Flask is used to build a web application to upload images of drowsiness and foogginess of driver.

## CNN model:
1) Imported libraries(os,keras,tensorflow)
2) Imported foggy and drowsy data sets 
3) Builded the sequential model with convolutional neural networks
4) Image Data Generator is used to normalize the size of images
5) Resizied the images with scaling 1-255
6) Saved the model to pkl file
output :
![image](https://user-images.githubusercontent.com/89366183/145733818-2f9625e8-94f5-4c8a-ae9b-7fbe5fe16a2d.png)

![image](https://user-images.githubusercontent.com/89366183/145733836-6e84c883-2293-481b-ac2d-f6196d5123d6.png)

## Flask:
foggy_controller.py
1) Imported libraries(os,flask,flask_cors(cross-origin resource sharing)
2) Loaded the savel CNN model
3) The drowsiness and fogginess classification is implemented in foggy prediction method and the result is returned

app.py
1) Imported libraries(flask,os,flask_cors)
2) Imported foggyprediction from foggy_controller module
3) Created functions to upload files with extensions jpg,png,gif,jpeg
4) Messages are printed to the web application using context variable

Output:
![image](https://user-images.githubusercontent.com/89366183/145734803-43412d78-385b-43f7-a011-23ac4974eb3a.png)
![image](https://user-images.githubusercontent.com/89366183/145734830-455acd31-7846-48da-8723-40629bd6d73f.png)
![image](https://user-images.githubusercontent.com/89366183/145734865-71812c49-93a9-4e76-b0b3-daee8bfb1452.png)




