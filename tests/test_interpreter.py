from interpreter import Interpreter
import numpy as np

# DEFINITION TESTS
def test_interpreter_arr_deff():
    code = 'NewArray[3,4]\nnewArray2[4,5]'
    ip = Interpreter(code)
    interpreted = ip.interpreted_code
    assert interpreted == 'NewArray=np.zeros((3 +1,4 +1))\nnewArray2=np.zeros((4 +1,5 +1))'
    
def test_interpreter_arr_deff_compiled():
    code = 'NewArray[3,4]\nnewArray2[4,5]'
    ip = Interpreter(code)
    interpreted = ip.interpreted_code
    exec(interpreted, globals())
    assert NewArray[0,0] == 0
    
def test_interpreter_deff_compiled():
    code = 'x<-5;y<--12;z<-45;'
    ip = Interpreter(code)
    interpreted = ip.interpreted_code
    exec(interpreted, globals())
    assert (x ==5 ) & (y==-12) & (z==45)
    
## IF AND DEFINITION
def test_if_def():
    code = 'IF 5^=23 THEN\n  x<-45\n  NewArray[3,4]\n  NewArray[2,2]<-x\nENDIF'
    ip = Interpreter(code)
    interpreted = ip.interpreted_code
    exec(interpreted, globals())
    assert NewArray[2,2] == 45

def test_if_else():
    code = 'IF 5^=23 THEN\n  x<-45\n  NewArray[3,4]\n  NewArray[2,2]<-x\n  IF NewArray[2,2] = 0 THEN\n    y<-33\n  ELSE IF NewArray[2,2] = 45 THEN\n    y<-0\n  ELSE\n    PRINT "y:",y\n  ENDIF\nENDIF'
    ip = Interpreter(code)
    interpreted = ip.interpreted_code
    exec(interpreted, globals())
    assert y == 0

## loop tests
def test_loops():
    code = """
x<-3
y<-23
IF x<5 THEN
    y<-5
ENDIF

FOR I<-5 TO 50 DO
    y<-y+1
REPEAT

WHILE y>10 DO
    y<-y-1
PRINT 'y sayisi' , y
    """
    ip = Interpreter(code)
    interpreted = ip.interpreted_code
    exec(interpreted, globals())
    assert y == 10