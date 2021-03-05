# rubik's-cube-solver
A webcam-based 3x3x3 rubik's cube solver written in Python 3 and OpenCV by using kociemba module.
Given an image of cube face to webcam and solve the rubik cube.

## Installation
The package is hosted on PyPI.
```
$ pip install rubik_solver
$ pip install kociemba
```

## cube notation
The names of the facelet positions of the cube (letters stand for Up, Left, Front, Right, Back, and Down)
```
             |************|
             |*U1**U2**U3*|
             |************|
             |*U4**U5**U6*|
             |************|
             |*U7**U8**U9*|
             |************|
 ************|************|************|************
 *L1**L2**L3*|*F1**F2**F3*|*R1**R2**R3*|*B1**B2**B3*
 ************|************|************|************
 *L4**L5**L6*|*F4**F5**F6*|*R4**R5**R6*|*B4**B5**B6*
 ************|************|************|************
 *L7**L8**L9*|*F7**F8**F9*|*R7**R8**R9*|*B7**B8**B9*
 ************|************|************|************
             |************|
             |*D1**D2**D3*|
             |************|
             |*D4**D5**D6*|
             |************|
             |*D7**D8**D9*|
             |************|
   ```
             
   ### How To Use
   
   1. Run following file.
   ```
   $ rubik_cube_solver.py
   ```
   2. You must scan the sides in U,L,F,R,B,D  
   * (Upper center): YELLOW
   * (Left center): BLUE
   * (Front center): RED
   * (Right center): GREEN
   * (Back center): ORANGE
   * (Down center): WHITE
   3. Press "c" everytime to Scan cube face
   4. Press "s" to start process  
   
   
   ### rubik cube solver demo
   
https://user-images.githubusercontent.com/80000090/110075035-2e517480-7da8-11eb-860a-56b14897e0d7.mp4

             
 
