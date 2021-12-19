for /l %%x in (1, 1, 100) do (
    echo %%x
    iozone -r 64 -a -g 16G -B >> %%x.txt
)