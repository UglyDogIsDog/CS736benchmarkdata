for x in {1..100..1}
  do
    echo $x
    ./iozone -r 64 -a -g 16G >> $x.txt
  done
