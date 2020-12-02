def compression(user_string):
    previous_char = ""
    char_count = 0
    loop_counter = 0
    compressed_string = []
    for char in user_string:
        if loop_counter == 0:
            previous_char = char
            char_count += 1
            loop_counter += 1
            continue
        if char == previous_char:
            char_count += 1
        else:
            if char_count > 1:
                compressed_string.append("%d%c" % (char_count, previous_char))
            else:
                compressed_string.append("%c" % previous_char)
            char_count = 1
        previous_char = char
        loop_counter += 1

    if char_count > 1:
        compressed_string.append("%d%c" % (char_count, previous_char))
    else:
        compressed_string.append("%c" % previous_char)

    str1 = ''.join(compressed_string)
    print(str1)


if __name__ == '__main__':
    compression("22")
