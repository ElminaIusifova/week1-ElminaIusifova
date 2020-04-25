# # Zaman Səyahəti
#
# Eynşteynin nisbilik nəzəriyyəsinə görə cisim nə qədər sürətli hərəkət edərsə, onda onun çəkisi sürət faktoruna görə artar, zaman axışı isə yavaşlayar. Sürət faktorunun hesablanması aşağıdakı düsturla aparılır:
#
# ![Formula of factor](./images/formula.png)
#
# Burada **v** cismin sürətidir, **c** isə işıq sürətidir və 299,792,458 metr/saniyəyə bərabərdir.
#
# ## Program Specification
#
# Sizin proqramınız istifadəçidən cismin sürətinin işıq sürətinin neçə faizi olduğunu daxil olunmasını tələb etməlidir. Daha sonra faktoru hesablayaraq cismin çəkisini və aşağıdakı planetlərə və qalaktikalara çatacaq vaxtı hesablamalıdır:
#
# * Alpha Centauri: 4.3 işıq ili
# * Barnard’s Star: 6.0 işıq ili
# * Betelgeuse (Samanyolu qalaktikasındadır): 309 işıq ili
# * Andromeda Qalaktikası (Bizə ən yazın qalaktika): 2,000,000 işıq ili
#
# Nümunə:
#
# ![](./images/example.jpg)
#
# ---
#
# ***Powered by [TechAcademy](https://techacademy.az)***
#
#
# ***Please follow instructions on how you should solve this task***

from math import sqrt

c = 299792458
p = int(input("Please enter the velocity: "))
print ("Ship is travelling at the speed", p, "% of the speed of light")
v =(c * p)/100
f = 1/sqrt(1-(v*v)/(c*c))

w = int(input("Please enter the weight of the shuttle "))
weight = w*f
AC = 4.3/f
BS = 6.0/f
B = 309 /f
Andr =2000000/f
print("At this speed:\nWeight of the shuttle is:", weight,"\nPerceived time to travel Alpha Centauri", AC,
      "years.\nPerceived time to travel Barnard's Star",BS,
      "years.\nBetelgeuse", B,
      "years.\nAndromeda Galaxy", Andr, "years")




