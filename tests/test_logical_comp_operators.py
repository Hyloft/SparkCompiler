from operators import logical_operators,comparison_operators

def test_logical_operators():
    text = 'IF (x12 AND (bool_deneme OR c2)) NOT ^C23'
    expected_text = 'IF (x12 and (bool_deneme or c2)) not (not C23)'
    for op in logical_operators:
        text = op.interprete_operator(text)
    assert text == expected_text
    
def test_comparison_operators():
    text = 'x=12 or b==45 and 2^=2; c:=3'
    expected_text = 'x==12 or b==45 and 2!=2; c:=3'
    for op in comparison_operators:
        text = op.interprete_operator(text)
    assert text == expected_text