import os
import cv2  #OpenCV color is from RGB to BGR
import face_recognition
import pickle  #Pickle is used to save the object on the disk/file for later use.
#Pickling is a way to convert a Python object (list, dictionary, etc.) into a character stream(file).
# Encoding is done to compress the images
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage   #To import images

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://faceattendancerealtime-bb0ee-default-rtdb.firebaseio.com/",
    'storageBucket':"faceattendancerealtime-bb0ee.appspot.com"  #Storage to store images in Google Cloud Storage
})


#To import students images which are stored in Images folder
folderPath = 'Images'
PathList = os.listdir(folderPath)
imgList = []  #Consist of list of images.
studentList = []
studentIds = []
#print(PathList)
for path in PathList:
    imgList.append(cv2.imread(os.path.join(folderPath,path)))    #Merge  Images folder and path 
    #print(os.path.splitext(path)[0] )  #To print only id's of images
    studentIds.append(os.path.splitext(path)[0])  #To print only id's of images

    fileName = f'{folderPath}/{path}' #to find path of the file
    bucket = storage.bucket() #bucket is used to store data/images in Google Cloud Storage Bucket(Firebase database)
    blob = bucket.blob(fileName) #Binary Large Object is unstructured data file
    blob.upload_from_filename(fileName)
print(len(imgList))


#Loop every single image and encode the image
def findEncodings(imagesList):
    encodeList = []
    for img in imagesList:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)   #Color Change--Color space(BGR to RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList
print("Encoding Started")  #started
encodeListKnown = findEncodings(imgList)  #Encoding processing
print(encodeListKnown)
encodeListKnownWithIds = [encodeListKnown, studentIds]  #are two lists to be stored in Pickle file
print("Encoding Completed")  #completed


file = open("EncodeFile.p",'wb')  #Create pickle file with its permissions wb--write binary file
pickle.dump(encodeListKnownWithIds, file)  #save lists into file
file.close()
print("File Saved")
