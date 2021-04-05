import face_recognition
import os
import cv2

known_DIR = "knownface"
tolerance = 0.6 
frame = 3
font = 1
Model = "cnn"

video = cv2.VideoCapture(-1)
print("loading known faces")
knownface = []
knownname = []

for name in os.listdir(known_DIR):
	for filename in os.listdir(f"{known_DIR}/{name}"):
		image = face_recognition.load_image_file(f"{known_DIR}/{name}/{filename}")
		encoding = face_recognition.face_encodings(image)[0]
		knownface.append(encoding)
		knownname.append(name)
print("loading unknown faces")

while True:
	ret, image = video.read()
	locations = face_recognition.face_locations(image, model=Model)
	encoding = face_recognition.face_encodings(image, locations) 
	for face_encoding, face_location in zip(encoding, locations):
		result = face_recognition.compare_faces(knownface, face_encoding, tolerance)
		match = None 

		if True in result:
			match = knownname[result.index(True)]
			print(f"Match found: {match}")
			topleft = (face_location[3], face_location[0])
			bottomright = (face_location[1], face_location[2])
			color = [50, 50, 50]
			cv2.rectangle(image, topleft, bottomright, color, frame)
			
			topleft = (face_location[3], face_location[2])
			bottomright = (face_location[1], face_location[2]+22)
			cv2.rectangle(image, topleft, bottomright, color, cv2.FILLED)
			cv2.putText(image, match, (face_location[3]+10, face_location[2]+15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255),font)
	cv2.imshow(filename, image)
	if cv2.waitKey(1) & 0xFF == ord("q"):
		break

# try:
# 	ret, image = video.read()
# 	small = cv2.resize(frame, (0, 0), fx=0.25, fy-0.25)

# except Exception as e:
# 	print(str(e)) 