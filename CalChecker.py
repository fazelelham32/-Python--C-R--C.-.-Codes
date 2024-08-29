def calculation(target, num, *nums, operator='+'):
    result = num
    if operator=='+':
        for item in nums:
            result+=item
    elif operator=='-':
        for item in nums:
            result-=item
    else:
        print('choose between + and - operator')
    return result

final_result=calculation(1,2,3,4)
print(final_result)
