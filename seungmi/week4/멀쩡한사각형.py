from math import gcd

def solution(w,h):
    w_h_gcd=gcd(w,h)
    return w*h-((w/w_h_gcd+h/w_h_gcd-1)*w_h_gcd)