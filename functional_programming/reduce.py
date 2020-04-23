def reduce(arr, fun, answer):
    for i in arr:
        answer = fun(answer, i)
    return answer


arr = [1, 2, 3, 4, 5]
arr2 = ["Hello...", "it's", "me...", "I", "was", "wondering"]

print(reduce(arr, lambda x, y: x + y, 0))  # 15
print(reduce(arr2, lambda x, y: x + y + " ", answer=""))
