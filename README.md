
# Image Similarity Score

This is a Image Similarity Project which compares a file of images from a master image.
It gives back the compared image with the given 'Similarity Score' on top of the Image.



I have used OpenCV in this code and in that i have used its SSIM ( STructural Similarity Index) ,in which it quantifies the image quality degradation that is caused by processing such as data compression or by losses in data transmission. This metric is basically a full reference that requires 2 images from the same shot, this means 2 graphically identical images to the human eye. The second image generally is compressed or has a different quality, which is the goal of this index.




## Working

I have a file and read all of its paths in 2 seperate ways for each master file and file of images.
After converting them in the same black and white photos , I start a loop which helps in comparing each image with the master image and storing in dictionary's.

After that i have printed each image in a line between the respective score's of 
(50%-60%) , (60%-70%) , (70%-80%) , (Above 80%).

![image](https://user-images.githubusercontent.com/87512533/181227280-39351952-dc76-4ec5-a867-0dd9c26f7a0d.png)


Then i have created a table to show the maximum similarity and minimum similarity as well as number of images in each of the segregation given above.

![image](https://user-images.githubusercontent.com/87512533/181227414-19c470ab-63ec-4847-923d-8a037f0396c0.png)

Then it will also make a different directory for the Images with their similarity score with the master image on top of the image.

![image](https://user-images.githubusercontent.com/87512533/181227780-423f0204-ef4f-490d-9435-f6e534a17898.png)

You can find the file in Scoree folder inside Duplicate Image Removal.

## Usage

1.Click on Duplicate Image Remover in Master branch

2.The Testing folder contains the "Master image" which will be compared with the file of images.

3.Sparsh/87_-312_372 File contains the list of images to be comapred with the Master Image.

4.Clicking on the Similarityscore.py will give us our required code with the explanation given in the above compartment of WORKING.

5.A directory of images with their similarity score is made , which u can see in the scoree folder in which under dir0 it will be visible.
