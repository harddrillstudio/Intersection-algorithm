# time_ranges is list of lists
timez = [[10, 40], [38, 78], [46, 96], [60, 122]]


def create_pairs_intersection(time_ranges):
    tuples_list = []  # list of start and end tuples

    for t_range in time_ranges:
        start = (t_range[0], -1)
        mid = ((t_range[0] + t_range[1]) / 2), 0
        end = (t_range[1], +1)

        #         print(start)
        #         print(end)
        #         print()

        tuples_list.append(start)
        tuples_list.append(mid)
        tuples_list.append(end)

    return tuples_list


def intersection(time_ranges):
    M = len(time_ranges)
    lower, upper = 0, 0
    tuples_list = create_pairs_intersection(time_ranges)

    print("Number of intervals:", M)
    tuples_list = sorted(tuples_list, key=lambda x: (x[0], x[1]))
    print(tuples_list)

    # 0. [initialize best f]
    for f in range(int(M / 2)):
        tuples_list = sorted(tuples_list, key=lambda x: (x[0], x[1]))

        midcount, endcount = 0, 0

        # 2. [find lower endpoint]
        for pair in tuples_list:
            endcount -= type_p(pair)

            if endcount >= (M - f):
                print("low has been found", lower)
                break

            lower = offset(pair)

            if type_p(pair) == 0:
                midcount += 1

        endcount = 0

        for pair in tuples_list[::-1]:
            endcount += type_p(pair)

            if endcount >= M - f:
                print("high has been found", upper)
                break

            upper = offset(pair)

            if type_p(pair) == 0:
                midcount += 1

        if midcount <= f:
            break

    print("Correct quantity:", M - f)
    print("False quantity:", f)
    if lower > upper:
        return ("Error")
    return [lower, upper]

print(intersection(timez))
