# mathgenerator
A program to generate math problems in a pretty format

based on a template provided by /u/lanemik on reddit

# Running

'''python3 mathgenerator.py'''

When it's done:

'''latex worksheet.tex'''

To print, open in something that can view dvi files. eg:

'''okular worksheet.dvi'''

To modify things for your own use, here are some of the places you will want to edit things:

\\textsc{{Scarlett's Math Problems}} \\\\  

That will be the title of your page. You might also want to edit "Teacher's Name" below that.

The following lines may look different by the time you get here. But they are accurage as of commit <a href="https://github.com/djotaku/mathgenerator/tree/90a09d8911b0f05ebb43d6b556e8c8f5156f3652">90a09d8</a>. Or you can try and find the modified lines. Shouldn't be hard.

On the line: 

 (a,b,c,d,e,f) = random.choices(range(1, 101), k=6)
 
 You will want to edit the range based on how high you want the numbers to go.
 
 On the line:
 
return f'\\threeprobs{{\\divi{{{a}}}{{{b}}}}}{{\\mult{{{c}}}{{{d}}}}}{{\\addi{{{e}}}{{{f}}}}}'

Change "divi", etc based on the mix of types of questions you want. As written above it will do one division problem, one multiplication problem, and one addition problem.
