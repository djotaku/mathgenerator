# mathgenerator
A program to generate math problems in a pretty format

based on a template provided by /u/lanemik on reddit

# Running

python3 mathgenerator.py

When it's done:

latex worksheet.tex

To print, open in something that can view dvi files. eg:

okular worksheet.dvi

# Modifications

To modify things for your own use, here are some of the places you will want to edit things:

\\textsc{{Scarlett's Math Problems}} \\\\  

That will be the title of your page. You might also want to edit "Teacher's Name" below that.

## If you don't care about whether the subtraction problems yield negative numbers

If you uncomment the line: 

 (a,b,c,d,e,f) = random.choices(range(1, 101), k=6)
 
 You will want to edit the range based on how high you want the numbers to go.
 
 Then you can modify the return to look like:
 
return f'\\threeprobs{{\\divi{{{a}}}{{{b}}}}}{{\\mult{{{c}}}{{{d}}}}}{{\\addi{{{e}}}{{{f}}}}}'

Change "divi", etc based on the mix of types of questions you want. As written above it will do one division problem, one multiplication problem, and one addition problem.

## Otherwise

In the subtraction function change your ranges as appropriate, but leave the second part of "b" as "a+1" so that you always have a positive subtraction problem.

Then modify the addition choices.

Currently not supporting multiplication or division in this model. See above if you want to turn it back to the version where it picks random numbers for all arithmatic (which can end up with negative subtraction) if you want to do that.
