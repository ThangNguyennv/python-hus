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
    lname = '' # tên đệm
    fname = '' # tên chính
    parts = s.strip().split()
    fname = parts[-1]
    lname = " ".join(parts[1:-1]) if len(parts) > 2 else ""
    return lname, fname

def name_key(names):
    parts = names.strip().split()
    ten = parts[-1]
    dem = " ".join(parts[1:-1]) if len(parts) > 2 else ""
    return (
        locale.strxfrm(ten),
        locale.strxfrm(dem)
    )

def sortNamesList(names):
    all_names = []
    for group in names:
        namesSorted = sorted(group, key=name_key)
        all_names.append(namesSorted)
    return all_names

