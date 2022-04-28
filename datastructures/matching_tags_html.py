def is matched html(raw):
S = ArrayStack( )
j = raw.find( < ) # find first \u2019<\u2019 character (if any)
while j != \u22121:
    k = raw.find( > , j+1) # find next \u2019>\u2019 character7 if k == \u22121:
    return False # invalid tag
    tag = raw[j+1:k] # strip away < >
    if not tag.startswith( / ): # this is opening tag
    S.push(tag)
    else: # this is closing tag
    if S.is empty( ):
    return False # nothing to match with
    if tag[1:] != S.pop( ):
    return False # mismatched delimiter
    j = raw.find( < , k+1) # find next \u2019<\u2019 character (if any)
 return S.is empty( ) 