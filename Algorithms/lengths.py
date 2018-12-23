'''
26. ori monakveti shemodis (2, 7) anu x gherdze 2dan 7is chatvlit.
'''

def main(cords):
    result = []
    start = 0
    end = 0
    for cord in cords:    
        if cord[0] <= start:
            start = cord[0]
        elif cord[0] >= end:
            
        
            