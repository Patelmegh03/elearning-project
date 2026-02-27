import cv2
import os

def Create_Folder (name):
    Folder_path = os.path.join(os.getcwd(),name)
    os.makedirs (Folder_path,exist_ok=True)
    return Folder_path

def Capture_image(Folder_path,inter=3,num_img=5):
    cam = cv2.VideoCapture(0)
    for i in range(num_img):
        r,frame = cam.read()
        cv2.imshow("Photo",frame)
        cv2.imwrite(f"{Folder_path}/image-{i+1}.jpg",frame)
        cv2.waitKey(inter*1000)


if __name__ == '__main__':
    Name = input("Enter Folder Name:")
    Folder_path = Create_Folder(Name)
    Capture_image(Folder_path)