list1=[1121, "Jackie Grainger", 22.22,
 1122, "Jignesh Thrakkar", 25.25,
 1127, "Dion Green", 28.75, False,
 24.32, 1132, "Jacob Gerber",
 "Sarah Sanderson", 23.45, 1137, True,
 "Brandon Heck", 1138, 25.84, True,
 1152, "David Toma", 22.65,
 23.75, 1157, "Charles King", False,
 "Jackie Grainger", 1121, 22.22, False,
 22.65, 1152, "David Toma"]

#this dictionary contains all of the information in order
info={"names":[],"ID":[],"wage":[]}
#this dictionary stores values after valadation
dict1={"total_hourly_rate":[],"underpaid_salaries":[],"company_raises":[]}
list2=[]
#this for-loops gets rid of all bools and repeated values
for i in list1:
    if type(i)!=bool and  i not in list2:
        
        list2.append(i)
#stores respective information
for i in range(0,len(list2)):
    if type(list2[i])==str:
        info["names"].append(list2[i])
    elif type(list2[i])==float:
        info["wage"].append(list2[i])
    elif type(list2[i])==int:
        info["ID"].append(list2[i])

#stores new hourly wage
for i in range(len(info["wage"])):
    dict1["total_hourly_rate"].append(round(info["wage"][i]*1.3,2))

#stores  the underpaid workers spot and their wage
for i in range(len(dict1["total_hourly_rate"])):
    if dict1["total_hourly_rate"][i]>28.15 and dict1["total_hourly_rate"][i]<30.65:
         dict1["underpaid_salaries"].append([i,dict1["total_hourly_rate"][i]])
    else:
        dict1["underpaid_salaries"].append([-99,0])

#stores new company wages
for i in info["wage"]:
    if i>22 and i<24:
        dict1["company_raises"].append(round(i*1.05,2))
    elif i>23 and i<26:
        dict1["company_raises"].append(round(i*1.04,2))
    elif i>26 and i<28:
        dict1["company_raises"].append(round(i*1.03,2))
    else:
        dict1["company_raises"].append(round(i*1.02,2))

#formats and displays information
print ("{:<8} {:<17} {:<14}{:<20}{:<20}{:<14}".format('Id','Name of Worker','Wage','Total Hourly Wage','Underpaid Salaries','After Company Raises'))
print("===============================================================================================")
for i in range(len(info["names"])):
    if  dict1["underpaid_salaries"][i][0]==i:
        print ("{:<8} {:<17} {:<14}{:<20}{:<20}{:<14}".format(info["ID"][i], info["names"][i],info["wage"][i],dict1["total_hourly_rate"][i],"Underpaid",dict1["company_raises"][i]))
    else:
        print ("{:<8} {:<17} {:<14}{:<20}{:<20}{:<14}".format(info["ID"][i], info["names"][i],info["wage"][i],dict1["total_hourly_rate"][i],"         ",dict1["company_raises"][i]))




    
