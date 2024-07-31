def solution(data, ext, val_ext, sort_by):
    m = ['code', 'date', 'maximum', 'remain']
    return sorted([i for i in data if i[m.index(ext)] < val_ext], key = lambda x : x[m.index(sort_by)])