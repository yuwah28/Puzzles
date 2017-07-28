import numpy as np

#Author: Pak Kau Lim

#Definition
#m : number of trials/ensembles
#n : number of coin used
#p : probability of head
#t : number of toss
#g : number of group
#h : head count in a trial
#s : sample number
#a,b,c : greater than give a,b values statement
#nh  : greather than n heads statement

m, n, p, t = 20000, 1, .4, 10
a, b, c, nh = 6, 5, 5, 5 

g = range(m)
s = 0
for k in range(m): 
    coin = np.random.binomial(n, p, t)
    h    = 1.*sum( i < 1 for i in coin)

    j = 1
    for i in range(0, t-1):
        if coin[i] != coin[i+1]:
            j = j + 1
        else:
            j = j           
    g[k] = j

    if (g[k] > a and h > c):
        s = s + 1

    print 'coin toss : ', coin, ' group num = ', g[k], 'h num = ', h

print 's', s    
#compute expectation value and probability(prob)
g_exp   = np.mean(g)
prob_a  = (1.*sum(i > a for i in g)) / (1.*len(g))
prob_b  = (1.*sum(i > b for i in g)) / (1.*len(g))
prob_ab = prob_a / prob_b   
prob_a_and_h = 1.*s / (1.*m)
 
print 'Expected number of group', 'after ', t, 'toss = ', format(g_exp,'.9f')
print 'P(>', a, 'group) ', 'after ', t, 'toss  = ', format(prob_a, '.9f') 
print 'P(>', a, 'group', '| >', b, 'groups) = ', format(prob_ab,'.9f')
print 'P(>', a, 'group and >', c, 'head) = ', format(prob_a_and_h, '.9f')
