set style data lines
set xrange [0:500]
set yrange [-0.05:1.01]
set xlabel "iteration"
set ylabel "freq
set title "freq of kC strategies"
plot 'results_b.txt' using 1:11 with lines lt rgb "gold" lw 3 title "f 0C",\
'results_b.txt' using 1:12 with lines lt rgb "pink" lw 3 title "f 1C",\
'results_b.txt' using 1:13 with lines lt rgb "web-green" lw 3 title "f 2C",\
'results_b.txt' using 1:14 with lines lt rgb "cyan" lw 3 title "f 3C",\
'results_b.txt' using 1:15 with lines lt rgb "skyblue" lw 3 title "f 4C",\
'results_b.txt' using 1:16 with lines lt rgb "dark-turquoise" lw 3 title "f 5C",\
'results_b.txt' using 1:17 with lines lt rgb "dark-violet" lw 3 title "f 6C",\
'results_b.txt' using 1:18 with lines lt rgb "slateblue1" lw 3 title "f 7C",\
'results_b.txt' using 1:19 with lines lt rgb "blue" lw 3 title "f 8C"