# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 11:47:34 2015

@author: Alejandro Alcalde (elbauldelprogramador.com)
"""

def berlekampMassey(s):
    """
    The Berlekamp-Massey algorithm (Algorithm 6.30) is an efficient 
    algorithm for determin-ing the linear complexity of a finite binary 
    sequence s n of length n (see Definition 6.18).
    
    The algorithm takes n iterations, with the N th iteration computing 
    the linear complexity of the subsequence s N consisting of the first N 
    terms of s n
    """
    C = [1]
    L = 0
    m = -1
    B = [1]
    N = 0
    T = []
    l = 1
    
    while(N < len(s)):
        
        d = 0
                
        for i in range(0,L+1):
            d += C[i]*s[N-i]
        d = d%2
        
        if d == 1:
            T=C
            D = [0]*(N-m)+B
            if(len(D) > len(C)):
                C = C+([0]*(len(D)-len(C)))
            for i in range(0,len(D)): 
                C[i] = (C[i]+D[i])%2
            if(L<=N/2):
                L=N+1-L
                m=N
                B=T
                l=1
            else:
                l+=1
        else:
             l+=1

        N = N+1
    
    return L,C
    
print berlekampMassey([1,0,0,1,0])