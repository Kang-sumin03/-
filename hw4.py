def rep_char(c,n):
    print(c*n)

def draw_line_string():
    msg1=('Hello '+name)
    msg2=('Welcom to Seoul.')
    
    if len(msg1)>len(msg2):
        nstr=len(msg1)
    else :
        nstr=len(msg2)


    rep_char('-', nstr*2+4)
    print(f'    {msg1}    ')
    print(f'    {msg2}    ')
    rep_char('-', nstr*2+4)


name=input('Input his/her name:')
draw_line_string()
