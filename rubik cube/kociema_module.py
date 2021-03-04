import kociemba
import cv2
import numpy as np
import time
from rubik_solver import utils
from drawLine import *
import winsound
def kociema(color_list):
	
	cube = ""
	for i in color_list:
		cube = cube + i
	
	a= utils.solve(cube, 'Kociemba')
	result_string = a
	
	for i in result_string:
		i = str(i)
		if len(i) > 1:
			if i[1] == '2':
				
				s = i[0]
				index = result_string.index(i)
				result_string.remove(i)
				result_string.insert(index,s)
				result_string.insert(index,s)
			elif i == "B'":
				index = result_string.index(i)
				result_string.remove(i)
				# replace B' with 3 instructions B' ==> up, right, down
				result_string.insert(index, "up")
				result_string.insert(index, "U'")
				result_string.insert(index, "down")

		elif i == "B":
			index = result_string.index(i)
			result_string.remove(i)
			# replace B with 3 instructions B ==> up, left, down
			result_string.insert(index, "up")
			result_string.insert(index, "U")
			result_string.insert(index, "down")
		else:
			continue

	#import pdb; pdb.set_trace()

	print(result_string)
	frame_idx = 0
	frame_reset_cnt = 120
	result_index = 0
	cubeshape = 180
	cubesize = 3
	startpoint = (100, 100)

	cap = cv2.VideoCapture(0)
	while True:
		cubeImg = np.zeros((480,640))
		res, cubeImg = cap.read()

		cv2.waitKey(10)
		cv2.imshow("cube",cubeImg)
		drawCube(cubeImg,cubeshape,cubesize,startpoint)

		if result_index >= len(result_string) - 1:
			cv2.putText(cubeImg, "DONE!!! Solved the Cube", (int(cubeImg.shape[1]/4), 30), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0,255,0))
			cv2.imshow("cube", cubeImg)
			if cv2.waitKey(10) == ord('q'):
				break
			continue

		frame_idx += 1
		if frame_idx > frame_reset_cnt:
			winsound.Beep(500,300)
			cv2.putText(cubeImg, "next", (int(cubeImg.shape[1]/4), 30), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0,255,0))
			
			result_index += 1
			frame_idx = 0

		result = result_string[result_index]
		if result == "D":
			arrowlines(cubeImg,(2,0),(2,2), cubeshape, cubesize)

		elif result == "D'":
			arrowlines(cubeImg,(2,2),(2,0), cubeshape, cubesize)
		
		elif result == 'F':
			rotation(cubeImg)

		elif result == "F'":
			antirotation(cubeImg)

		elif result == 'R':
			arrowlines(cubeImg,(2,2),(0,2), cubeshape, cubesize)

		elif result == "R'":
			arrowlines(cubeImg,(0,2),(2,2), cubeshape, cubesize)

		elif result == 'U':
			arrowlines(cubeImg,(0,2),(0,0), cubeshape, cubesize)

		elif result == "U'":
			arrowlines(cubeImg,(0,0),(0,2), cubeshape, cubesize)
		
		elif result == 'L':
			arrowlines(cubeImg,(0,0),(2,0), cubeshape, cubesize)

		elif result == "L'":
			arrowlines(cubeImg,(2,0),(0,0), cubeshape, cubesize)

		elif result == "down":
			arrowlines(cubeImg,(0,0),(2,0), cubeshape, cubesize)
			arrowlines(cubeImg,(0,1),(2,1), cubeshape, cubesize)
			arrowlines(cubeImg,(0,2),(2,2), cubeshape, cubesize)

		elif result == "up":
			arrowlines(cubeImg,(2,0),(0,0), cubeshape, cubesize)
			arrowlines(cubeImg,(2,1),(0,1), cubeshape, cubesize)
			arrowlines(cubeImg,(2,2),(0,2), cubeshape, cubesize)

		elif result == "right":
			arrowlines(cubeImg,(0,0),(0,2), cubeshape, cubesize)
			arrowlines(cubeImg,(1,0),(1,2), cubeshape, cubesize)
			arrowlines(cubeImg,(2,0),(2,2), cubeshape, cubesize)

		elif result == "left":
			arrowlines(cubeImg,(0,2),(0,0), cubeshape, cubesize)
			arrowlines(cubeImg,(1,2),(1,0), cubeshape, cubesize)
			arrowlines(cubeImg,(2,2),(2,0), cubeshape, cubesize)

		cv2.imshow("cube", cubeImg)

		if cv2.waitKey(10) == ord('q'):
			break
