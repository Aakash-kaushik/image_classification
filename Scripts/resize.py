import cv2
import glob
import os

dir=r'/home/aakash/14w/downloads/resized_modak'

files=glob.glob("*.*")

os.makedirs(dir)

dim=(300,300)

for img in files:
  if img=='resize.py':
    print('python file')
  else:
    temp=cv2.imread(img)
    #temp=cv2.cvtColor(temp,cv2.COLOR_BGR2GRAY)
    res_img=cv2.resize(temp,dim)
    cv2.imwrite(os.path.join(dir,img),res_img)
    print(img)

