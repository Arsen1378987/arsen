def get_in_sec(day):
    hours = day * 24
    minutes = hours * 60
    seconds = minutes * 60
    return seconds

d = 1
sec = get_in_sec(d)
print(sec)
# s = d * 24 * 60 * 60
# print_in_sec(s)

