# -*- coding:utf-8 -*-
import sys
import io
import math

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
value = int(input("請輸入本金(萬): "))
year = int(input("請輸入期數(年): "))
r = int(input("請輸入利率(%): "))

real_value = value * 10000
real_year = year * 12
real_r = r / 1200

principal = math.ceil(real_value/real_year)

play = 0
accumulated_amount = 0
total_interest = 0

print("期數    本金    利息    本利和")

for index in range(real_year-1):
    interest = (real_value - principal*play)*real_r
    play += 1
    accumulated_amount = principal + interest + accumulated_amount
    total_interest += round(interest)
    print(play, "  ", principal, "  ", round(
        interest), "  ", round(accumulated_amount))

new_principal = real_value - principal*play
interest = (real_value - principal*play)*real_r
play += 1
accumulated_amount = new_principal + interest + accumulated_amount
total_interest += round(interest)
print(play, "  ", new_principal, "  ", round(
    interest), "  ", round(accumulated_amount))

print("平均每月攤還本金: ", principal)
print("全部利息: ", round(total_interest))
