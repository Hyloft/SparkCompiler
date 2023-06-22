import re

class Token():
    def __init__(self,token,regex,max_count=1):
        self.regex = regex if type(regex) == list else [regex]
        self.token = token
        self.max_count = [max_count] if type(max_count) != list else max_count
        self.check_error()
        
    def check_error(self):
        if len(self.max_count) != len(self.regex):
            raise Exception(f'"{self.token}" token error. max_count and regex size not match.')

    def match_token(self,text:str)->bool:
        text = text.strip()
        match = [False for i in self.regex]
        
        for i in range(0,len(self.regex)):
            reg = self.regex[i]
            if 0< len(re.findall(reg,text)) <=self.max_count[i]:
                match[i] = True
        
        return False if False in match else True

### IF    
IF = Token('IF',r'^(\s+)?(IF)\s')
ELSE_IF = Token('ELSE_IF',r'^(\s+)?(ELSE)\s\wF\s')
ELSE = Token('ELSE',r'ELSE$')
ENDIF = Token('ENDIF',r'ENDIF$')
ONE_LINE_IF = Token('ONE_LINE_IF',[IF.regex[0],ENDIF.regex[0]],max_count=[1,1])

### FOR
FOR = Token('FOR',r'^(\s+)?(FOR)\s')
REPEAT = Token('REPEAT',r'^(\s+)?REPEAT$')

### WHILE
WHILE = Token('WHILE',r'^(\s+)?(WHILE)\s')
END = Token('END',r'^(\s+)?END$')

### PRINT/READ
PRINT = Token('PRINT',r'^(\s+)?(PRINT)\s')
READ = Token('READ',r'^(\s+)?(READ)\s')

### ASSIGNMENT
ASSIGNMENT_ARRAY = Token('ASSIGNMENT_ARRAY',r'^(\s+)?\w+\[+[\d,]+\]$',max_count=255)
ASSIGNMENT = Token('ASSIGNMENT',r'<-',max_count=255)

### NULL LINES
NULL_LINE = Token('NULL_LINE',r'^(\s+)$')

tokens_with_order = [
    ONE_LINE_IF,IF,ELSE,ELSE_IF,ENDIF,
    WHILE,END,
    FOR,REPEAT,
    PRINT, READ,
    ASSIGNMENT, ASSIGNMENT_ARRAY ,
    NULL_LINE   
]