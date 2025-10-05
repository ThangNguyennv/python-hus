# -*- coding: utf-8 -*-
import locale

locale.setlocale(locale.LC_ALL, 'vi_VN')

def inputList():
    all_groups = []
    current_group = []

    while True:
        try:
            line = input().strip()
        except EOFError:
            break

        if line == "":
            if current_group:
                all_groups.append(current_group)
                current_group = []
        else:
            current_group.append(line)

    if current_group:
        all_groups.append(current_group)

    return all_groups

def getName(s):
    tokens = s.strip().split(' ')
    fname = ''
    sname = ''
    if len(tokens) == 1:
        fname = tokens[0]
    else:  # ' '.join(tokens[:-1])
        fname = tokens[len(tokens)-1] # fname = tokens[-1]
        for i in range(0,len(tokens)-1): # " ".join(tokens[:-1])
            sname = sname+ tokens[i]+' '
        sname = sname.strip()

    return sname, fname

def compare(name):
    sname, fname = getName(name)
    return locale.strxfrm(fname), locale.strxfrm(sname)

def sortNamesList(names):
    all_names = []
    for group in names:
        namesSorted = sorted(group, key=compare)
        all_names.append(namesSorted)
    return all_names

