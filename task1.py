#__author__ = 'Lavanya'
from __future__ import division
import MySQLdb
import csv
import pdb
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
import pylab as pl

agegroup1_diseases1 = []
agegroup2_diseases1 = []
agegroup3_diseases1 = []
agegroup4_diseases1 = []
agegroup5_diseases1 = []
agegroup6_diseases1 = []
agegroup7_diseases1 = []
agegroup8_diseases1 = []
agegroup9_diseases1 = []
n1=0
n2=0
n3=0
n4=0
n5=0
n6=0
n7=0
n8=0
n9=0
disease1 = []
disease2 = []
disease3 = []
disease4 = []
disease5 = []
disease6 = []
disease7 = []
disease8 = []
disease9 = []
occurance1 = []
occurance2 = []
occurance3 = []
occurance4 = []
occurance5 = []
occurance6 = []
occurance7 = []
occurance8 = []
occurance9 = []

f = open("6339_Dataset_1(2).csv", "rb")
input_data = csv.reader(f)
for row in input_data:
    if row[0] == '1':
        n1=n1+1
    if row[0] == '2':
        n2=n2+1
    if row[0] == '3':
        n3=n3+1
    if row[0] == '4':
        n4=n4+1
    if row[0] == '5':
        n5=n5+1
    if row[0] == '6':
        n6=n6+1
    if row[0] == '7':
        n7=n7+1
    if row[0] == '8':
        n8=n8+1
    if row[0] == '9':
        n9=n9+1

    if row[0] == '1':
        agegroup1_diseases1.append(row[13])
    if row[0] == '2':
        agegroup2_diseases1.append(row[13])
    if row[0] == '3':
        agegroup3_diseases1.append(row[13])
    if row[0] == '4':
        agegroup4_diseases1.append(row[13])
    if row[0] == '5':
        agegroup5_diseases1.append(row[13])
    if row[0] == '6':
        agegroup6_diseases1.append(row[13])
    if row[0] == '7':
        agegroup7_diseases1.append(row[13])
    if row[0] == '8':
        agegroup8_diseases1.append(row[13])
    if row[0] == '9':
        agegroup9_diseases1.append(row[13])

    if row[0] == '1':
        agegroup1_diseases1.append(row[14])
    if row[0] == '2':
        agegroup2_diseases1.append(row[14])
    if row[0] == '3':
        agegroup4_diseases1.append(row[14])
    if row[0] == '4':
        agegroup4_diseases1.append(row[14])
    if row[0] == '5':
        agegroup5_diseases1.append(row[14])
    if row[0] == '6':
        agegroup6_diseases1.append(row[14])
    if row[0] == '7':
        agegroup7_diseases1.append(row[14])
    if row[0] == '8':
        agegroup8_diseases1.append(row[14])
    if row[0] == '9':
        agegroup9_diseases1.append(row[14])

def get_top3_diseases(listofdiseases):
    count3 = Counter(listofdiseases).most_common(3)
    return count3

def get_top3_diseases2(listofdiseases):
    d = []
    count3 = Counter(listofdiseases).most_common(3)
    for i in (0,1,2):
        d.append(count3[i][0])
    return d

def prevalence():
    a=get_top3_diseases(agegroup1_diseases1)
    #print "a: ", a
    print "\nAGE GROUP 1:"
    for i in (0, 1, 2):
        disease1.append(a[i][0])
        occurance1.append(a[i][1])
    print "\nTop 3 diseases in age group 1 are:\n", disease1
    print "\nNumber of people affected by this disease respectivele are:\n", occurance1
    for i in (0, 1, 2):
        prev = 100*(int(occurance1[i])/n1)
        print "\nAge Group 1, Prevalence(in %) of disease ", disease1[i], " = ", prev
    print "\nAGE GROUP 2:"
    a=get_top3_diseases(agegroup2_diseases1)
    for i in (0, 1, 2):
        disease2.append(a[i][0])
        occurance2.append(a[i][1])
    print "\nTop 3 diseases in age group 2 are:\n", disease2
    print "\nNumber of people affected by this disease respectivele are:\n", occurance2
    for i in (0, 1, 2):
        prev = 100*(int(occurance2[i])/n2)
        print "\nAge Group 2, Prevalence(in %) of disease ", disease2[i], " = ", prev
    print "\nAGE GROUP 3:"
    a=get_top3_diseases(agegroup3_diseases1)
    for i in (0, 1, 2):
        disease3.append(a[i][0])
        occurance3.append(a[i][1])
    print "\nTop 3 diseases in age group 3 are:\n", disease3
    print "\nNumber of people affected by this disease respectivele are:\n", occurance3
    for i in (0, 1, 2):
        prev = 100*(int(occurance3[i])/n3)
        print "\nAge Group 3, Prevalence(in %) of disease ", disease3[i], " = ", prev
    print "\nAGE GROUP 4:"
    a=get_top3_diseases(agegroup4_diseases1)
    for i in (0, 1, 2):
        disease4.append(a[i][0])
        occurance4.append(a[i][1])
    print "\nTop 3 diseases in age group 4 are:\n", disease4
    print "\nNumber of people affected by this disease respectivele are:\n", occurance4
    for i in (0, 1, 2):
        prev = 100*(int(occurance4[i])/n4)
        print "\nAge Group 4, Prevalence(in %) of disease ", disease4[i], " = ", prev
    print "\nAGE GROUP 5:"
    a=get_top3_diseases(agegroup5_diseases1)
    for i in (0, 1, 2):
        disease5.append(a[i][0])
        occurance5.append(a[i][1])
    print "\nTop 3 diseases in age group 5 are:\n", disease5
    print "\nNumber of people affected by this disease respectivele are:\n", occurance5
    for i in (0, 1, 2):
        prev = 100*(int(occurance5[i])/n5)
        print "\nAge Group 5, Prevalence(in %) of disease ", disease5[i], " = ", prev
    print "\nAGE GROUP 6:"
    a=get_top3_diseases(agegroup6_diseases1)
    for i in (0, 1, 2):
        disease6.append(a[i][0])
        occurance6.append(a[i][1])
    print "\nTop 3 diseases in age group 6 are:\n", disease6
    print "\nNumber of people affected by this disease respectivele are:\n", occurance6
    for i in (0, 1, 2):
        prev = 100*(int(occurance6[i])/n6)
        print "\nAge Group 6, Prevalence(in %) of disease ", disease6[i], " = ", prev
    print "\nAGE GROUP 7:"
    a=get_top3_diseases(agegroup7_diseases1)
    for i in (0, 1, 2):
        disease7.append(a[i][0])
        occurance7.append(a[i][1])
    print "\nTop 3 diseases in age group 7 are:\n", disease7
    print "\nNumber of people affected by this disease respectivele are:\n", occurance7
    for i in (0, 1, 2):
        prev = 100*(int(occurance7[i])/n7)
        print "\nAge Group 7, Prevalence(in %) of disease ", disease7[i], " = ", prev
    print "\nAGE GROUP 8:"
    a=get_top3_diseases(agegroup8_diseases1)
    for i in (0, 1, 2):
        disease8.append(a[i][0])
        #print "diseases: ",disease8
        occurance8.append(a[i][1])
    print "\nTop 3 diseases in age group 8 are:\n", disease8
    print "\nNumber of people affected by this disease respectivele are:\n", occurance8
    for i in (0, 1, 2):
        prev = 100*(int(occurance8[i])/n8)
        print "\nAge Group 8, Prevalence(in %) of disease ", disease8[i], " = ", prev
    print "\nAGE GROUP 9:"
    a=get_top3_diseases(agegroup9_diseases1)
    for i in (0, 1, 2):
        disease9.append(a[i][0])
        occurance9.append(a[i][1])
    print "\nTop 3 diseases in age group 9 are:\n", disease9
    print "\nNumber of people affected by this disease respectivele are:\n", occurance9
    for i in (0, 1, 2):
        prev = 100*(int(occurance9[i])/n9)
        print "\nAge Group 9, Prevalence(in %) of disease ", disease9[i], " = ", prev
#prevalence()


def get_topmost_disease(age, list_diseases):
    if age == '1':
        count = Counter(list_diseases).most_common()
    elif age == '3':
        count = Counter(list_diseases).most_common(2)
    else:
        count = Counter(list_diseases).most_common(1)
    print "\nMost common diseases in age group: ", age, "\n", count

'''get_topmost_disease('1', agegroup1_diseases1)
get_topmost_disease('2', agegroup2_diseases1)
get_topmost_disease('3', agegroup3_diseases1)
get_topmost_disease('4', agegroup4_diseases1)
get_topmost_disease('5', agegroup5_diseases1)
get_topmost_disease('6', agegroup6_diseases1)
get_topmost_disease('7', agegroup7_diseases1)
get_topmost_disease('8', agegroup8_diseases1)
get_topmost_disease('9', agegroup9_diseases1)
'''
def mortality1():
    men_alive = 0
    men_dead = 0
    women_alive = 0
    women_dead = 0
    n_men = 0
    n_women = 0
    f = open("6339_Dataset_1(2).csv", "rb")
    input_data = csv.reader(f)

    for row in input_data:
        if row[1] == '1':
            n_men = n_men + 1
        elif row[1] == '2':
            n_women = n_women +1
        if row[11] == 'Y' or row[12] == 'Y':
            if row[1] == '1' and row[4] == 'A':
                men_alive = men_alive + 1
            elif row[1] == '1' and row[4] == 'B':
                men_dead = men_dead + 1
            elif row[1] == '2' and row[4] == 'A':
                women_alive = women_alive + 1
            elif row[1] == '2' and row[4] == 'B':
                women_dead = women_dead + 1
    women_mortal = women_dead/n_women
    men_mortal = men_dead/n_men
    print "In hospital mortality of men:\nMen discharged alive: ", men_alive, "\nMen discharged dead: ", men_dead, "\nTotal number of men: ", n_men, "\nMen mortality rate: ", men_mortal
    print "\nIn hospital mortality of women:\nWomen discharged alive: ", women_alive, "\nWomen discharged dead: ",women_dead, "\nTotal number of men: ", n_women, "\nWomen mortality rate: ", women_mortal

#mortality1()

def mortality2(age, n, top3_diseases):
    #pdb.set_trace()
    ma = 0
    md = 0
    wa = 0
    wd = 0
    i = 0
    f = open("6339_Dataset_1(2).csv", "rb")
    input_data = csv.reader(f)
    for row in input_data:
        if row[0] == age:
            for i in (0,1,2):
                    if row[13] == top3_diseases[i] or row[14] == top3_diseases[i]:
                        if row[11] == 'Y' or row[12] == 'Y':
                            #print "inner: ",row[13]
                            #pdb.set_trace()
                            if row[1] == '1' and row[4] == 'A':
                                ma = ma+1
                                #print "ma:", ma
                            elif row[1] == '1' and row[4] == 'B':
                                md = md+1
                                #print "md:", md
                            elif row[1] == '2' and row[4] == 'A':
                                wa = wa+1
                                #print "wa:", wa
                            elif row[1] == '2' and row[4] == 'B':
                                wd = wd+1
                                #print "wd:", wd
    men_mortality = md/n
    women_mortality = wd/n
    #print "\nNumber of women discharged ALIVE in top 3 diseases of age group ", age, ": ", wa
    print "\nNumber of women discharged DEAD in top 3 diseases of age group ", age, ": ", wd
    #print "\nNumber of men discharged ALIVE in top 3 diseases of age group ", age, ": ", ma
    print "\nNumber of men discharged DEAD in top 3 diseases of age group ", age, ": ", md
    print "\nIn HOSPITAL MORTALITY of MEN in top 3 diseases of age group ",age, ": ", men_mortality
    print "\nIn HOSPITAL MORTALITY of WOMEN in top 3 diseases of age group ",age, ": ", women_mortality

'''d1= get_top3_diseases2(agegroup1_diseases1)
mortality2('1',n1, d1)
d2= get_top3_diseases2(agegroup2_diseases1)
mortality2('2',n2, d2)
d3= get_top3_diseases2(agegroup3_diseases1)
mortality2('3',n3, d3)
d4= get_top3_diseases2(agegroup4_diseases1)
mortality2('4',n4, d4)
d5= get_top3_diseases2(agegroup5_diseases1)
mortality2('5',n5, d5)
d6= get_top3_diseases2(agegroup6_diseases1)
mortality2('6',n6, d6)
d7= get_top3_diseases2(agegroup7_diseases1)
mortality2('7',n7, d7)
d8= get_top3_diseases2(agegroup8_diseases1)
mortality2('8',n8, d8)
d9= get_top3_diseases2(agegroup9_diseases1)
mortality2('9',n9, d9)'''

def demographic1(age_group):
    age = []
    stay= []
    age_stay_count = []
    f = open("6339_Dataset_1(2).csv", "rb")
    input_data = csv.reader(f)

    for row in input_data:
        age.append(row[0] if row[0]!= '' else "0")
        stay.append(row[5] if row[5] != '' else "0")
        if row[0] == age_group:
            age_stay_count.append(row[5] if row[5] != '' else "0")
    count = Counter(age_stay_count).most_common()
    print "\nStay Indicator for age group: ", age_group, "\n", count
    return count
'''demographic1('1')
demographic1('2')
demographic1('3')
demographic1('4')
demographic1('5')
demographic1('6')
demographic1('7')
demographic1('8')
demographic1('9')'''


def demographic2(race):
    f = open("6339_Dataset_1(2).csv", "rb")
    input_data = csv.reader(f)
    race_stay_count = []
    for row in input_data:
        if row[2] == race:
            race_stay_count.append(row[5] if row[5] != '' else "0")
    count = Counter(race_stay_count).most_common()
    print "\nStay indicator for race: ", race, "\n", count
    #return count

'''demographic2('1')
demographic2('2')
demographic2('3')
demographic2('4')
demographic2('5')
demographic2('6')'''

def demographic3(gender):
    f = open("6339_Dataset_1(2).csv", "rb")
    input_data = csv.reader(f)
    gender_stay_count = []
    for row in input_data:
        if row[1] == gender:
            gender_stay_count.append(row[5] if row[5] != '' else "0")
    count = Counter(gender_stay_count).most_common()
    print "\nStay indicator for gender: ", gender, "\n", count
    #return count
'''demographic3('1')
demographic3('2')'''

def draw_demographs():

    N = 9
    shortMeans   = np.array([4, 62, 211, 211, 199, 195, 206, 174, 110])
    longMeans = np.array([0, 6, 17, 9, 17, 17, 14, 14, 11])
    ageStd1 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
    ind=np.arange(N)
    width=0.50      # the width of the bars: can also be len(x) sequence

    p1 = plt.bar(ind, shortMeans,   width, color='b', yerr=ageStd1)
    p2 = plt.bar(ind, longMeans, width, color='r',
                 bottom=shortMeans, yerr=ageStd1)
    plt.ylabel('Stays')
    plt.title('Stays by age')
    plt.xticks(ind+width/2., ('1', '2', '3', '4', '5', '6', '7', '8', '9') )
    plt.yticks(np.arange(0,300,10))
    plt.legend( (p1[0], p2[0]), ('Short', 'Long') )
    plt.savefig('age_demograph')
#draw_demographs()

def draw2():
    N = 2
    ind=np.arange(N)
    width=0.50
    gender_short = np.array([594, 778])
    gender_long = np.array([50, 55])
    s = (1, 2)
    p1 = plt.bar(ind, gender_short,   width, color='b', yerr=s)
    p2 = plt.bar(ind, gender_long, width, color='r',
                 bottom=gender_short, yerr=s)
    plt.ylabel('Stays')
    plt.title('Stays by gender')
    plt.xticks(ind+width, ('Men', 'Women') )
    plt.yticks(np.arange(0,1300,100))
    plt.legend( (p1[0], p2[0]), ('Short', 'Long') )
    plt.savefig('gender_demograph')

#draw2()

def draw3():
    N = 6
    ind=np.arange(N)
    width=0.50
    race_short = np.array([1103, 187, 21, 13, 36, 7])
    race_long = np.array([88, 14, 0, 0, 3, 0])
    s= (1, 2, 3, 4, 5, 6)
    p1 = plt.bar(ind, race_short,   width, color='b', yerr=s)
    p2 = plt.bar(ind, race_long, width, color='r',
                 bottom=race_short, yerr=s)
    plt.ylabel('Stays')
    plt.title('Stays by race')
    plt.xticks(ind+width/2., ('1', '2', '3', '4', '5', '6'))
    plt.yticks(np.arange(0,1300,100))
    plt.legend( (p1[0], p2[0]), ('Short', 'Long') )
    plt.savefig('race_demograph')
#draw3()

def task3ii():
    common_diag_codel = []
    common_diag_codes = []
    f = open("6339_Dataset_1(2).csv", "rb")
    input_data = csv.reader(f)
    gender_stay_count = []
    for row in input_data:
        if row[5] == 'L':
            common_diag_codel.append(row[13] if row[13]!= '' else "0")
        if row[5] == 'S':
            common_diag_codes.append(row[13] if row[13]!= '' else "0")

    count = Counter(common_diag_codel).most_common(1)
    print "\n Most common primary diagnosis code for long stay: ", count
    count2 = Counter(common_diag_codes).most_common(1)
    print "\n Most common primary diagnosis code for short stay: ", count2
#task3ii()

def task5(age, n):
    discharge_dest = []
    f = open("6339_Dataset_1(2).csv", "rb")
    input_data = csv.reader(f)
    for row in input_data:
        if row[0] == age:
            discharge_dest.append(row[17])
    count = Counter(discharge_dest).most_common()
    max_dest = Counter(discharge_dest).most_common(1)[0][0]
    max_count = Counter(discharge_dest).most_common(1)[0][1]
    people_to_max = 100*(max_count/n)
    return count, people_to_max, max_dest
'''a1, b1, c1 = task5('1', n1)
print "For AGE GROUP 1 DISCHARGE DEST : NUMBER OF PEOPLE DISCHARGED TO THAT DESTINATION = \n", a1, "\nThe DISCHARGE DEST maximum people went to: ", c1, "\n% of people in AGE GROUP 1 who went to this DISCHARGE DEST: ", b1, "%"
a2, b2, c2 = task5('2', n2)
print "\nFor AGE GROUP 2 DISCHARGE DEST : NUMBER OF PEOPLE DISCHARGED TO THAT DESTINATION = \n", a2, "\nThe DISCHARGE DEST maximum people went to: ", c2, "\n% of people in AGE GROUP 2 who went to this DISCHARGE DEST: ", b2, "%"
a3, b3, c3 = task5('3', n3)
print "\nFor AGE GROUP 3 DISCHARGE DEST : NUMBER OF PEOPLE DISCHARGED TO THAT DESTINATION = \n", a3, "\nThe DISCHARGE DEST maximum people went to: ", c3, "\n% of people in AGE GROUP 3 who went to this DISCHARGE DEST: ", b3, "%"
a4, b4, c4 = task5('4', n4)
print "\nFor AGE GROUP 4 DISCHARGE DEST : NUMBER OF PEOPLE DISCHARGED TO THAT DESTINATION = \n", a4, "\nThe DISCHARGE DEST maximum people went to: ", c4, "\n% of people in AGE GROUP 4 who went to this DISCHARGE DEST: ", b4, "%"
a5, b5, c5 = task5('5', n5)
print "\nFor AGE GROUP 5 DISCHARGE DEST : NUMBER OF PEOPLE DISCHARGED TO THAT DESTINATION = \n", a5, "\nThe DISCHARGE DEST maximum people went to: ", c5, "\n% of people in AGE GROUP 5 who went to this DISCHARGE DEST: ", b5, "%"
a6, b6, c6 = task5('6', n6)
print "\nFor AGE GROUP 6 DISCHARGE DEST : NUMBER OF PEOPLE DISCHARGED TO THAT DESTINATION = \n", a6, "\nThe DISCHARGE DEST maximum people went to: ", c6, "\n% of people in AGE GROUP 6 who went to this DISCHARGE DEST: ", b6, "%"
a7, b7, c7 = task5('7', n7)
print "\nFor AGE GROUP 7 DISCHARGE DEST : NUMBER OF PEOPLE DISCHARGED TO THAT DESTINATION = \n", a7, "\nThe DISCHARGE DEST maximum people went to: ", c7, "\n% of people in AGE GROUP 7 who went to this DISCHARGE DEST: ", b7, "%"
a8, b8, c8 = task5('8', n8)
print "\nFor AGE GROUP 8 DISCHARGE DEST : NUMBER OF PEOPLE DISCHARGED TO THAT DESTINATION = \n", a8, "\nThe DISCHARGE DEST maximum people went to: ", c8, "\n% of people in AGE GROUP 8 who went to this DISCHARGE DEST: ", b8, "%"
a9, b9, c9 = task5('9', n9)
print "\nFor AGE GROUP 9 DISCHARGE DEST : NUMBER OF PEOPLE DISCHARGED TO THAT DESTINATION = \n", a9, "\nThe DISCHARGE DEST maximum people went to: ", c9, "\n% of people in AGE GROUP 9 who went to this DISCHARGE DEST: ", b9, "%"'''

def draw_graph5():
    N = 9
    ind=np.arange(N)
    width=0.50
    percent = np.array([75, 77.94, 69.74, 55.91, 60.19, 45.75, 43.64, 32.45, 42.15])
    dest = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1])
    s= (1, 2, 3, 4, 5, 6, 7, 8, 9)
    p1 = plt.bar(ind, percent,   width, color='b', yerr=s)
    plt.ylabel('Percentage of patients')
    plt.title('Percentage of patients to most common discharge destination by age group')
    plt.xticks(ind+width/2., ('1', '2', '3', '4', '5', '6', '7', '8', '9'))
    plt.yticks(np.arange(0,100,10))
    #plt.legend((p1[0]), ('Percentage of patients') )
    plt.savefig('task5')
#draw_graph5()


