n_list = []
while True:
    try:
        n_list.append(int(input()))
    except:
        print(max(n_list))
        print(n_list.index(max(n_list)) + 1)
        break