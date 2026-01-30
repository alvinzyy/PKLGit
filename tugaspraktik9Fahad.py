"""
Contoh penggunaan list di Python — ringkas dan runnable.
Menampilkan: pembuatan, indexing, slicing, metode umum,
iterasi, list comprehension, nested list, dan tugas umum.
"""

def creation_examples():
    a = [1, 2, 3]
    b = list(range(5))
    c = ['x'] * 3
    print('Creation: a=', a, 'b=', b, 'c=', c)


def methods_examples():
    lst = [10, 20, 30]
    lst.append(40)
    lst.insert(1, 15)
    lst.extend([50, 60])
    removed = lst.pop()  # removes last
    first = lst.pop(0)   # removes first
    print('Methods: after append/insert/extend ->', lst, 'popped=', removed, 'first=', first)
    # remove by value (guarded)
    if 20 in lst:
        lst.remove(20)
    print('Methods: after remove(20) ->', lst)


def slicing_indexing_examples():
    l = list(range(10))
    print('Indexing: l[0]=', l[0], 'l[-1]=', l[-1])
    print('Slicing: l[2:6]=', l[2:6], 'l[:5]=', l[:5], 'l[::2]=', l[::2])


def iteration_examples():
    items = ['apel', 'pisang', 'jeruk']
    for i, v in enumerate(items, 1):
        print(f'Iterasi {i}:', v)


def comprehension_nested_examples():
    squares = [x * x for x in range(6)]
    evens = [x for x in range(10) if x % 2 == 0]
    matrix = [[i, j] for i in range(3) for j in range(2)]
    print('Comprehension: squares=', squares, 'evens=', evens)
    print('Nested list (matrix)=', matrix)


def common_tasks_examples():
    nums = [3, 1, 2, 3, 2, 5]
    # deduplicate while preserving order
    dedup = list(dict.fromkeys(nums))
    # flatten nested list
    nested = [[1, 2], [3, 4], [5]]
    flat = [y for x in nested for y in x]
    print('Common: nums=', nums, 'dedup=', dedup, 'flat=', flat)
    print('Stats: sum=', sum(nums), 'max=', max(nums), 'min=', min(nums))


def main():
    print('--- Examples: List in Python ---')
    creation_examples()
    methods_examples()
    slicing_indexing_examples()
    iteration_examples()
    comprehension_nested_examples()
    common_tasks_examples()


if __name__ == '__main__':
    main()
