
mylist = [2, 33, 18, 1, 7, 55, 98]
reversed_list = (mylist[2::])[::-1]  # reversed original list ignoring first 2 elements in original.
if reversed_list[2] == 7:
    print("boom")