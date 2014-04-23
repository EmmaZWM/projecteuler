def get_word_value(word):
    return sum(ord(w) - ord("A") + 1 for w in word)

def gen_triangle_number_below(x):
    start = 1
    ret = start * (start + 1)/2
    while ret < x:
        yield ret
        start += 1
        ret = start * (start + 1)/2

def main():
    count = 0
    with open('words.txt') as f:
        line = f.read().strip().split(',')
        words = [i[1:-1] for i in line]
        len_max = max(len(w) for w in words)
        tri_num = gen_triangle_number_below(len_max * 26)
        tri_dict = {}
        for num in tri_num:
            tri_dict[num] = 1
        for word in words:
            if get_word_value(word) in tri_dict:
                count += 1
    return count

if __name__ == '__main__':
    print main()
