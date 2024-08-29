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

        checher(target, result)
    return result
def checker(target, result):
    if target<result:
        print('true target is greater that your selected target')
    elif target>result:
        print('true target is lower that your selected target')

    else:
        print('your target is equal to our result')

final_result=calculation(1,2,3,4)
print('the final result is %d' % final_result)
