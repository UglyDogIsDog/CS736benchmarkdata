for /l %%x in (1, 1, 100) do (
    echo %%x
    iozone -r 4 -a -g 1024 -n 4 >> %%x.txt
)