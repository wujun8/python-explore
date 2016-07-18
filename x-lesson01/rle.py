def encode(input_string):
    count = 1
    prev = ''
    lst = []
    character = ''
    for character in input_string:
        if character != prev:
            if prev:
                entry = (prev,count)
                lst.append(entry)
            count = 1
            prev = character
        else:
            count += 1
    else:
        entry = (character,count)
        lst.append(entry)
    return lst


def decode(lst):
    q = ""
    for character, count in lst:
        q += character * count
    return q


source_str = 'WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB'
encode_list = encode(source_str)
encode_str = ''
for w, count in encode_list:
    if count > 1:
        encode_str += str(count) + w
    else:
        encode_str += w
print encode_str
decode_str = decode(encode_list)
print decode_str