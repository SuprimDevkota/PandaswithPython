#This is a prediction for the admission list of students for BCT and BCE stream 2077 where in I used the past data to come up with the appropriate cutoff ranks...
#..The division of students into these streams were based upon the number representing their priority in an unfiltered priority list

import pandas as pd
df = pd.read_csv('datasets/priority list.csv')
df.set_index('Rank', inplace=True)
df.sort_index(inplace=True)

# COMPUTER ENGINEERING REGULAR
df_comp = df[df['p1']==11]  # 11 is used to denote BCT(regular)
comp_list = list(df_comp['Applicant Name'].head(27)) # 27 is the number of students(open) that got into this stream last year
print(*comp_list, sep=', ')

# COMPUTER ENGINEERING FULL FEE
df_comp = df[(df['p1']==11) &(df['p2']==12)] # 12 is used to denote BCT(full fee)
df_comp = df_comp.copy()
update_df_comp = df_comp.drop(df_comp.index[0:11],0)  # these 11 students would fall under BCT(regular) making their p2 unnecessary.
total_df_comp = update_df_comp.append(df[df['p1']==12]) # appending the list of eligible students with p1 =11 and p2 =12 AND those with p1 =11
total_df_comp.sort_index(inplace=True)
comp_list = list(total_df_comp['Applicant Name'].head(55)) #55 is the number of students(open) that got into this stream last year
print(*comp_list, sep=', ')

# CIVIL ENGINEERING REGULAR
df_civ1= df[(df.index > 65) & (df.index < 170)]  #65 and 170 were set as the floor and ceiling points because below 65 would easily fall in 1 while above 170 would not
df_civ1 = df_civ1[(df_civ1['p1']==11) & (df_civ1['p2']==1)] #civ1 denotes those students who didn't get into 11 and hence their p2 is invoked. 
df_civ2 = df[df['p1']==1] #civ2 denotes those with p1 = 1 
df_civ = df_civ2.append(df_civ1)
df_civ.sort_index(inplace=True)
civ_list = list(df_civ['Applicant Name'].head(81)) #81 is the number of students(open) that got into this stream last year
print(*civ_list, sep=', ')
