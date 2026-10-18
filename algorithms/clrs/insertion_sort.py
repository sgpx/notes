def insertion_sort(a):
        for i in range(1,len(a)):
                print(a)
                print(f"\n\ni : {i}, a[i] : {a[i]}")
                key = a[i]
                j = i - 1
                print(f"j : {j}, a[j] : {a[j]}")
                while j >= 0 and a[j] > key:
                        print(f"inside loop j : {j}, a[j] : {a[j]}")
                        print(f"setting a[j+1] {j+1} as a[j] {j}")
                        print(a)
                        a[j+1] = a[j]
                        print(a)
                        j -= 1
                print(f"setting j+1 : {j+1}, a[j+1] : {a[j+1]}, key : {key}")
                a[j+1] = key
                print(a)
        return a

a = [4,5,1,2]
insertion_sort(a)
