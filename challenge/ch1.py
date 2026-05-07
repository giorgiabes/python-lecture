test_lst = [1, 2, 3, 500, 41, 42, 43, 44]


def longest_consecutive(lst):
    if len(lst) == 0:
        return 0

    sorted_lst = sorted(lst)  # [1, 1, 2, 4, 100, 200]

    tmp_arr = []
    arr = []

    for i in range(len(sorted_lst) - 1):
        if sorted_lst[i + 1] - sorted_lst[i] == 1:
            tmp_arr.append(sorted_lst[i])

    result = len(arr) + 1
    return result


# print(len(arr))  # 2

###############################################################


def test_longest_consecutive(longest_consecutive):
    """
    longest_consecutive — შენი ფუნქცია, რომელიც იღებს სიას
    და აბრუნებს ყველაზე გრძელი თანმიმდევრული მიმდევრობის სიგრძეს.
    """

    test_cases = [
        # (შეტანა, მოსალოდნელი შედეგი, აღწერა)
        ([100, 4, 200, 1, 3, 2], 4, "ძირითადი მაგალითი"),
        ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9, "დუბლიკატით"),
        ([], 0, "ცარიელი სია"),
        ([1], 1, "ერთი ელემენტი"),
        ([5, 5, 5, 5], 1, "ყველა დუბლიკატი"),
        ([1, 2, 3, 4, 5], 5, "უკვე სორტირებული"),
        ([5, 4, 3, 2, 1], 5, "შებრუნებული რიგით"),
        ([10, 20, 30, 40], 1, "არცერთი თანმიმდევრული"),
        ([-3, -2, -1, 0, 1], 5, "უარყოფითი რიცხვებით"),
        ([1, 2, 0, 1], 3, "დუბლიკატი შუაში"),
        ([9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6], 7, "რთული შემთხვევა: -1..., 0...6"),
        ([1, 2, 3, 100, 200, 4, 5, 6, 7], 7, "ორი ჯგუფი — გრძელი იმარჯვებს"),
        ([1000000, 999999, 999998], 3, "დიდი რიცხვები"),
        ([0], 1, "მხოლოდ ნული"),
        ([-1, -2, -3, -4], 4, "მხოლოდ უარყოფითი"),
    ]

    passed = 0
    failed = 0

    for i, (input_data, expected, description) in enumerate(test_cases, 1):
        result = longest_consecutive(input_data)
        status = "✅" if result == expected else "❌"

        if result == expected:
            passed += 1
            print(f"{status} ტესტი {i}: {description}")
        else:
            failed += 1
            print(f"{status} ტესტი {i}: {description}")
            print(f"   შეტანა:    {input_data}")
            print(f"   მოსალოდნელი: {expected}")
            print(f"   მიღებული:   {result}")

    print(f"\n{'=' * 50}")
    print(f"შედეგი: {passed}/{len(test_cases)} გავლილი")
    if failed == 0:
        print("🎉 ყველა ტესტი წარმატებით გაიარა!")
    else:
        print(f"⚠️  {failed} ტესტი ვერ გაიარა")


# გამოყენება:
# 1. დაწერე შენი ფუნქცია
# def longest_consecutive(nums):
#     # შენი კოდი აქ
#     pass
#
# 2. გაუშვი ტესტი
test_longest_consecutive(longest_consecutive)
