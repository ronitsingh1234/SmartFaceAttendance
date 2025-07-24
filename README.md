![image alt](https://github.com/ronitsingh1234/SmartFaceAttendance/blob/main/Screenshot%202025-07-24%20130729.png?raw=true)
Description:
This is the main GUI window of the Face Recognition Attendance System, built using Tkinter. It serves as the homepage with buttons for key functionalities like:
Student Details: Register or view student information.
Face Detector: Launches the face detection module.
Attendance: Opens attendance records.
Train Data: Triggers the model training using collected images.
Photos: Opens the dataset directory.
Exit: Closes the application


![image alt](https://github.com/ronitsingh1234/SmartFaceAttendance/blob/main/Screenshot%202025-07-24%20130750.png?raw=true)
Description:
This shows the "Student Details" window where users can register student information. It typically includes fields like:
Student ID
Name
Roll number
Email
Phone number
Department and Course
There’s also a photo sample section to collect images for training.

![image alt](https://github.com/ronitsingh1234/SmartFaceAttendance/blob/main/Screenshot%202025-07-24%20130905.png?raw=true
)
![image alt](https://github.com/ronitsingh1234/SmartFaceAttendance/blob/main/Screenshot%202025-07-24%20131000.png?raw=true)

![image alt](https://github.com/ronitsingh1234/SmartFaceAttendance/blob/main/Screenshot%202025-07-24%20131020.png?raw=true)
Description:
This is the Face Detector module in action.
When launched, it activates the webcam and detects faces in real-time using OpenCV. Once a face is detected, it automatically saves the images in a structured folder for model training.
This shows the real-time face recognition process.
When the face recognition module is run, it detects and identifies registered faces using the trained model. If a match is found, it displays the student’s name and ID on the screen and logs attendance.


![image alt](https://github.com/ronitsingh1234/SmartFaceAttendance/blob/main/Screenshot%202025-07-24%20131104.png?raw=true)
Description:
This is the Train Data process running in the console.
When clicked, it uses the images stored in the dataset folder to train a face recognition model using OpenCV’s LBPH (Local Binary Pattern Histogram) algorithm and saves the model as a .yml file.



![image alt](https://github.com/ronitsingh1234/SmartFaceAttendance/blob/main/Screenshot%202025-07-24%20131123.png?raw=true)
Description:
This screenshot shows the "Photos" button functionality, which opens the file explorer to the folder where all captured images (data/ or dataset/) are stored. This directory contains the training images for each student.


![image alt](https://github.com/ronitsingh1234/SmartFaceAttendance/blob/main/Screenshot%202025-07-24%20131143.png?raw=true)
![image alt](https://github.com/ronitsingh1234/SmartFaceAttendance/blob/main/Screenshot%202025-07-24%20131200.png?raw=true)
Description:
This is the "Attendance" window, which displays the attendance log in tabular form.
It shows records such as:
Student ID
Name
Time
Date
Attendance status
It fetches data from a CSV file where attendance is automatically marked when a known face is detected.
