set style data lines
set xrange [0:500]
set yrange [-0.05:1.01]
set xlabel "iteration"
set ylabel "freq"
set xlabel "iteration"
set title "strategies freq"
plot 'm_results_a.txt' using 1:5 with lines lc 7 lw 3 title "f all-C",\
 'm_results_a.txt' using 1:6 with lines lc 3 lw 3  title "f all-D",\
 'm_results_a.txt' using 1:7 with lines lc 2 lw 3 title "f k-D",\
'm_results_a.txt' using 1:8 with lines lt rgb "cyan" lw 3 title "f k-C",\
'm_results_a.txt' using 1:9 with lines lt rgb "magenta" lw 3 title "f k-DC"


