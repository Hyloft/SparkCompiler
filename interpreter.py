#purpose of this program is translate sparks lang to python lang
import sys

from lexer import Lexer

import re

from operators import arithmetic_operators,logical_operators,comparison_operators

import numpy as np

reg_arr_def = r'\w+\[+[0-9,]+\]'

reg_arr = r'\w+\[+[\w+,]+\]'

class Interpreter():
    
    def __init__(self,code):
        self.lexer = Lexer(code)
        self.lexemes = self.lexer.analyse_lexeme()
        
        self.token_fn = {
            'IF':self.if_line,
            'ELSE_IF':self.else_if_line,
            'ELSE':self.else_line,
            'ENDIF':self.endif_line,
            'ONE_LINE_IF':self.oneline_if_line,
            'FOR':self.for_line,
            'REPEAT':self.repeat_line,
            'WHILE':self.while_line,
            'END':self.end_line,
            'PRINT':self.print_line,
            'READ':self.read_line,
            'ASSIGNMENT_ARRAY':self.assignment_array_line,
            'ASSIGNMENT':self.assignment_line,
            'NULL_LINE':self.null_line
        }
        
        self.interpreted_code = self.interprete_all()

    def interprete_all(self):
        txt = []
        for lexeme in self.lexemes:
            # print(lexeme)
            fn = self.token_fn[lexeme['token']]
            lexeme['code'] = self.handle_operators(arithmetic_operators,lexeme['code'])
            txt.append((' '*lexeme['space'])+fn(lexeme))
        return '\n'.join(txt)
    
    ##HELPERS
    def handle_operators(self,operators,text):
        for op in operators:
            text = op.interprete_operator(text)
        return text
    
    def interprete_array_definition(self,text):
        ids = [(m.start(0), m.end(0)) for m in re.finditer(reg_arr_def,text)]
        for idx in ids:
            text = text[:idx[0]] + text[idx[0]:idx[1]].split('[')[0]+'=' + 'np.zeros((' + ','.join([t + ' +1' for t in text[idx[0]:idx[1]].split('[')[1][:-1].split(',')]) + '))' + text[idx[1]:]
        return text
    
    # def interprete_arrays(self,text):
    #     ids = [(m.start(0), m.end(0)) for m in re.finditer(reg_arr_def,text)]
    #     for idx in ids:
    #         text = text[:idx[0]] + text[idx[0]:idx[1]].split('[')[0]+'=' + 'np.array(' + text[idx[0]:idx[1]].split('[')[1][:-1] + ')' + text[idx[1]:]
    #     return text
    
    ##ALL FN
    def null_line(self,lexeme):
        return ''
    
    def assignment_line(self,lexeme):
        return lexeme['code'].replace('<-','=')
    
    def assignment_array_line(self,lexeme):
        return self.interprete_array_definition(lexeme['code'])
    
    def oneline_if_line(self,lexeme):
        text:str = lexeme['code']
        text = text.replace('IF','if').replace('THEN',':').replace('ENDIF',';')
        text = self.handle_operators([*comparison_operators,*logical_operators],text).replace('<-','=')
        return text
    
    def if_line(self,lexeme):
        text:str = lexeme['code']
        text = text.replace('IF','if').replace('THEN',':')
        text = self.handle_operators([*comparison_operators,*logical_operators],text)
        return text
    
    def else_if_line(self,lexeme):
        text:str = lexeme['code']
        text = text.replace('ELSE IF','elif').replace('THEN',':')
        text = self.handle_operators([*comparison_operators,*logical_operators],text)
        return text
    
    def else_line(self,lexeme):
        return 'else:'
    
    def endif_line(self,lexeme):
        return ''
    
    def while_line(self,lexeme):
        text:str = lexeme['code']
        text = text.replace('WHILE','while').replace('DO',':')
        text = self.handle_operators([*comparison_operators,*logical_operators],text)
        return text
    
    def end_line(self,lexeme):
        return ''
    
    def for_line(self,lexeme):
        text:str = lexeme['code']
        fs = text.split('<-')
        var = fs[0].split('FOR')[1]
        ss = fs[1].split('TO')
        n1 = ss[0]
        n2 = ss[1].split('DO')[0]
        text = f'for {var} in range({n1},{n2}+1):'
        return text
    
    def repeat_line(self,lexeme):
        return ''
    
    def print_line(self,lexeme):
        text:str = lexeme['code']
        text_s = text.split('PRINT')
        text = f'print({text_s[1]})'
        return text
    
    def read_line(self,lexeme):
        text:str = lexeme['code']
        text_s = text.split('READ')
        text = f'{text_s[1].strip()} = int(input())'
        return text
        
def compile_file(filename):
    code = open(filename,'r',encoding='utf-8')
    interpreter = Interpreter(code.read())
    python_code = interpreter.interpreted_code
    exec(python_code)

if __name__ == '__main__':
    try:
        if len(sys.argv) > 1:
            compile_file(sys.argv[1])
        else:
            compile_file('code.sparks')
    except Exception as err:
        print(err)
    ext = input('\n\n~~press ENTER to exit~~')