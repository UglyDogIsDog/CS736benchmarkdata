for x in {1..100..1}
  do
    echo $x
    ./iozone -r 4 -a -g 1024 -n 1 -B >> $x.txt
  done
