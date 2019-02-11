import subprocess
import os
paths = subprocess.check_output("git ls-files", shell=True).splitlines()
paths = ['kaleidoscope/' + path.decode() for path in paths]
paths = sorted(paths, key = lambda line: (line.count(os.sep), line))

tree = {}

for item in paths:
    p = tree
    for x in item.split('/'):
        p = p.setdefault(x, {})
        
def file_append(s, fn):
    with open(fn, "a") as f:
        f.write(s)
        
def write_tree(val, nesting = -5, fn='tree.txt'):
    if type(val) == dict:
        file_append('', fn)
        nesting += 5
        for k in val:
            file_append(nesting * ' '+ '|--- ', fn)
            file_append(k + '', fn)
            file_append('\n', fn)
            write_tree(val[k] ,nesting)
    else:
        file_append(val, fn)
        file_append('\n', fn)
        
write_tree(tree)