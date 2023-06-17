set style data lines
set xrange [0:500]
set yrange [-0.05:1.01]
set xlabel "iteration"
set ylabel "freq
set title "freq of kDC strategies"
plot 'results_b.txt' using 1:20 with lines lt 4 lw 3 title "f 0DC",\
'results_b.txt' using 1:21 with lines lt 3 lw 3 title "f 1DC",\
'results_b.txt' using 1:22 with lines lt rgb "yellow" lw 3 title "f 2DC",\
'results_b.txt' using 1:23 with lines lt rgb "red" lw 3 title "f 3DC",\
'results_b.txt' using 1:24 with lines lt rgb "green" lw 3 title "f 4DC",\
'results_b.txt' using 1:25 with lines lt rgb "violet" lw 3 title "f 5DC",\
'results_b.txt' using 1:26 with lines lt rgb "cyan" lw 3 title "f 6DC",\
'results_b.txt' using 1:27 with lines lt rgb "pink" lw 3 title "f 7DC",\
'results_b.txt' using 1:28 with lines lt rgb "dark-orange" lw 3 title "f 8DC"