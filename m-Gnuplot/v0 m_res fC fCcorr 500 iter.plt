set style data lines
set xrange [0:500]
set yrange [-0.05:1.01]
set ylabel "freq"
set xlabel "iteration"
set title "frequencies and av pay"
set key at 65,0.98
plot 'm_results_a.txt' using 1:2 with lines lc 5 lw 3 title "f C",\
'm_results_a.txt' using 1:3 with lines lc 7 lw 3 title "f C corr",\
'm_results_a.txt' using 1:4 with lines lc 4 lw 3 title "av pay",\
'm_results_a.txt' using 1:5 with lines lc 6 lw 3 title "c cr 0s",\
'm_results_a.txt' using 1:6 with lines lc 2 lw 3 title "c cr 1s",\
'm_results_a.txt' using 1:12 with lines lc 8  lw 3 title "f strat ch",\
'm_results_a.txt' using 1:13 with lines lc 1 lw 3 title "f str ch fin"
