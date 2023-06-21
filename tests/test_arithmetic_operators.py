from operators import arithmetic_operators

def test_arithmetic_operators():
    t = '3^5 * 24 * (2^4) / 44 + 2 - 5'
    for op in arithmetic_operators:
        t = op.interprete_operator(t)
    assert t == '3**5 * 24 * (2**4) / 44 + 2 - 5'