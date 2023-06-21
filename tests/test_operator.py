from operators import Operator

def test_interprete_one_operator():
    op = Operator('^','**')
    interpreted_text = op.interprete_operator('3^5')
    print(interpreted_text)
    assert interpreted_text == '3**5'
    
def test_interprete_two_operator():
    op = Operator(['^','ust'],'**')
    interpreted_text = op.interprete_operator('3^5 + 4ust2')
    print(interpreted_text)
    assert interpreted_text == '3**5 + 4**2'
    
def test_interprete_tricky_operator(): # in case of changes in interprete function.
    op = Operator('^^','**')
    interpreted_text = op.interprete_operator('3^^^5')
    print(interpreted_text)
    assert interpreted_text == '3**^5'