import keras.preprocessing.image as kf
import glob.glob

datagen=kf.ImageDataGenerator(rotation_range=40,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest')

files=glob.glob("*.*")
for img in files:
  if img=="processing.py":
    print("Leaving python file")
  else:
    image=kf.load_img(img)
    x=kf.img_to_array(image)
    x=x.reshape((1,)+x.shape)
    i=0
    for batch in datagen.flow(x,batch_size=1,save_to_dir='preview',save_prefix='mod'): #mod for modak and not for not_modak
      i+=1
      if i>20:
        break
