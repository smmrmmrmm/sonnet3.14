# sonnet 3.14159 (thon)

the_canvas = []
the_counter = 0

for i in range(1062):
    if (i%30) == 21:
    
        if 12 > the_counter > 6:
            line = '.'*14 + '#'*12 + '.'*9    
        elif 20 > the_counter > (20-4):
            line = '.'*19 + '#'*16
        else:
            line = '.'*35
            
        line = line + line[::-1]
        
        the_counter += 1  
        the_canvas.append(line)

for part in the_canvas:
    print(part)


print("Who said I can't make code into art?")