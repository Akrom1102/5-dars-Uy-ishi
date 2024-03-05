def birxilsoz(strs):

    prefix = strs[0]

    for string in strs[1:]:
        while string.find(prefix) != 0:
            prefix = prefix[:-1]
            if not prefix:
                return "Yo'q. Oxshashlik yo'q"

    return prefix


print(birxilsoz(["flower", "flow", "flight"]))
print(birxilsoz(["cat", "dor", "ayiq"]))
print(birxilsoz(["olma", "olim", "olmos"]))
print(birxilsoz(["Akrom", "Akmal", "Akbar"]))