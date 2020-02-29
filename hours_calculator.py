import pandas as pd
import os
import re
month="october"
path = os.getcwd()+"/"+month+"/"

folder = os.fsencode(path)
the_name="Yann"

filenames = []
i=1
hours_worked=0
def hasNumbers(inputString):
    return bool(re.search(r'\d', inputString))
count_month=0
for file in os.listdir(folder):

    filename = os.fsdecode(file)
    if filename.endswith('.xlsx'): # whatever file types you're using...
        filenames.append(filename[:-5])
        df=pd.read_excel(path+filename, index=False)
        df.rename(columns={'Unnamed: 0':"Member"}, inplace=True)
        df2=df.dropna(subset=['Member'])
        df2['combined']= df2.values.tolist()
        df4=df2.set_index('Member')
        shifts=df2.loc[df2['Member'] == the_name]['combined'].tolist()
        working=[]
        for b in shifts:
            for a in b:
                if hasNumbers(a)==True:
                    working.append(a)
        shift_dict=[]
        count=0
        for shift in working:
            total_hours=(float(shift.split('-')[1].replace('30','5'))-float(shift.split('-')[0].replace('30','5')))
            if total_hours >6:
                shift_dict.append(total_hours-0.5)
                count+=(total_hours-0.5)
            else:
                shift_dict.append(total_hours)
                count+=total_hours
                count.append(something)
        count_month+=count

print(hours_worked)
print(count_month)
