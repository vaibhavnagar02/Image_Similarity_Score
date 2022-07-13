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











#scoree = []
#similar_lists = []

#image_list = os.listdir(input2_path)
#test_list = os.listdir(input_path)

#while True:
    #if len(image_list) == 0:
       # break
    #i = 0
    #temp2 = []
    #temp2.append(test_list)
    #temp = []
    #temp.append(image_list[i])
    #del image_list[0]
    #j = 0
    #while j < len(image_list):
        #image1 = image_list[j]
        #image1 = cv2.imread( input2_path + "/" + image_list[j] )
        #image1 = cv2.resize(image1, (100, 200))
        #image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
        #flag = False
        #for (iter),k in enumerate(temp2):
           # image2 = cv2.imread( input_path + "/"  )
           # image2 = cv2.resize(image2, (100, 200))
           # image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
            #score, diff = ssim(image1, image2, full = True)
            #print("Similarity score is:" , score)
        #else:
           # j = j + 1



#os.chdir("C://Users/vaibh/PycharmProjects/DIR/Duplicate_Image_Remover/scoree")
#for iter,i in enumerate(scoree):
  #  os.chdir("C://Users/vaibh/PycharmProjects/DIR/Duplicate_Image_Remover/scoree")
   # if not os.path.exists("dir" + str(iter)):
    #    os.mkdir("dir" + str(iter))
     #   os.chdir("dir" + str(iter))
    #else:
     # os.chdir("dir" + str(iter))
    #for k,j in enumerate(i):
     #   sentiment = "image" +  str(k) + ".jpg"
      #  cv2.imwrite(sentiment  , j)





# i = 0
# while i < len(image_list):
#     temp = []
#     if len(image_list) == 1:
#         temp.append(image_list[0])
#         del image_list[0]
#         similar_lists.append(temp)
#         break
#     print("\n", i, " -----------------> ")
#     temp.append(image_list[i])
#
#     j = i+1
#     while j < len(image_list):
#         image1 = cv2.imread( input_path + "/" + image_list[i] )
#         image2 = cv2.imread( input_path + "/" + image_list[j] )
#
#         image1 = cv2.resize(image1, (200, 200))
#         image2 = cv2.resize(image2, (200, 200))
#
#         image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
#         image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
#
#         for k in temp:
#             ssim(ima)
#
#         j = j + 1
#
#     del image_list[i]
#     similar_lists.append(temp)
#     i = 0


base = "C://Users/vaibh/PycharmProjects/DIR/Duplicate_Image_Remover/Similar_Images"

#Similar Images
#for iter, list in enumerate(similar_lists):
   # os.chdir(base)
    #if len(list) == 1:
     #   continue
    #if not os.path.exists("dir" + str(iter)):
       # os.mkdir("dir"+str(iter))
       # os.chdir("dir"+str(iter))
       # for i, j in enumerate(list):
         #  print(input_path + "/" + j)
          # image = cv2.imread( input_path + "/" + j )
          # filename = "image" + str(i) + ".jpg"
           #cv2.imwrite(filename, image)




#os.chdir("C://Users/vaibh/PycharmProjects/DIR/Duplicate_Image_Remover/unique_images")
#Unique Images
#for iter, list in enumerate(similar_lists):
   # img = list[0]
    #image = cv2.imread( input_path + "/" + img )
    #cv2.imwrite( "image" + str(iter) + ".jpg", image )
#base2 = "C://Users/vaibh/PycharmProjects/DIR/Duplicate_Image_Remover/scoree"

#Similar Images





