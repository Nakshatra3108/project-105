import os
import cv2

path='Images'
images=[]

for file in os.listdir(path):
    nm,ext=os.path.splitext(file)
    if ext in ['.gif','.png','.jpg','.jpeg','.jfif']:
        file_name=path+'/'+file
        #print(file_name) 
        images.append(file_name)
print(images)
count=len(images)

frame = cv2.imread(images[0])
print(frame.shape)
height,width,layers=frame.shape
size=(width,height)
print(size)
out=cv2.VideoWriter('Video_File.avi',cv2.VideoWriter_fourcc(*'DIVX'),0.8,size)
for i in range(0, count-1):
    img=cv2.imread(images[i])
    out.write(img)
print('done')