import os

def searchInFiles(x, path):
    a = os.listdir(path)
    result = []
    for f in a:
        if os.path.isfile(f):
            for line in open(f, 'r', encoding = 'utf-8'):
                if x in line:
                    result.append(('docs/' + f, line))
                    break
    result.sort(key=lambda s: s[0])
    return result