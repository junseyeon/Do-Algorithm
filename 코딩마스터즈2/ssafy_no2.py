
def main():
    T = int(input())
    for test_case in range(1, T + 1):
        N, A, B = map(int, input().split())  # min, max
        arr = list(map(int, input().split()))
        # arr = list(input().split())
        max_n = max(arr)
        min_n = min(arr)
        left_arr = dict()
        for i in arr:
            if i != max_n and i != min_n:
                if i in left_arr:
                    left_arr[i] += 1
                else:
                    left_arr[i] = 1
        # print(left_arr)
        arr_len = len(left_arr)
        sum_arr = [0] * arr_len
        values = list(left_arr.values())
        for i in range(arr_len):
            for j in values[i:]:
                if sum_arr[i] + j <= B:
                    sum_arr[i] += j
                if sum_arr[i] > B:
                    break
        print("#%d" % test_case, max(sum_arr))


if __name__ == "__main__":
    main()

