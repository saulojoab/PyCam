#coding: utf-8

import cv2, time

# Creating the video object.
video = cv2.VideoCapture(1);
a = 0;

# Dimensions of the video.
frame_width = int(video.get(3));
frame_height = int(video.get(4));

print("Video dimension is: " + str(frame_width) + "x" + str(frame_height));

answer = str(input("Wanna record (y/n)? "));

# VideoWriter.
cap = None;
if (answer == "y"):
    filename = str(input("Name your video file: "));
    cap = cv2.VideoWriter((filename + ".mov"), cv2.VideoWriter_fourcc('M','J','P','G'), 30, (frame_width, frame_height));

# Setting our capture command.
captureStarted = False;
while True:
    a = a + 1;
    # Getting the read status and the frame (image).
    check, frame = video.read();

    # Printing them.
    print(check);
    print(frame);

    # Showing the frame.
    cv2.imshow("Camera Feed", frame);

    if captureStarted and cap != None:
        print("Recording! Current frame: " + str(a));
        cap.write(frame);
    else:
        print("Not recording!");

    # Any key to leave.
    key = cv2.waitKey(1);

    if key == ord('q'):
        break;
    # Starting/stopping recording on button press.
    elif key == ord('r'):
        captureStarted = not captureStarted;

print("Total frames: " + str(a));
# Stop the camera
video.release();
if cap != None:
    cap.release();

cv2.destroyAllWindows();