# image_classification
image classification using python, keras and tensorflow for keras 

  #### Approach
    1. Downloaded the images from google images contaning modak and india sweets(without modak)
    2. resized them to be of equal dimensions
    3. processed and augmented the data with keras.preprocessing.image because i had less amount of examples to train and test on
    4. implemented a CNN with help of keras and tensorflow in background
    5. compiled and trained the model 
    6. Gives a .h5 model
 #### steps to run through
    1. first run the scrape_modak.py and scrape_not_modak.py scripts to download the images
    2. keep the in two folders one containing modak and other not_modak
    3. resize them using resize.py(need to put resize.py in the folder where your images are)
    4. make a folder named preview in both the folder keep processing.py in that nad run that to create more data
    5. then take all that data and split into test and train sets and create folders like this 
       data
        |test
          |modak
          |not_modak
        |train
          |modak
          |not_modak
    6. after creating put the model.py file in the folder named data and run it with command "python3 ./model.py" if you are using a terminal.
    7. Save a .h5 model in the same directory.
 #### Results
 ![result](https://raw.githubusercontent.com/Aakash-kaushik/image_classification/master/result.png)
