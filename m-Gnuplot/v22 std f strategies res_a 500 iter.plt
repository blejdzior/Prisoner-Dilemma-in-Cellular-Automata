set style data lines
set xrange [0:500]
set yrange [-0.05:1.01]
set xlabel "iteration"
set ylabel "freq"
set title "avg and std strategies"
plot 'std_results_a.txt' using 1:12:13 with yerrorbars lc 7 title "stdev: all-C",\
'std_results_a.txt' using 1:12 with lines lc 7 lw 3 title "avg num all-C",\
'std_results_a.txt' using 1:14:15 with yerrorbars lc 6 title "stdev: all-D",\
'std_results_a.txt' using 1:14 with lines lc 6 lw 3 title "avg num of all-D",\
'std_results_a.txt' using 1:16:17 with yerrorbars lc 2 title "stdev: k-D",\
'std_results_a.txt' using 1:16 with lines lc 2 lw 3 title "avg num of k-D",\
'std_results_a.txt' using 1:18:19 with yerrorbars lc 3 title "stdev: k-C",\
'std_results_a.txt' using 1:18 with lines lc 3 lw 3 title "avg num of k-C",\
'std_results_a.txt' using 1:20:21 with yerrorbars lc 9 title "stdev: k-DC",\
'std_results_a.txt' using 1:20 with lines lc 9 lw 3 title "avg num of k-DC"




