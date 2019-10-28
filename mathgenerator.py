import random

latex_template = """%%----------LaTeX template for teachers-----------------------------%%
%%----------Samuel S. Watson----------------------------------------%% 
%%----------January 2013--------------------------------------------%% 

\\documentclass[12pt]{{article}} % Specifies font size

%----------------PACKAGES-------------------------------------------%%
\\usepackage[margin=1in]{{geometry}} % Sets all four margins to 1 inch
\\usepackage[pdftex]{{graphicx}} % Allows inclusion of image files
\\usepackage{{amssymb}} % Access to extra math symbols
\\usepackage{{amsmath}} % Access to extra math symbols
\\usepackage{{wrapfig}} % Allows wrapping of text around figures
\\usepackage{{calc}} % Gives access to a basic calculator 
%-------------------------------------------------------------------%%

%----------------COMMANDS-------------------------------------------%%
\\newcommand\\blank{{\\underline{{\\hspace{{2cm}}}}}} % Gives a blank 
\\newcounter{{prob}} % A new counter for current problem number
\\setcounter{{prob}}{{1}} % Start the counter at the value 1
\\newcommand\\itm{{
\\fbox{{\\textbf{{\\theprob}}}} \\refstepcounter{{prob}}
}} % Calls problem number
\\newcommand{{\\problem}}[1]{{\\makebox[0.5cm]{{\\itm}}   
  \\begin{{minipage}}[t]{{\\textwidth-0.5cm}} #1 \\end{{minipage}} 
}} % An environment for a problem statement on or more lines
\\newcommand{{\\pairofprobs}}[2]{{
  \\begin{{minipage}}[t]{{0.5\\textwidth}}\\itm #1 \\end{{minipage}} 
  \\begin{{minipage}}[t]{{0.5\\textwidth}}\itm #2 \\end{{minipage}} 
}} % Fits two problems on a line
\\newcommand{{\\threeprobs}}[3]{{
\\begin{{minipage}}[t]{{0.31\\textwidth}}\\itm #1 \\end{{minipage}} \\hfill
 \\begin{{minipage}}[t]{{0.31\\textwidth}}\\itm #2 \\end{{minipage}} \\hfill 
 \\begin{{minipage}}[t]{{0.31\\textwidth}}\\itm #3 \\end{{minipage}}
}} % Fits three problems on a line
\\newcounter{{choice}} % Counter for multiple choice problems 
\\setcounter{{choice}}{{1}} % Start the counter at the value 1
\\newcommand\\achoice{{
(\\alph{{choice}}) \\stepcounter{{choice}}
}} % Generates letter for multiple choice option
\\newcommand{{\\answers}}[5]{{\\vspace*{{-7mm}} 
  \begin{{tabular}}{{l@{{\hspace{{1mm}}}}p{{0.9\\textwidth}}}}
    \\achoice & #1 \\\\ \\achoice & #2 \\\\ \\achoice & #3 \\\\ 
    \\achoice & #4 \\\\ \\achoice & #5 \\end{{tabular}}
  \\setcounter{{choice}}{{1}}
}} % Makes multiple-choice options 
%---------------------------------

% The commands below are for setting up arithmetic 
% problems with the four basic operations. See examples 
% in the CONTENT section  

\\newcommand\\divi[2]{{
#1 \\: \\begin{{array}}{{|l}}
\\hline #2
\\end{{array}}
}}

\\newcommand\\mult[2]{{
$\\begin{{array}}{{rr}} 
 & #1 \\\\ 
 \\times & #2 \\\\ \\hline 
 \\end{{array}}$}}
 
\\newcommand\\addi[2]{{
  $\\begin{{array}}{{rr}} 
   &  #1 \\\\ 
    + & #2 \\\\ \\hline 
  \\end{{array}}$}}

\\newcommand\\subt[2]{{
  $\\begin{{array}}{{rr}}
    & #1 \\\\ 
    - & #2 \\\\ \\hline
  \\end{{array}}$}}
%-------------------------------------------------------------------%%

%-----------FORMATTING----------------------------------------------%%
\\pagestyle{{empty}} % Ensures that no page numbers are printed
\\parskip = 0.2 in % Puts a little space between paragraphs 
\\parindent = 0.0 in % Enforces no indentation for paragraphs
%-------------------------------------------------------------------%%

%-----------USAGE EXAMPLES------------------------------------------%%
% To try any of the examples below, uncomment them and paste 
% them below the \\begin{{document}} command in the CONTENT section. 

% To set up a division problem such as 93 divided by 3:
% \\divi{{3}}{{93}}

% To set up a muliplication problem such as 14 times 4:
% \\mult{{14}}{{4}}

% To put two problems on the same line: 
% \\pairofprobs{{\\divi{{3}}{{93}}}}{{\\mult{{14}}{{4}}}} 

% To include a 3cm vertical space between questions 
% \\vspace{{3cm}} 

%--------------------------------------------------------------------%%

%-----------CONTENT--------------------------------------------------%%
\\begin{{document}}

\\begin{{center}} 
  \\textsc{{Insert title here}} \\\\ 
  Teacher's name
\\end{{center}}

Date:\\underline{{\\hspace*{{4cm}}}} \\hfill 
Name:\\underline{{\\hspace*{{4cm}}}}

%\\fontsize{{14}}{{18pt}} \\selectfont % Increase Font Size

\\textit{{Directions}} 

{problems}

\\end{{document}} 
%-------------------------------------------------------------------%%

"""

def get_row_of_random_problems():
   
   (a,b,c,d,e,f) = random.choices(range(1, 101), k=6)
   
   return f'\\threeprobs{{\\divi{{{a}}}{{{b}}}}}{{\\mult{{{c}}}{{{d}}}}}{{\\addi{{{e}}}{{{f}}}}}'

def get_rows_of_random_problems(n):
    rows = ""
    for x in range(n):
        rows = rows +  '\\n\\vspace{{2cm}}\\n' + get_row_of_random_problems() 
    return rows

problems = get_rows_of_random_problems(5)  # May need more or fewer than 5 rows, try it out

worksheet = latex_template.format(problems=problems)

with open('worksheet.tex', 'w') as f:
    f.write(worksheet)
