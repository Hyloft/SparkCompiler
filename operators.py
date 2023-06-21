import re
from helpers import replacer

class Operator():
    def __init__(self,operator,python_equilavent):
        self.operator = operator
        self.python_equilavent = python_equilavent
    
    def interprete_operator(self,text:str)->str:
        for operator in (self.operator if type(self.operator)==list else [self.operator]):
            text=text.replace(operator,self.python_equilavent)
        return text
        
### Arithmetic Operators

power = Operator('^','**')

def power_interprete(text:str)->str:
    reg = r'[/^]+[0-9]'
    ids = [(m.start(0), m.end(0)) for m in re.finditer(reg,text)]
    for idx in ids:
        text = text[:idx[0]] + text[idx[0]:idx[1]].replace('^','**') + text[idx[1]:]
    return text

power.interprete_operator = power_interprete

arithmetic_operators = [power]

### Comparison Operators

equal = Operator('=','==')
def equal_interprete(text:str)->str:
    reg = r'(\w|\s)\=(\w|\s)'
    ids = [(m.start(0), m.end(0)) for m in re.finditer(reg,text)]
    for idx in ids:
        text = text[:idx[0]] + text[idx[0]:idx[1]].replace('=','==') + text[idx[1]:]
    return text

equal.interprete_operator = equal_interprete

not_equal = Operator('^=','!=')

comparison_operators = [equal,not_equal]

## Logical Operators

_not = Operator('^','~')

def _not_interprete(text:str)->str:
    reg = r'[/^]+[a-zA-Z]\w+'
    ids = [(m.start(0), m.end(0)) for m in re.finditer(reg,text)]
    for idx in ids:
        text = text[:idx[0]] + '(not ' + text[idx[0]+1:idx[1]]+')' + text[idx[1]:]
    return text

_not.interprete_operator = _not_interprete

_not_text = Operator('NOT','not')
_and = Operator('AND','and')
_or = Operator('OR','or')

logical_operators = [_not,_not_text,_and,_or]
