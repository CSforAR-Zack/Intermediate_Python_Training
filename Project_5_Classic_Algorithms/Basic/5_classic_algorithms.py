import searches_sorts as ss


def main():
    values = [0, 2, 4, 7, 9, 23, 24, 36, 60, 62]
    target = 36

    print(ss.linear_search(values, target))
    print(ss.binary_search(values, target))

    b_values = [7, 23, 3, 24, 62, 9, 36, 60, 4, 0]
    ss.bubble_sort(b_values)
    print(b_values)
    
    s_values = [7, 23, 3, 24, 62, 9, 36, 60, 4, 0]
    ss.selection_sort(s_values)
    print(s_values)

    i_values = [7, 23, 3, 24, 62, 9, 36, 60, 4, 0]
    ss.insertion_sort(i_values)
    print(i_values)

    m_values = [7, 23, 3, 24, 62, 9, 36, 60, 4, 0]
    sorted_values = ss.merge_sort(m_values)
    print(sorted_values)


if __name__ == '__main__':
    main()