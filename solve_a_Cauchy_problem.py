from math import exp
import matplotlib.pyplot as plt

def runge_kutt(f, f_d, x1, y1, r, n):
	h = r/n
	x_list = [x1]
	y_list = [y1]
	er_list = [0]
	for j in range(n):
		k1 = f(x_list[j],y_list[j])
		k2 = f(x_list[j]+h/2,y_list[j]+h/2*k1)
		k3 = f(x_list[j]+h/2,y_list[j]+h/2*k2)
		k4 = f(x_list[j]+h,y_list[j]+h*k3)
		yj= y_list[j]+h*(k1+2*k2+2*k3+k4)/6
		xj = x_list[j] + h
		x_list.append(xj)
		y_list.append(yj)
		er_list.append(yj - f_d(xj))
	return x_list, y_list , er_list


f1 = lambda x, y: exp(x)*(x+1)+(y/(x+1))
f2 = lambda x: exp(x)*(x+1)
x_list_rk, y_list_rk, er_list_rk = runge_kutt(f1, f2 ,0, 1, 1, 10)




def grid(x_list, y_list, f_d,):
	for element in range(len(x_list)):
		print(f"x = {round(x_list[element]*1000000)/1000000} y = {y_list[element]}\
		Er = {y_list[element] - f_d(x_list[element])}")

print("Runge kutt method")
grid(x_list_rk,y_list_rk, f2)


def adams_bush(f, f_d, x1, y1, r, n):
	h = r/n
	x_list = [x1]
	y_list = [y1]
	er_list = [0]
	f_d_list = [y1]
	for j in range(n):
		k1 = f(x_list[j],y_list[j])
		k2 = f(x_list[j]+h,y_list[j])
		k3 = f(x_list[j]-h,y_list[j])
		k4 = f(x_list[j]-2*h,y_list[j])
		dy = k4*55/24 - k3*59/24 + k2*37/24 - k1*3/8
		yj= y_list[j] + h*dy
		xj = x_list[j] + h
		x_list.append(xj)
		y_list.append(yj)
		er_list.append(yj - f_d(xj))
		f_d_list.append(f_d(xj))
	return x_list, y_list , er_list, f_d_list


x_list_ad, y_list_ad, er_list_ad, f_d_list_ad = adams_bush(f1, f2 ,0, 1, 1, 10)
print("Adams method")
grid(x_list_ad,y_list_ad, f2)
graph1=  plt.plot(x_list_ad,list(zip(f_d_list_ad, y_list_rk, y_list_ad )))
plt.xlabel('x')
plt.ylabel('y')
plt.legend(['y', 'Runge-Kut', 'Adams'])
plt.show()

graph2 = plt.plot(x_list_ad, list(zip(er_list_rk, er_list_ad)))
plt.xlabel('x')
plt.ylabel('y')
plt.legend(['Runge-Kut error', 'Adams error'])
plt.show()