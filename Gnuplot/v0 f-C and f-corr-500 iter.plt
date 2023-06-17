set style data lines
set xrange [0:500]
set yrange [-0.05:1.01]
set xlabel "iteration"
set ylabel "freq"
set key at 65,0.98
plot 'results_a.txt' using 1:2 with lines lc 5 lw 3 title "f C",\
'results_a.txt' using 1:3 with lines lc 7 lw 3 title "f C corr",\
'results_a.txt' using 1:4 with lines lc 4 lw 3 title "av pay",\
'results_a.txt' using 1:5 with lines lc 6 lw 3 title "c cr 0s",\
'results_a.txt' using 1:6 with lines lc 2 lw 3 title "c cr 1s",\
'results_a.txt' using 1:12 with lines lc 8 lw 3 title "f strat ch",\
'results_a.txt' using 1:13 with lines lc 1 lw 3 title "f str ch fin"

