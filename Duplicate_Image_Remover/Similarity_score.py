import os
import cv2
import matplotlib as plt
from skimage.metrics import structural_similarity as ssim
#input2_path = "C://Users/vaibh/PycharmProjects/DIR/Duplicate_Image_Remover/Sparsh/87_-312_372"
#input_path = "C://Users/vaibh/PycharmProjects/DIR/Duplicate_Image_Remover/testing"
window_name = 'Imagee'
font = cv2.FONT_HERSHEY_SIMPLEX
org = (50, 50)
fontScale = 1
color = (255, 0, 0)
thickness = 2

similar_list = []
temp3 = []
temp4=[]
temp5=[]
temp6=[]
temp7 = []


Input_path = 'C://Users/vaibh/PycharmProjects/DIR/Duplicate_Image_Remover/Sparsh/87_-312_372'
master_image = cv2.imread('C://Users/vaibh/PycharmProjects/DIR/Duplicate_Image_Remover/testing/test.jpg')
images_list = os.listdir('C://Users/vaibh/PycharmProjects/DIR/Duplicate_Image_Remover/Sparsh/87_-312_372')

master_image_gray = cv2.cvtColor(master_image, cv2.COLOR_BGR2GRAY)
#image_gray = cv2.cvtColor(images, cv2.COLOR_BGR2GRAY)
sim_score = []
for i in images_list:
    temp_img = cv2.imread(Input_path + "/" +i)
    temp_img_gray = cv2.cvtColor(temp_img , cv2.COLOR_BGR2GRAY)
    (score, diff) = ssim(master_image_gray, temp_img_gray, full=True)
    image = cv2.putText(temp_img_gray, f"similarity: {round(score, 2)}", (10, 10), cv2.FONT_HERSHEY_DUPLEX, 0.6, (255, 255, 255),1)
    temp3.append(image)
    print("Image similarity of "+i+' with test.jpg is :'+str(score))    
    if score > 0.50 and score < 0.60:
        temp4.append(i)
    elif score > 0.60 and score < 0.70:
            temp5.append(i)
    elif score > 0.70 and score < 0.80:
        temp6.append(i)
    elif score > 0.80:
        temp7.append(i)

print("similarity score between 0.50 and 0.60 are:",temp4)
print("similarity score between 0.60 and 0.70 are:",temp5)
print("similarity score between 0.70 and 0.80 are:", temp6)
print("similarity score above 0.80 are:",temp7)




#(score, diff) = ssim(master_image_gray, image_gray , full=True)
#print("Image similarity", score)
similar_list.append(temp3)

os.chdir("C://Users/vaibh/PycharmProjects/DIR/Duplicate_Image_Remover/scoree")
for iter, i in enumerate(similar_list):
    os.chdir("C://Users/vaibh/PycharmProjects/DIR/Duplicate_Image_Remover/scoree")
    if os.path.exists("dir" + str(iter)):
        os.chdir("dir" + str(iter))
    else:
        os.mkdir("dir" + str(iter))
        os.chdir("dir" + str(iter))
        for k, j in enumerate(i):
          sentiment = "image" + str(k) + ".jpg"
          cv2.imwrite(sentiment, j)
















