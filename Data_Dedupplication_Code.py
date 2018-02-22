
# coding: utf-8

# In[38]:

import math 
import pandas as pd
import csv
import fuzzywuzzy as fuzz
import extdata


# In[ ]:

train=pd.read_csv(extdata.training)
test=pd.read_csv(extdata.test)
flag=1
dtset1=pd.DataFrame(columns=['ln','dob','gn','fn','full_name_dob'])
dtset2=pd.DataFrame(columns=['ln','dob','gn','fn','full_name_dob'])
print("Training Data separated into two dataframes: Males and Females.\n")
for i in range(len(train)):
    if train.loc[i,'gn']=='F':
        dtset1=dtset1.append(train.loc[i])
    else:
        dtset2=dtset2.append(train.loc[i])
dtset1_test=pd.DataFrame(columns=['ln','dob','gn','fn','full_name_dob'])
dtset2_test=pd.DataFrame(columns=['ln','dob','gn','fn','full_name_dob'])
for i in range(len(test)):
    if test.loc[i,'gn']=='F':
        dtset1_test=dtset1.append(test.loc[i])
    else:
        dtset2_test=dtset2.append(test.loc[i])

print("Training of Dataframe containing female patients starts........\n")
F_UniqueNameCount=extdata.F_UniqueNameCount
F_Dist=math.inf
F_threshold=-0.5
dtset1=dtset1.reset_index(drop=True)
dtset2=dtset2.reset_index(drop=True)
dtset1_test=dtset1_test.reset_index(drop=True)
dtset2_test=dtset2_test.reset_index(drop=True)
while flag:
    F_threshold+=0.5
    F_count=0
    F_dobW=F_threshold
    F_uniqueNms=[]
    F_labels={}
    for i in range(len(dtset1)):
        F_labels[i]=-1
    for i in range(len(dtset1)):
        for j in range(len(dtset1)):
            F_fn_C=(max((dtset1[i]['fn'].str.len()),(dtset1[j]['fn'].str.len())))*(1-fuzz.ratio(dtset1[i]['fn'],dtset1[j]['fn'])/100)
            F_ln_C=(max((dtset1[i]['ln'].str.len()),(dtset1[j]['ln'].str.len())))*(1-fuzz.ratio(dtset1[i]['ln'],dtset1[j]['ln'])/100)
            F_dobC=(dtset1[i]['dob']!=dtset1[j]['dob'])*dobW
            if(F_fn_C+F_ln_C+F_dobC<threshold): 
                if F_labels[j]==-1 and F_labels[i]==-1:
                    F_labels[j]=F_count
                    F_count+=1
                    F_labels[i]=F_labels[j]
                else :
                    if F_labels[j]==-1:
                        F_labels[j]=F_labels[i]
                    elif F_labels[i]==-1:
                        F_labels[i]=F_labels[j]
                    else :
                        labels[i]=min(F_labels[i],F_labels[j])
                        F_labels[j]=F_labels[i]
            else:
                if F_labels[i]==-1:
                    F_labels[i]=F_count
                    F_count+=1
                if F_labels[j]==-1:
                    F_labels[j]=F_count
                    F_count+=1
    F_labels=sorted(F_labels.items(),key=lambda x:x[1])
    F_count=0
    for frows in F_labels:
        if F_count<=frows[1]:
            F_uniqueNms.append(dset1[rows[0]])
            F_count=frows[1]+1
    if F_Dist> abs(len(F_uniqueNms)-F_UniqueNameCount):
        F_Dist=abs(len(F_uniqueNms)-F_UniqueNameCount)
        FOptValThreshold=F_threshold
        flag=1
    else: 
        flag=0
print("System has been Trained.")
print("Optimum value of the Threshold is ", FOptValThreshold)
print("Applying the threshold value on the  required female testing Data.\n TESTING......")
F_threshold=FOptValThreshold
dobW=F_threshold;
F_uniqueNms=[]
F_labels={}
F_count=0
for i in range(len(dtset1_test)):
    F_labels[i]=-1
for i in range(len(dtset1_test)):
    for j in range(len(dtset1_test)):
        F_fn_C=F_fn_C=(max((dtset1_test[i]['fn'].str.len()),(dtset1[j]['fn'].str.len())))*(1-fuzz.ratio(dtset1_test[i]['fn'],dtset1_test[j]['fn'])/100)
        F_ln_C=(max((dtset1_test[i]['ln'].str.len()),(dtset1_test[j]['ln'].str.len())))*(1-fuzz.ratio(dtset1_test[i]['ln'],dtset1_test[j]['ln'])/100)
        F_dobC=dobW*(dtset1_test[i]['dob']!=dtset1_test[j]['dob'])
        if(F_fn_C+F_ln_C+F_dobC<F_threshold): 
                if F_labels[j]==-1 and F_labels[i]==-1:
                    F_labels[j]=F_count
                    F_count+=1
                    F_labels[i]=F_labels[j]
                else :
                    if F_labels[j]==-1:
                        F_labels[j]=F_labels[i]
                    elif F_labels[i]==-1:
                        F_labels[i]=F_labels[j]
                    else :
                        labels[i]=min(F_labels[i],F_labels[j])
                        F_labels[j]=F_labels[i]
        else:
                if F_labels[i]==-1:
                    F_labels[i]=F_count
                    F_count+=1
                if F_labels[j]==-1:
                    F_labels[j]=F_count
                    F_count+=1
F_labels=sorted(F_labels.items(),key=lambda k:k[1])

F_tempLabels={}
F_count=0
F_labCount=0

F_temp=-1
for frows in F_labels:
    if F_temp==frows[1]:
        F_tempLabels[frows[0]]=F_labCount
    else :
        F_labCount+=1;
        F_tempLabels[frows[0]]=F_labCount
    F_temp=frows[1]
    if F_count<=frows[1]:
        F_uniqueNms.append(dtset1_test[rows[0]])
        F_count=frows[1]+1
fy_labels=[0 for i in range(len(dtset1_test))]
for frows in F_tempLabels:
    fy_labels[frows]=F_tempLabels[frows]
F_output=pd.DataFrame(columns=['ln','dob','gn','fn'])
p=0
for i in range(len(F_uniqueNms)):
    F_output[p]=dtset_test[F_output[i]]
#--------------------------------------Female output came---------------------------
flag=1
print("Training of Dataframe containing male patients starts........\n")
M_UniqueNameCount=extdata.M_UniqueNameCount
M_Dist=math.inf
M_threshold=-0.5
while flag:
    M_threshold+=0.5
    M_count=0
    M_dobW=M_threshold
    M_uniqueNms=[]
    M_labels={}
    for i in range(len(dtset2)):
        M_labels[i]=-1
    for i in range(len(dtset2)):
        for j in range(len(dtset2)):
            M_fn_C=(max((dtset2[i]['fn'].str.len()),(dtset2[j]['fn'].str.len())))*(1-fuzz.ratio(dtset2[i]['fn'],dtset2[j]['fn'])/100)
            M_ln_C=(max((dtset2[i]['ln'].str.len()),(dtset2[j]['ln'].str.len())))*(1-fuzz.ratio(dtset2[i]['ln'],dtset2[j]['ln'])/100)
            M_dobC=(dtset2[i]['dob']!=dtset2[j]['dob'])*dobW
            if(M_fn_C+M_ln_C+M_dobC<threshold): 
                if M_labels[j]==-1 and M_labels[i]==-1:
                    M_labels[j]=M_count
                    M_count+=1
                    M_labels[i]=M_labels[j]
                else :
                    if M_labels[j]==-1:
                        M_labels[j]=M_labels[i]
                    elif M_labels[i]==-1:
                        M_labels[i]=M_labels[j]
                    else :
                        labels[i]=min(M_labels[i],M_labels[j])
                        M_labels[j]=M_labels[i]
            else:
                if M_labels[i]==-1:
                    M_labels[i]=M_count
                    M_count+=1
                if M_labels[j]==-1:
                    M_labels[j]=M_count
                    M_count+=1
    M_labels=sorted(M_labels.items(),key=lambda x:x[1])
    M_count=0
    for mrows in M_labels:
        if M_count<=mrows[1]:
            M_uniqueNms.append(dset1[rows[0]])
            M_count=mrows[1]+1
    if M_Dist> abs(len(M_uniqueNms)-M_UniqueNameCount):
        M_Dist=abs(len(M_uniqueNms)-M_UniqueNameCount)
        MOptValThreshold=M_threshold
        flag=1
    else: 
        flag=0
print("System has been Trained.")
print("Optimum value of the Threshold is ", MOptValThreshold)
print("Applying the threshold value on the  required female testing Data.\n TESTING......")
M_threshold=MOptValThreshold
dobW=M_threshold;
M_uniqueNms=[]
M_labels={}
M_count=0
for i in range(len(dtset2_test)):
    M_labels[i]=-1
for i in range(len(dtset2_test)):
    for j in range(len(dtset2_test)):
        M_fn_C=M_fn_C=(max((dtset2_test[i]['fn'].str.len()),(dtset2[j]['fn'].str.len())))*(1-fuzz.ratio(dtset2_test[i]['fn'],dtset2_test[j]['fn'])/100)
        M_ln_C=(max((dtset2_test[i]['ln'].str.len()),(dtset2_test[j]['ln'].str.len())))*(1-fuzz.ratio(dtset2_test[i]['ln'],dtset2_test[j]['ln'])/100)
        M_dobC=dobW*(dtset2_test[i]['dob']!=dtset2_test[j]['dob'])
        if(M_fn_C+M_ln_C+M_dobC<M_threshold): 
                if M_labels[j]==-1 and M_labels[i]==-1:
                    M_labels[j]=M_count
                    M_count+=1
                    M_labels[i]=M_labels[j]
                else :
                    if M_labels[j]==-1:
                        M_labels[j]=M_labels[i]
                    elif M_labels[i]==-1:
                        M_labels[i]=M_labels[j]
                    else :
                        labels[i]=min(M_labels[i],M_labels[j])
                        M_labels[j]=M_labels[i]
        else:
                if M_labels[i]==-1:
                    M_labels[i]=M_count
                    M_count+=1
                if M_labels[j]==-1:
                    M_labels[j]=M_count
                    M_count+=1
M_labels=sorted(M_labels.items(),key=lambda k:k[1])

M_tempLabels={}
M_count=0
M_labCount=0

M_temp=-1
for mrows in M_labels:
    if M_temp==mrows[1]:
        M_tempLabels[mrows[0]]=M_labCount
    else :
        M_labCount+=1;
        M_tempLabels[mrows[0]]=labCount
    M_temp=mrows[1]
    if M_count<=mrows[1]:
        M_uniqueNms.append(dtset2_test[rows[0]])
        M_count=mrows[1]+1
my_labels=[0 for i in range(len(dtset2_test))]
for mrows in M_tempLabels:
	my_labels[mrows]=M_tempLabels[mrows]
	# print(rows)
M_output=pd.DataFrame(columns=['ln','dob','gn','fn'])
p=0
for i in range(len(M_uniqueNms)):
    M_output[p]=dtset_test[M_output[i]]
#--------------------------------------male output came---------------------------
frames=[F_output,M_output]
dedupe_output=pd.concat(frames)
dedupe_output=dedupe_output.reset_index(drop=True)
dedupe_output.to_csv('output.csv', sep='\t', encoding='utf-8')
print("Unique data: ", M_UniqueNms+F_UniqueNms)
print("Output has been saved  as ", extdata.output, ".")


# In[ ]:



