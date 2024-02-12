"""
Assignment #3 Solution
ENGR 104, Fundamental Of Engineering Computing
Welz, Matt
1.29.2024
"""
# Problem 7.1 (2 Points)
print('----- Problem 7.1 (2 Points) -----')
a1 = 4 + 5
print(a1)
a2 = 12 - 3
print(a2)
a3 = 3 * 3
print(a3)
a4 = 81 / 9
print(int(a4))

# Problem 7.2 (2 Points)
print('\n----- Problem 7.2 (2 Points) -----')
name = 'matt'
print(f"'Hello {name.title()} would you like to learn some Python today'")

# Problem 7.3 (2 Points)
print('\n----- Problem 7.3 (2 Points) -----')
fav_num = 39
print(f"My favorite number is {fav_num}!")

# Problem 7.4 (2 Points)
print('\n----- Problem 7.4 (2 Points)-----')
h_0 = 1.6   #initial height (m)
v_0 = 15.2  #initial velocity (m/s)
t = 1.5     # time of flight (s)
g = 9.81    # gravitational acceleration (m/s^2)
h =round(h_0 + v_0*t - 0.5*g*t**2,2)
v =round( v_0 - g*t,3)
print(f"The height and velocity of the ball after {t} seconds is {h} (m) and {v} (m/s), respectively")

# ============================================================================
# Problem 8.1 (3 Points)
import math as m
print('\n----- Problem 8.1 (3 Points)-----')
a = (2+m.exp(2.8))/(m.sqrt(13)-2)
a = round(a,3)
print(f"a={a}")
b = (1-(1+m.log(2))**(-3.5))/(1+m.sqrt(5))
b = round(b,3)
print(f"b={b}")
c = m.sin((2-m.sqrt(2))/(2+m.sqrt(2)))
c = round(c,3)
print(f"c={c}")

# Problem 8.2 (2 Points)
print('\n----- Problem 8.2 (2 Points) -----')
x = 6.7
y =round(0.01*x**5 - 1.4*x**3 + 80*x +16.7,2)
print(f"y={y}")
z = round(m.sqrt(x**3 + m.exp(x) - 51/x),2)
print(f"z={z}")

# Problem 8.3 (2 Points)
print('\n----- Problem 8.3 (2 Points) -----')
T = 3.2
t1 = round(56*T - g*(T**2)/2,2)
print(f"t1={t1}")
t2 = round(14*m.exp(-0.1*T)*m.sin(2*m.pi*T),2)
print(f"t2={t2}")

# ============================================================================
# Problem 9.1 (1 Points)
print('----- Problem 9.1 (1 Points) -----')
friends = ['andy','autumn','kirsten','brett','amber']
print(friends[0])
print(friends[1])
print(friends[2])
print(friends[3])
print(friends[4])

# Problem 9.2 (1 Points)
print('\n----- Problem 9.2 (1 Points) -----')
print(list(range(-3,7,1)))

# Problem 9.3 (1 Points)
print('\n----- Problem 9.3 (1 Points) -----')
print(list(range(25,-10,-5)))

# Problem 9.4 (1 Points)
print('\n----- Problem 9.4 (1 Points) -----')
aa = [6,7,8,9]
bb = [3,2,34]
cc = aa + bb
print(cc)

# Problem 9.5 (3 Points)
print('\n----- Problem 9.5 (3 Points) -----')
combo2 = ['bad',[2,1,3],'100',20.5,'hello']
print(len(combo2))
print('The list contains five elements because it counts the embedded list as a single item!')
print(combo2[1][0])

# ============================================================================
# Problem 10.1 (2 Points)
print('\n----- Problem 10.1 (2 Points) -----')
lst = ['a','b','c','d','e']
print(lst)
lst[3]=[]       # method 1
del lst[1]      # method 2
lst.remove('c') # method 3
lst.pop(1)      # method 4
print(lst)

# Problem 10.2 (2 Points)
print('\n----- Problem 10.2 (2 Points) -----')
lista = [54,45,3,24,67,89,100]
lista.sort()
print(lista)
lista.reverse()
print(lista)

# Problem 10.3 (2 Points)
print('\n----- Problem 10.3 (2 Points) -----')
lstaa = ['1','b','3','d','5']
print(lstaa)
lstaa[0]='a'
lstaa[2]='c'
lstaa[4]='e'
lstaa.append('f')
    #OR
lstaa = lstaa + ['g']
print(lstaa)

# Problem 10.4 (2 Points)
print('\n----- Problem 10.4 (2 Points) -----')
LST = [100,50,25,0,-25,-50,-100]
print(LST)
LST[3:7]=[]
print(LST)

    
    
    
        
















