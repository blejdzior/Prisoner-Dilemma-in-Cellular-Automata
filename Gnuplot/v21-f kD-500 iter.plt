set style data lines
set xrange [0:500]
set yrange [-0.05:1.01]
set xlabel "iteration"
set ylabel "freq
set title "freq of kD strategies"
plot 'results_b.txt' using 1:2 with lines lt rgb "gold" lw 3 title "f 0D",\
'results_b.txt' using 1:3 with lines lt rgb "coral" lw 3 title "f 1D",\
'results_b.txt' using 1:4 with lines lt rgb "dark-yellow" lw 3 title "f 2D",\
'results_b.txt' using 1:5 with lines lt rgb "tan1" lw 3 title "f 3D",\
'results_b.txt' using 1:6 with lines lt rgb "green" lw 3 title "f 4D",\
'results_b.txt' using 1:7 with lines lt rgb "cyan" lw 3 title "f 5D",\
'results_b.txt' using 1:8 with lines lt rgb "violet" lw 3 title "f 6D",\
'results_b.txt' using 1:9 with lines lt rgb "web-green" lw 3 title "f 7D",\
'results_b.txt' using 1:10 with lines lt rgb "dark-spring-green" lw 3 title "f 8D"