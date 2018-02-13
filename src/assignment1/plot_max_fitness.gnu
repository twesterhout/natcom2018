#!/usr/bin/gnuplot -p

set terminal pngcairo \
    enhanced color font "DejaVu Sans Mono, 10" size 800,600
set output "doc/source/FakeMonteCarlo.png"

set title "Fake Monte-Carlo"
set ylabel "Fitness"
set xlabel "Iteration"

plot for [i = 1:10] "data/assignment1/fake_monte_carlo_" . i . ".dat" \
    with linespoints pointtype 7 pointsize 0.3 notitle
# linecolor rgb "#303030" notitle

set output
set terminal x11



