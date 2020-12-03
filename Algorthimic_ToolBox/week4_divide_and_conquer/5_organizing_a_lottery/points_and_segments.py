# Uses python3
import sys

def fast_count_segments(starts, ends, points):
    cnt = []
    for entry_number in points:
        way_ward = 0
        for i,j in zip(starts,ends):
            if i<= entry_number <=j :
                way_ward = way_ward + 1
        cnt.append(way_ward)

    return cnt

def x_y(entry_number,starts,ends):

    way_ward = 0
    for i,j in zip(starts,ends):
        if i<=entry_number:
            if entry_number<=j:
                way_ward = way_ward + 1
    return way_ward


def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    cnt = [ x_y(x,starts,ends) for x in points]
    for x in cnt:
        print(x, end=' ')
