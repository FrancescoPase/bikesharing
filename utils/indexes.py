def days_index(df):
    """
    Find indexes of daily trips
    """
    d_i = {}
    for index, row in df.iterrows():
        day = int(row['starttime'].split()[0].split('-')[2])
        if d_i.get(day) is None:
            d_i[day] = index
    return d_i


def hour_rides(first, last, df):
    """
    Find indexes to extract temporal rides within days
    """
    d_h = {}
    for index, row in df.iloc[first:last].iterrows():
        hour = int(row['starttime'].split(':')[0][-2:])
        if d_h.get(hour) is None:
            d_h[hour] = [index]
        else:
            d_h[hour].append(index)
    return d_h


def transform_source(sources, iso):
    """
    Transfmorm Index depending on week graph
    """
    s_list = sources.copy()

    for j in range(len(s_list)):
        i = 0
        if s_list[j] in set(iso):
            print('Ocioooo')
            s_list[j] = -1

        for e in iso:
            if e < s_list[j]:
                i += 1
        s_list[j] -= i
    return s_list


