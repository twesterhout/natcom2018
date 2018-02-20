#!/usr/bin/gnuplot -p

set terminal pngcairo \
    enhanced color font "DejaVu Sans Mono, 10" size 800,600
set output "doc/source/GP_Size.png"

set ylabel "Size"
set xlabel "Iteration"

plot[:50] "data/assignment1/genetic_output.dat" \
    u 1:4 with linespoints pointtype 7 pointsize 1 \
    linecolor rgb "#303030" notitle

set output "doc/source/GP_Fitness.png"

set ylabel "Fitness"

plot[:50] "data/assignment1/genetic_output.dat" \
    u 1:5 with linespoints pointtype 7 pointsize 1 \
    linecolor rgb "#303030" notitle

set output "doc/source/GP_Function.png"

unset ylabel

plot[][:5] "data/assignment1/genetic_data.dat" \
    u 1:2 with points pt 7 pointsize 1 \
    linecolor rgb "#303030" title "Raw data", \
    x + x**2 + x**3 + x**4 linecolor rgb "#303030" title "Fit"

set output
set terminal x11
