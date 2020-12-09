import markdown2
import glob
import os.path

def findall(p, s):
    '''Yields all the positions of
    the pattern p in the string s.'''
    i = s.find(p)
    while i != -1:
        yield i
        i = s.find(p, i+1)

files_to_convert = list(glob.glob(os.path.join('pages', '**', '*.md')))

print(len(files_to_convert), 'files to convert')

for i, f in enumerate(files_to_convert):
    print(i, f)
    # read
    with open(f, 'r') as ff:
        data = ff.read()
    # convert
    res = markdown2.markdown(data, extras=["fenced-code-blocks"])

    # switch images paths to global
    data_dir = os.path.dirname(f)
    res = res.replace('img src="', 'img src="' + data_dir.replace('\\','/') + '/')

    # save
    with open(os.path.splitext(f)[0] + '.html', 'w') as ff:
        ff.write(res)
    