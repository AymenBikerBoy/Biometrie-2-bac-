import colorama
from colorama import Fore, Back, Style
from prettytable import PrettyTable
from math import *
colorama.init(autoreset=True)
#- Aymen Zainabi -#
p = "Realiser par Aymen Zainabi"
p = "\033[1;32m%s\033[0m" %p
a = "Xi"
a = "\033[93m%s\033[0m" %a
b = "Fi"
b = "\033[93m%s\033[0m" % b
c = "Xi x Fi"
c = "\033[93m%s\033[0m" % c
d = "Xi - x̄"
d = "\033[93m%s\033[0m" % d
e = "(Xi - x̄)²"
e = "\033[93m%s\033[0m" % e
f = "(Xi - x̄)² x Fi"
f = "\033[93m%s\033[0m" % f
print("######################################### BIOMETRIE 2-BAC #####################################")
#- Le type de la variation -#

option = float(input("Si la variation est discontinue taper 1, si la variation est continue taper 2: "))


#- la variation est discontinue -#
if option == 1:
# - Xi, Fi -#
    xi_1 = float(input("Xi_1: "))
    fi_1 = float(input("Fi_1: "))
    xi_2 = float(input("Xi_2: "))
    fi_2 = float(input("Fi_2: "))
    xi_3 = float(input("Xi_3: "))
    fi_3 = float(input("Fi_3: "))
    xi_4 = float(input("Xi_4: "))
    fi_4 = float(input("Fi_4: "))
    xi_5 = float(input("Xi_5: "))
    fi_5 = float(input("Fi_5: "))
    xi_6 = float(input("Xi_6: "))
    fi_6 = float(input("Fi_6: "))
    xi_7 = float(input("Xi_7: "))
    fi_7 = float(input("Fi_7: "))
    xi_8 = float(input("Xi_8: "))
    fi_8 = float(input("Fi_8: "))
    xi_9 = float(input("Xi_9: "))
    fi_9 = float(input("Fi_9: "))
    xi_10 = float(input("Xi_10: "))
    fi_10 = float(input("Fi_10: "))
    xi_11 = float(input("Xi_11: "))
    fi_11 = float(input("Fi_11: "))
    xi_12 = float(input("Xi_12: "))
    fi_12 = float(input("Fi_12: "))
#- Somme de Fi -#
    somme_fi = fi_1 + fi_2 + fi_3 + fi_4 + fi_5 + fi_6 + fi_7 + fi_8 + fi_9 + fi_10 + fi_11 +fi_12
# - Xi x Fi -#
    bar_1 = xi_1 * fi_1
    bar_2 = xi_2 * fi_2
    bar_3 = xi_3 * fi_3
    bar_4 = xi_4 * fi_4
    bar_5 = xi_5 * fi_5
    bar_6 = xi_6 * fi_6
    bar_7 = xi_7 * fi_7
    bar_8 = xi_8 * fi_8
    bar_9 = xi_9 * fi_9
    bar_10 = xi_10 * fi_10
    bar_11 = xi_11 * fi_11
    bar_12 = xi_12 * fi_12
#- Somme de Xi x Fi -#
    somme_bar = bar_1 + bar_2 + bar_3 + bar_4 + bar_5 + bar_6 + bar_7 + bar_8 + bar_9 + bar_10 +bar_11 +bar_12
# - X bar -#
    x_bar = somme_bar / somme_fi
#- (Xi - x̄) -#
    xi_xbar_1 = xi_1 - x_bar
    xi_xbar_2 = xi_2 - x_bar
    xi_xbar_3 = xi_3 - x_bar
    xi_xbar_4 = xi_4 - x_bar
    xi_xbar_5 = xi_5 - x_bar
    xi_xbar_6 = xi_6 - x_bar
    xi_xbar_7 = xi_7 - x_bar
    xi_xbar_8 = xi_8 - x_bar
    xi_xbar_9 = xi_9 - x_bar
    xi_xbar_10 = xi_10 - x_bar
    xi_xbar_11 = xi_11 - x_bar
    xi_xbar_12 = xi_12 - x_bar
#- (Xi - x̄)² -#
    xi_xbar_carre_1 = xi_xbar_1 ** 2
    xi_xbar_carre_2 = xi_xbar_2 ** 2
    xi_xbar_carre_3 = xi_xbar_3 ** 2
    xi_xbar_carre_4 = xi_xbar_4 ** 2
    xi_xbar_carre_5 = xi_xbar_5 ** 2
    xi_xbar_carre_6 = xi_xbar_6 ** 2
    xi_xbar_carre_7 = xi_xbar_7 ** 2
    xi_xbar_carre_8 = xi_xbar_8 ** 2
    xi_xbar_carre_9 = xi_xbar_9 ** 2
    xi_xbar_carre_10 = xi_xbar_10 ** 2
    xi_xbar_carre_11 = xi_xbar_11 ** 2
    xi_xbar_carre_12 = xi_xbar_12 ** 2
#- (Xi - x̄)² x Fi -#
    v_1 = xi_xbar_carre_1 * fi_1
    v_2 = xi_xbar_carre_2 * fi_2
    v_3 = xi_xbar_carre_3 * fi_3
    v_4 = xi_xbar_carre_4 * fi_4
    v_5 = xi_xbar_carre_5 * fi_5
    v_6 = xi_xbar_carre_6 * fi_6
    v_7 = xi_xbar_carre_7 * fi_7
    v_8 = xi_xbar_carre_8 * fi_8
    v_9 = xi_xbar_carre_9 * fi_9
    v_10 = xi_xbar_carre_10 * fi_10
    v_11 = xi_xbar_carre_11 * fi_11
    v_12 = xi_xbar_carre_12 * fi_12
#- somme de (Xi - x̄)² x Fi -#
    somme_v = v_1 + v_2 + v_3 + v_4 + v_5 + v_6 + v_7 + v_8 + v_9 + v_10 + v_11 + v_12
#- σ -#
    sigma = sqrt(somme_v / somme_fi)
#- CV = K -#
    cv = sigma * 100 / x_bar
#- interval de confiance -#
    min = x_bar - sigma
    max = x_bar + sigma

#- Table -#
    mytable = PrettyTable([a, b, c, d, e, f])
    mytable.add_row([xi_1, fi_1, bar_1, xi_xbar_1, xi_xbar_carre_1, v_1])
    mytable.add_row([xi_2, fi_2, bar_2, xi_xbar_2, xi_xbar_carre_2, v_2])
    mytable.add_row([xi_3, fi_3, bar_3, xi_xbar_3, xi_xbar_carre_3, v_3])
    mytable.add_row([xi_4, fi_4, bar_4, xi_xbar_4, xi_xbar_carre_4, v_4])
    mytable.add_row([xi_5, fi_5, bar_5, xi_xbar_5, xi_xbar_carre_5, v_5])
    mytable.add_row([xi_6, fi_6, bar_6, xi_xbar_6, xi_xbar_carre_6, v_6])
    mytable.add_row([xi_7, fi_7, bar_7, xi_xbar_7, xi_xbar_carre_7, v_7])
    mytable.add_row([xi_8, fi_8, bar_8, xi_xbar_8, xi_xbar_carre_8, v_8])
    mytable.add_row([xi_9, fi_9, bar_9, xi_xbar_9, xi_xbar_carre_9, v_9])
    mytable.add_row([xi_10, fi_10, bar_10, xi_xbar_10, xi_xbar_carre_10, v_10])
    mytable.add_row([xi_11, fi_11, bar_11, xi_xbar_11, xi_xbar_carre_11, v_11])
    mytable.add_row([xi_12, fi_12, bar_12, xi_xbar_12, xi_xbar_carre_12, v_12])
    mytable.add_row(["Σ", somme_fi, somme_bar, p, "Σ", somme_v])

#- les indices de dispertion -#
    print(mytable)
    print(Fore.YELLOW+"x̄ = ", x_bar)
    print(Fore.YELLOW+"σ = ", sigma)
    print(Fore.YELLOW+"[x̄ - σ,x̄ + σ] = " , "[{} , {}]".format(min , max) )
    if cv < 15:
        print(Fore.YELLOW+"                        cv = k = ", cv , Fore.RED+ " < 15%                   ")
        print("--->  La population est homogene et la dispertion est faible  <---")
    elif 15 <= cv <= 30:
        print(Fore.YELLOW+"                      cv = k = 15⩽ ", cv, Fore.RED+ " ⩽ 15%                      ")
        print("--->  l'homogenite de la population et la dispertion sont moyenne  <---")
    elif cv > 30 :
        print(Fore.YELLOW+"                        cv = k = ", cv, Fore.RED+ " > 30%                     ")
        print(Fore.YELLOW+"--->  la polpulation est heterogene et la dispertion est forte  <---")


#- la variation est continue -#
elif option == 2:
#- Xi, Fi -#
    st_1 = float(input("Saisie le debut de l interval: "))
    fn_1 = float(input("Saisie la fin de l'intervale: "))
    xi_1 = (st_1 + fn_1) / 2
    fi_1 = float(input("Fi_1: "))
    st_2 = float(input("Saisie le debut de l interval: "))
    fn_2 = float(input("Saisie la fin de l'intervale: "))
    xi_2 = (st_2 + fn_2) / 2
    fi_2 = float(input("Fi_2: "))
    st_3 = float(input("Saisie le debut de l interval: "))
    fn_3 = float(input("Saisie la fin de l'intervale: "))
    xi_3 = (st_3 + fn_3) / 2
    fi_3 = float(input("Fi_3: "))
    st_4 = float(input("Saisie le debut de l interval: "))
    fn_4 = float(input("Saisie la fin de l'intervale: "))
    xi_4 = (st_4 + fn_4) / 2
    fi_4 = float(input("Fi_4: "))
    st_5 = float(input("Saisie le debut de l interval: "))
    fn_5 = float(input("Saisie la fin de l'intervale: "))
    xi_5 = (st_5 + fn_5) / 2
    fi_5 = float(input("Fi_5: "))
    st_6 = float(input("Saisie le debut de l interval: "))
    fn_6 = float(input("Saisie la fin de l'intervale: "))
    xi_6 = (st_6 + fn_6) / 2
    fi_6 = float(input("Fi_6: "))
    st_7 = float(input("Saisie le debut de l interval: "))
    fn_7 = float(input("Saisie la fin de l'intervale: "))
    xi_7 = (st_7 + fn_7) / 2
    fi_7 = float(input("Fi_7: "))
    st_8 = float(input("Saisie le debut de l interval: "))
    fn_8 = float(input("Saisie la fin de l'intervale: "))
    xi_8 = (st_8 + fn_8) / 2
    fi_8 = float(input("Fi_8: "))
    st_9 = float(input("Saisie le debut de l interval: "))
    fn_9 = float(input("Saisie la fin de l'intervale: "))
    xi_9 = (st_9 + fn_9) / 2
    fi_9 = float(input("Fi_9: "))
    st_10 = float(input("Saisie le debut de l interval: "))
    fn_10 = float(input("Saisie la fin de l'intervale: "))
    xi_10 = (st_10 + fn_10) / 2
    fi_10 = float(input("Fi_10: "))
    st_11 = float(input("Saisie le debut de l interval: "))
    fn_11 = float(input("Saisie la fin de l'intervale: "))
    xi_11 = (st_11 + fn_11) / 2
    fi_11 = float(input("Fi_11: "))
    st_12 = float(input("Saisie le debut de l interval: "))
    fn_12 = float(input("Saisie la fin de l'intervale: "))
    xi_12 = (st_12 + fn_12) / 2
    fi_12 = float(input("Fi_12: "))
#- Somme de Fi -#
    somme_fi = fi_1 + fi_2 + fi_3 + fi_4 + fi_5 + fi_6 + fi_7 + fi_8 + fi_9 + fi_10 + fi_11 + fi_12
# - Xi x Fi -#
    bar_1 = xi_1 * fi_1
    bar_2 = xi_2 * fi_2
    bar_3 = xi_3 * fi_3
    bar_4 = xi_4 * fi_4
    bar_5 = xi_5 * fi_5
    bar_6 = xi_6 * fi_6
    bar_7 = xi_7 * fi_7
    bar_8 = xi_8 * fi_8
    bar_9 = xi_9 * fi_9
    bar_10 = xi_10 * fi_10
    bar_11 = xi_11 * fi_11
    bar_12 = xi_12 * fi_12
#- Somme de Xi x Fi -#
    somme_bar = bar_1 + bar_2 + bar_3 + bar_4 + bar_5 + bar_6 + bar_7 + bar_8 + bar_9 + bar_10 + bar_11 + bar_12
# - X bar -#
    x_bar = somme_bar / somme_fi
#- (Xi - x̄) -#
    xi_xbar_1 = xi_1 - x_bar
    xi_xbar_2 = xi_2 - x_bar
    xi_xbar_3 = xi_3 - x_bar
    xi_xbar_4 = xi_4 - x_bar
    xi_xbar_5 = xi_5 - x_bar
    xi_xbar_6 = xi_6 - x_bar
    xi_xbar_7 = xi_7 - x_bar
    xi_xbar_8 = xi_8 - x_bar
    xi_xbar_9 = xi_9 - x_bar
    xi_xbar_10 = xi_10 - x_bar
    xi_xbar_11 = xi_11 - x_bar
    xi_xbar_12 = xi_12 - x_bar
#- (Xi - x̄)² -#
    xi_xbar_carre_1 = xi_xbar_1 ** 2
    xi_xbar_carre_2 = xi_xbar_2 ** 2
    xi_xbar_carre_3 = xi_xbar_3 ** 2
    xi_xbar_carre_4 = xi_xbar_4 ** 2
    xi_xbar_carre_5 = xi_xbar_5 ** 2
    xi_xbar_carre_6 = xi_xbar_6 ** 2
    xi_xbar_carre_7 = xi_xbar_7 ** 2
    xi_xbar_carre_8 = xi_xbar_8 ** 2
    xi_xbar_carre_9 = xi_xbar_9 ** 2
    xi_xbar_carre_10 = xi_xbar_10 ** 2
    xi_xbar_carre_11 = xi_xbar_11 ** 2
    xi_xbar_carre_12 = xi_xbar_12 ** 2
#- (Xi - x̄)² x Fi -#
    v_1 = xi_xbar_carre_1 * fi_1
    v_2 = xi_xbar_carre_2 * fi_2
    v_3 = xi_xbar_carre_3 * fi_3
    v_4 = xi_xbar_carre_4 * fi_4
    v_5 = xi_xbar_carre_5 * fi_5
    v_6 = xi_xbar_carre_6 * fi_6
    v_7 = xi_xbar_carre_7 * fi_7
    v_8 = xi_xbar_carre_8 * fi_8
    v_9 = xi_xbar_carre_9 * fi_9
    v_10 = xi_xbar_carre_10 * fi_10
    v_11 = xi_xbar_carre_11 * fi_11
    v_12 = xi_xbar_carre_12 * fi_12
#- somme de (Xi - x̄)² x Fi -#
    somme_v = v_1 + v_2 + v_3 + v_4 + v_5 + v_6 + v_7 + v_8 + v_9 + v_10 + v_11 + v_12
#- σ -#
    sigma = sqrt(somme_v / somme_fi)
#- CV = K -#
    cv = sigma * 100 / x_bar
#- interval de confiance -#
    min = x_bar - sigma
    max = x_bar + sigma
#- Table -#
    mytable = PrettyTable([a, b, c, d, e, f])
    mytable.add_row([[st_1, fn_1],xi_1, fi_1, bar_1, xi_xbar_1, xi_xbar_carre_1, v_1])
    mytable.add_row([[st_2, fn_2],xi_2, fi_2, bar_2, xi_xbar_2, xi_xbar_carre_2, v_2])
    mytable.add_row([[st_3, fn_3],xi_3, fi_3, bar_3, xi_xbar_3, xi_xbar_carre_3, v_3])
    mytable.add_row([[st_4, fn_4],xi_4, fi_4, bar_4, xi_xbar_4, xi_xbar_carre_4, v_4])
    mytable.add_row([[st_5, fn_5],xi_5, fi_5, bar_5, xi_xbar_5, xi_xbar_carre_5, v_5])
    mytable.add_row([[st_6, fn_6],xi_6, fi_6, bar_6, xi_xbar_6, xi_xbar_carre_6, v_6])
    mytable.add_row([[st_7, fn_7],xi_7, fi_7, bar_7, xi_xbar_7, xi_xbar_carre_7, v_7])
    mytable.add_row([[st_8, fn_8],xi_8, fi_8, bar_8, xi_xbar_8, xi_xbar_carre_8, v_8])
    mytable.add_row([[st_9, fn_9],xi_9, fi_9, bar_9, xi_xbar_9, xi_xbar_carre_9, v_9])
    mytable.add_row([[st_10, fn_10],xi_10, fi_10, bar_10, xi_xbar_10, xi_xbar_carre_10, v_10])
    mytable.add_row([[st_11, fn_11],xi_11, fi_11, bar_11, xi_xbar_11, xi_xbar_carre_11, v_11])
    mytable.add_row([[st_12, fn_12],xi_12, fi_12, bar_12, xi_xbar_12, xi_xbar_carre_12, v_12])
    mytable.add_row(["","Σ", somme_fi, somme_bar, p, "Σ", somme_v])
#- les indices de dispertion -#
    print(mytable)
    print(Fore.YELLOW+"x̄ = ", x_bar)
    print(Fore.YELLOW+"σ = ", sigma)
    print(Fore.YELLOW+"[x̄ - σ,x̄ + σ] = ", "[{} , {}]".format(min, max))
    if cv < 15:
        print("                        cv = k = ", cv, " < 15                   ")
        print("--->  La population est homogene et la dispertion est faible  <---")
    elif 15 <= cv <= 30:
        print("                      cv = k = 15⩽ ", cv, " ⩽ 30                      ")
        print("--->  l'homogenite de la population et la dispertion sont moyenne  <---")
    elif cv > 30:
        print("                        cv = k = ", cv, " > 30                     ")
        print("--->  la polpulation est heterogene et la dispertion est forte  <---")
print( Fore.GREEN +'################################### D\u0332I\u0332M\u0332A\u0332 N\u0332I\u0332C\u0332E\u0332 ###################################')












