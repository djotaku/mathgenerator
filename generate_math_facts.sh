#!/bin/bash

echo "Generating random facts"
python math_facts_add_sub.py

echo "latex stuff"
latex worksheet.tex
dvipdfm worksheet.dvi

echo "print"
lp -d HL3140CW worksheet.pdf
