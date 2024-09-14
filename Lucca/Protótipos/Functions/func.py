import numpy as np


"""
Questão 1

"""
def f_q1(x, y): #x,y ∈ [-100, 100]
  return x**2+y**2
lim_xy_q1 = [-100, 100]



"""
Questão 2

"""
def f_q2(x, y): #x ∈ [-2, 4], y ∈ [-2, 5]
  return -np.exp((x**2+y**2)) + 2*-np.exp(((x-1.7)**2)+(y-1.7)**2)
lim_x_q2 = [-2, 4]
lim_y_q2 = [-2, 5]



"""
Questão 3

"""
def f_q3(x,y): #x,y ∈ [-8, 8]
  return -20 * np.exp(-0.2*np.sqrt(0.5*(x**2+y**2))) - np.exp(0.5*(np.cos(2*np.pi*x) + np.cos(2*np.pi*y))) + 20 + np.exp(1)

lim_xy_q3 = [-8, 8]



"""
Questão 4

"""
def f_q4(x, y): #x,y ∈ [-5.12, 5.12]
  return ((x**2) - 10 * np.cos(2*np.pi*x)+10) + ((y**2) - 10 * np.cos(2*np.pi*y)+10)

lim_xy_q4 = [-5.12, 5.12]



"""
Questão 5

"""
def f_q5(x, y): # x,y ∈ [-10, 10]
  return (x*np.cos(x)/20) + 2 * np.exp(-(x**2)-((y-1)**2)) + 0.01 * x * y

lim_xy_q5 = [-10, 10]



"""
Questão 6

"""
def f_q6(x, y): # x,y ∈ [-1, 3]
  return x * np.sin(4*np.pi*x) - y * np.sin(4*np.pi*y + np.pi) + 1

lim_xy_q6 = [-1, 3]



"""
Questão 7

"""
def f_q7(x, y): # x,y ∈  [0, np.pi]
  return -np.sin(x) * (np.sin(x**2/np.pi)**20) - np.sin(y) * (np.sin(2*y**2/np.pi)**20)

lim_xy_q7 = [-0, np.pi]



"""
Questão 8

"""
def f_q8(x, y): # x,y ∈ [-200, 20]
  return -(y + 47) * np.sin(np.sqrt(np.abs(x/2 + (y + 47)))) - x * np.sin(np.sqrt(np.abs(x - (y + 47))))

lim_xy_q8 = [-200, 20]