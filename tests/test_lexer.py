from lexer import Lexer

def test_integration_lexer_tokens():
    text = "x<-2; c<-4;\nnewArr[3,4]\nFOR  k<-5   TO 10  DO\n  newArr[k,c]<-x\nREPEAT"
    expected=[
        {'line':1,'code':'x<-2; c<-4;','token':'ASSIGNMENT','space':0},
        {'line':2,'code':'newArr[3,4]','token':'ASSIGNMENT_ARRAY','space':0},
        {'line':3,'code':'FOR k<-5 TO 10 DO','token':'FOR','space':0},
        {'line':4,'code':'newArr[k,c]<-x','token':'ASSIGNMENT','space':2},
        {'line':5,'code':'REPEAT','token':'REPEAT','space':0},
    ]
    lexer = Lexer(text)
    res = lexer.analyse_lexeme()
    assert res == expected