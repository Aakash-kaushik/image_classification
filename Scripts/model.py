from keras.models import Sequential
from keras.layers import Conv2D,MaxPooling2D
from keras.layers import Activation,Dropout,Flatten,Dense
from keras.preprocessing.image import ImageDataGenerator

model=Sequential()
model.add(Conv2D(32,(3,3),input_shape=(300,300,3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Conv2D(32,(3,3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Conv2D(32,(3,3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Flatten())
model.add(Dense(64))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(1))
model.add(Activation('sigmoid'))

model.compile(loss='binary_crossentropy',optimizer='rmsprop',metrics=['accuracy'])

datagen=ImageDataGenerator(rescale=1.0/255.0)

train_generator=datagen.flow_from_directory('train',target_size=(300,300),batch_size=8,class_mode='binary')
test_generator=datagen.flow_from_directory('test',target_size=(300,300),batch_size=8,class_mode='binary')

model.fit_generator(train_generator,steps_per_epoch=5311,epochs=5,validation_data=test_generator,validation_steps=2655)

model.save_weights('50_epochs.h5')
