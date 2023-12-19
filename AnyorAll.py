"""
Title     : Any or All
Subdomain : Built-Ins
Domain    : Python
Created   : 19/12/2023
Updated   : 19/12/2023
Problem   : https://www.hackerrank.com/challenges/any-or-all/problem
"""

n = input()
ar = input().split()
print(all(int(i) > 0 for i in ar) and any(i == i[::-1] for i in ar))
