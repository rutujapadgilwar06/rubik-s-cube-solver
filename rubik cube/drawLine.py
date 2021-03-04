
import cv2
import numpy as np


cubecolor = (0,0,0)
cubelineSize = 2

def drawCube(img, cubesize, cubeshape, start_point): # start_poing (100, 100)
    cubecell = int(cubesize / cubeshape)
    # draw horizontal lines first
    for i in range(cubeshape + 1):
        start_line = (start_point[0], start_point[1] + i * cubecell)
        end_line = (start_point[0] + cubesize, start_point[1] + i * cubecell)
        cv2.line(img, start_line, end_line, cubecolor, 2)
    
    for i in range(cubeshape + 1):
        start_line = (start_point[0] + i * cubecell, start_point[1])
        end_line = (start_point[0] + i * cubecell, start_point[1] + cubesize)
        cv2.line(img, start_line, end_line, cubecolor, cubelineSize)

    return img

def rotation(cubeImg):
	arrowlines(cubeImg, (0,1), (1,2), 180, 3)
	arrowlines(cubeImg, (1,2), (2,1), 180, 3)
	arrowlines(cubeImg, (2,1), (1,0), 180, 3)
	arrowlines(cubeImg, (1,0), (0,1), 180, 3)

def antirotation(cubeImg):
	arrowlines(cubeImg, (0,1), (1,0), 180, 3)
	arrowlines(cubeImg, (1,0), (2,1), 180, 3)
	arrowlines(cubeImg, (2,1), (1,2), 180, 3)
	arrowlines(cubeImg, (1,2), (0,1), 180, 3)


def arrowlines(cubeImg,start_idx_box,end_idx_box,imgsize, cubesize): # start_idx_box start from 1


	start_idx_box_y = start_idx_box[0]
	start_idx_box_x = start_idx_box[1]

	end_idx_box_y = end_idx_box[0]
	end_idx_box_x = end_idx_box[1]

	boxsize = imgsize / cubesize
	box_center_x = boxsize / 2
	box_center_y = boxsize / 2
	start_x = 100 # make function arguement later
	start_y = 100

	#start_point_x = int(start_idx_box * box_center_x + boxsize % 2)
	start_point_x = int(start_x + start_idx_box_x * boxsize + box_center_x)
	start_point_y = int(start_y + start_idx_box_y * boxsize + box_center_y)

	end_point_x = int(start_x + end_idx_box_x * boxsize + box_center_x)
	end_point_y = int(start_x + end_idx_box_y * boxsize + box_center_y)
	start_point = (start_point_x, start_point_y)
	end_point = (end_point_x, end_point_y)
	
	cv2.arrowedLine(cubeImg, start_point, end_point, (0,0,0),2) # red
	return cubeImg
