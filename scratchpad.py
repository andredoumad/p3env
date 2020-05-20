import os
path = os.getcwd()
print(path)
with open('scratchpad_in.txt', mode="r") as fin:
    with open('scratchpad_out.txt', mode="w+") as fout:
        lines = fin.readlines()
        for line in reversed(lines):
            fout.write(line.strip() + '\n')
            print(line.strip())