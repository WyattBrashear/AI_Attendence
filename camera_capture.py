import cv2
import os
import random
import time

stu_amount = int(input("How many students are you adding in today? "))
for i in range(stu_amount):
    # Create a VideoCapture object (0 for default webcam)
    cap = cv2.VideoCapture(0)
    tval = ["train", "val", "test"]
    student_class = str(input("What student are you adding in today? "))
    frame_amount = int(input("Please enter (As an integer) how many frames to capture. (multiplied by 3 for data) ")) * 3
    # Check if camera opened successfully
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        exit()
    if os.path.exists("classroom_dataset"):
        os.mkdir(f"{os.getcwd()}\classroom_dataset\{tval[0]}\{student_class}")
        os.mkdir(f"{os.getcwd()}\classroom_dataset\{tval[1]}\{student_class}")
        os.mkdir(f"{os.getcwd()}\classroom_dataset\{tval[2]}\{student_class}")
    else:
        os.mkdir(f"{os.getcwd()}\classroom_dataset")
        os.mkdir(f"{os.getcwd()}\classroom_dataset\{tval[2]}")
        os.mkdir(f"{os.getcwd()}\classroom_dataset\{tval[1]}")
        os.mkdir(f"{os.getcwd()}\classroom_dataset\{tval[0]}")
        os.mkdir(f"{os.getcwd()}\classroom_dataset\{tval[0]}\{student_class}")
        os.mkdir(f"{os.getcwd()}\classroom_dataset\{tval[1]}\{student_class}")
        os.mkdir(f"{os.getcwd()}\classroom_dataset\{tval[2]}\{student_class}")
    print(f"Image capture is about to begin for: {student_class}. Please make sure to move your head around for best results.")
    time.sleep(1)
    print("Image capture is beggining in 3.")
    time.sleep(1)
    print("Image capture is beggining in 2.")
    time.sleep(1)
    print(("Image capture is beggining in 1!"))

    # Capture a single frame
    for i in range(frame_amount):
        ret, frame = cap.read()

        # Check if frame captured successfully
        if not ret:
            print("Error: Could not capture frame.")
            cap.release()
            exit()

        # Split the captured images into train, val, and test
        if random.randint(0, 100) >= 85:
            if random.randint(1, 2) == 2: 
                cv2.imwrite(f"{os.getcwd()}\classroom_dataset\{tval[1]}\{student_class}\{student_class}{i}.jpg", frame)
                print(f"Validation image written to: {os.getcwd()}\classroom_dataset\{tval[1]}\{student_class}\{student_class}{i}.jpg")
            else:
                cv2.imwrite(f"{os.getcwd()}\classroom_dataset\{tval[2]}\{student_class}\{student_class}{i}.jpg", frame)
                print(f"Testing image written to: {os.getcwd()}\classroom_dataset\{tval[2]}\{student_class}\{student_class}{i}.jpg")
        else:
            cv2.imwrite(f"{os.getcwd()}\classroom_dataset\{tval[0]}\{student_class}\{student_class}{i}.jpg", frame)
            print(f"Training Image written to: {os.getcwd()}\classroom_dataset\{tval[0]}\{student_class}\{student_class}{i}.jpg")

    # Release the camera
    cap.release()

print("Image capture complete! feel free to export this dataset and get training!")
