# -*- coding: utf-8 -*-
"""
Created on Fri May 20 16:45:11 2022

@author: asus
"""


class BMI():
    def count(height, weight):
        BMI = weight / pow(height, 2)

        print('您的BMI值為：%.2f' %BMI)

        if BMI < 18.5:
            print('屬\"體重過輕\"')
        elif BMI <24 or BMI == 18.5:
            print('屬\"體重正常\"')
        elif BMI <27 or BMI == 24:
            print('屬\"過重\"')
        elif BMI <30 or BMI == 27:
            print('屬\"輕度肥胖\"')
        elif BMI <35 or BMI == 30:
            print('屬\"中度肥胖\"')
        else:
            print('屬\"重度肥胖\"')

    def keep():
        ans = input('是否要繼續輸入(y/n): ')
        return ans
    
    try:
        while True:
            height= int(input('請輸入身高(公分): ')) / 100
            weight = int(input('請輸入體重(公斤): '))
            count(height, weight)
            g = keep()
            if g == 'n' or g == 'N':
                break
    except:
        print('請輸入正確數值')

BMI()