def flatten(data):
    if not data:
        return []
    for i in data:
        if type(i) == list:
            for j in i:
                first_list = first_list.append(j)
                second_list = second_list.append(flatten(j[1:]))
                first_list.extend(second_list)
                return first_list
        if type(i) != list:
            first = []
            first.append[i]
            second = []
            second.append(flatten(i[1:]))
            first.extend(second)
            return first


def main():
    daten = [1, [2, 3], [4, [5, [6, 7]]], [[[8], 9], [10]]]
    print(flatten(daten))

if __name__ == '__main__':
    main()