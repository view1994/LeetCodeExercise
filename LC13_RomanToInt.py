# -*- coding: utf-8 -*-
#
means={
    'I':1,
    'V':5,
    'X':10,
    'L':50,
    'C':100,
    'D':500,
    'M':1000
}
def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    nums= []
    num = 0
    for i in s:
        nums.append(means[i])
    nums.append(0)
    for i in range(len(nums)-1):
        if nums[i] < nums[i+1]:
            num -= nums[i]
        else:
            num += nums[i]
    return num


def main():
    print(romanToInt('MCCXXXIV'))


if __name__ == '__main__':
    main()