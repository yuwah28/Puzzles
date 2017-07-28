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

print ' '
print 'Evaluating Statistics of Bias Coin Tossing ...'
print ' '

m, n, p, t  = 30000, 1, .6, 10
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

    if (g[k] > c and h > nh):
        s = s + 1

#compute expectation value and probability(prob)
g_exp   = np.mean(g)
prob_a  = (1.*sum(i > a for i in g)) / (1.*len(g))
prob_b  = (1.*sum(i > b for i in g)) / (1.*len(g))
prob_ab = prob_a / prob_b   
prob_c_and_nh = 1.*s / (1.*m)

print 'Expected number of group', 'after ', t, 'tosses = ', format(g_exp,'.9f')
print 'P(>', a, 'group) ', 'after ', t, 'tosses  = ', format(prob_a, '.9f') 
print 'P(>', a, 'group', '| >', b, 'groups) = ', format(prob_ab,'.9f')
print 'P(>', c, 'group and >', nh, 'head) = ', format(prob_c_and_nh, '.9f')
print ' '
print 'Done!'
print ' '
