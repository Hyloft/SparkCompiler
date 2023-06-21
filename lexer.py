# not works with other lexers. it just finds what the line does.

# expected output: {'line':line,'code':text,'token':token.token,'space':spaces}

from tokens import tokens_with_order
import re

class Lexer():
    
    def __init__(self,pharagraph:str):
        self.all_text = pharagraph
    
    def get_start_spaces(self,text):
        space_count = 0
        for char in text:
            if char == ' ': space_count+=1
            else: break
        return space_count
    
    def find_token_type(self,text):
        for token in tokens_with_order:
            if token.match_token(text) == True:
                return token
        return False
    
    def no_token_error(self,line,text):
        raise Exception(f'line {line} have no matching tokens. `{text}`')
    
    def analyse_lexeme_line(self,text,line):
        if text == '': return {'line':line,'code':'','token':'NULL_LINE','space':0}
        token = self.find_token_type(text)
        if token == False: self.no_token_error(line,text)
        spaces = self.get_start_spaces(text)
        text = re.sub('( +)',' ',text).strip()
        return {'line':line,'code':text,'token':token.token,'space':spaces}
    
    def analyse_lexeme(self):
        line_texts = self.all_text.split('\n')
        result = []
        for idx,line in enumerate(line_texts):
            result.append(self.analyse_lexeme_line(line,idx+1))
        return result