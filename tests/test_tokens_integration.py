from tokens import tokens_with_order

def handle_tokens(text):
    for token in tokens_with_order:
        if token.match_token(text) == True:
            return token
    return False

def test_if_token():
    text = 'IF x<15 THEN'
    token = handle_tokens(text)
    assert token.token == 'IF'

def test_onleine_if_token():
    text = 'IF x<15 THEN x<-34 ENDIF'
    token = handle_tokens(text)
    assert token.token == 'ONE_LINE_IF'
    
def test_assign_array():
    text = 'newArray2[3,4]'
    token = handle_tokens(text)
    assert token.token == 'ASSIGNMENT_ARRAY'
    
def test_assign():
    text = 'MynewInt <- 12'
    token = handle_tokens(text)
    assert token.token == 'ASSIGNMENT'

def test_assign_2():
    text = 'x<-2 c <- 4'
    token = handle_tokens(text)
    assert token.token == 'ASSIGNMENT'