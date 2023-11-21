
def main():
    T = int(input())
    for test_case in range(1, T + 1):
        N = int(input())
        arr = list(map(int, input().split()))

        sort_arr= sorted(list(set(arr)), reverse=True)
        top_arr = [] # arr의 순위 기록
        for i in arr:
            top_arr.append(sort_arr.index(i)+1)

        price=0
        while arr:
            max_n = arr[top_arr.index(1)]
            if 2 in top_arr:
                next_max = arr[top_arr.index(2)]  # 다음 큰 가격
                arr.remove(next_max)

            price += max_n
            arr.remove(max_n)

            sort_arr = sorted(list(set(arr)), reverse=True)
            top_arr = []  # arr의 순위 기록
            for i in arr:
                top_arr.append(sort_arr.index(i) + 1)

        #print(price)
        print("#%d" % test_case, price)


if __name__ == "__main__":
    main()