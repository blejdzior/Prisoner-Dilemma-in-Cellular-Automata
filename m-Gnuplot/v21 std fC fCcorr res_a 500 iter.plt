set style data lines
set xrange [0:500]
set yrange [-0.05:1.01]
set xlabel "iteration"
set ylabel "freq"
set title "avg and std fC and fCcorr"
plot 'std_results_a.txt' using 1:2 with lines lc 5 lw 3 title "av fC",\
'std_results_a.txt' using 1:2:3 with yerrorbars lc 5 title "std",\
'std_results_a.txt' using 1:4 with lines lc 7 lw 3 title "av fC corr",\
'std_results_a.txt' using 1:4:5 with yerrorbars lc 7 title "std",\
'std_results_a.txt' using 1:6 with lines lc 4 lw 3 title "av pay",\
'std_results_a.txt' using 1:6:7 with yerrorbars lc 4 title "std",\
'std_results_a.txt' using 1:8 with lines lc 6 lw 3 title "av fcr0s",\
'std_results_a.txt' using 1:8:9 with yerrorbars lc 6 title "std",\
'std_results_a.txt' using 1:10 with lines lc 2 lw 3 title "av fcr1s",\
'std_results_a.txt' using 1:10:11 with yerrorbars lc 2 title "std",\
'std_results_a.txt' using 1:22 with lines lc 8 lw 3 title "av f strat ch",\
'std_results_a.txt' using 1:22:23 with yerrorbars lc 8 title "std",\
'std_results_a.txt' using 1:24 with lines lc 1 lw 3 title "av f strat ch fin",\
'std_results_a.txt' using 1:24:25 with yerrorbars lc 1 title "std"