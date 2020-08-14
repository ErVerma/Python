import numpy as np 
import pandas as pd 
import re
data=pd.read_csv("Rainfall.csv")
#set index as any column
#data.set_index("SUBDIVISION",inplace=True)
print(data[110:206])
#pritn("Getting SUBDIVISION in Set")
sublist=[]
#creating set of subdivision to avoid Redundancy
subset={"ANDAMAN & NICOBAR ISLANDS"}
for col in data["SUBDIVISION"]:
	subset.add(col)
#convert set subset to list sublist
for s in subset:
	sublist.append(s)
#sublist contains list of subdivision
for subdivision in sublist:
	#columns contain Column Heading JAN to OCT-DEc
	for col in data.columns[2:]:
		mn = data.loc[data["SUBDIVISION"]==subdivision,[col]].mean()
		data.loc[data["SUBDIVISION"]==subdivision,[col]]=data.loc[data["SUBDIVISION"]==subdivision,[col]].fillna(mn)
	
print(data[110:206])

#create junesept list
junsept=[]
for col in data["Jun-Sep"]:
	junsept.append(col)
data["SouthWest-Monsoon"]=junsept
#print(data)
#create octdec list
octdec=[]
for col in data["Oct-Dec"]:
	octdec.append(col)
data["NorthEast-Monsoon"]=octdec
print(data[130:140])

#operation
#axis =1 apply to each row
#axis =0 apply to each column
#df['JUN10percent'] = df.apply(lambda row: row.JUN * 0.1, axis = 1) 

#create dictionary for subdivision and region classification
state_map = { 'ANDAMAN & NICOBAR ISLANDS' : 'SOUTH', 'ARUNACHAL PRADESH':'EAST', 'ASSAM & MEGHALAYA':'EAST',
                'NAGA MANI MIZO TRIPURA':'EAST', 'SUB HIMALAYAN WEST BENGAL & SIKKIM':'EAST', 'GANGETIC WEST BENGAL':'EAST',
                'ORISSA':'EAST','JHARKHAND':'EAST', 'BIHAR':'EAST', 'EAST UTTAR PRADESH':'NORTH', 'WEST UTTAR PRADESH':'NORTH',
                'UTTARAKHAND':'NORTH','HARYANA DELHI & CHANDIGARH':'NORTH','PUNJAB':'NORTH','HIMACHAL PRADESH':'NORTH',
                'JAMMU & KASHMIR':'NORTH','WEST RAJASTHAN':'WEST', 'EAST RAJASTHAN':'WEST','WEST MADHYA PRADESH':'WEST',
                'EAST MADHYA PRADESH':'EAST', 'GUJARAT REGION':'WEST', 'SAURASHTRA & KUTCH':'WEST', 'KONKAN & GOA':'WEST',
                'MADHYA MAHARASHTRA':'WEST','MATATHWADA':'WEST','VIDARBHA':'WEST','CHHATTISGARH':'EAST', 'COASTAL ANDHRA PRADESH':'SOUTH',
                'TELANGANA':'SOUTH', 'RAYALSEEMA':'SOUTH', 'TAMIL NADU':'SOUTH','COASTAL KARNATAKA':'SOUTH','NORTH INTERIOR KARNATAKA':'SOUTH',
                'SOUTH INTERIOR KARNATAKA':'SOUTH','KERALA':'SOUTH','LAKSHADWEEP':'SOUTH'
            }
data['Region']=np.nan
#setting region using fillna method
'''
#for subdivision in sublist:
for subdivision in sublist:
	for col in data.columns[20:]:
		data.loc[data["SUBDIVISION"]==subdivision,[col]]=data.loc[data["SUBDIVISION"]==subdivision,[col]].fillna(state_map[subdivision])
		
'''
#setting region using apply method
def fun1(x,state_map):
	if str(x.Region)=="nan":
		x.Region=state_map[x.SUBDIVISION]
	return x

data = data.apply(fun1,args=[state_map],axis=1)

print(data[300:380])
#generalising data for SouthWest Mon-soon and NorthEast Monsoon from 1901 to 2015
'''
RegionList=['SOUTH','WEST','NORTH','EAST']
l2=[]
l3=[]
newdata={'Region':RegionList,'NorthEast-Monsoon':l2,'SouthWest-Monsoon':l3}
for reg in RegionList:
	agg=re.findall('\d+\.\d+',str(data.loc[data["Region"]==reg,['NorthEast-Monsoon']].mean()))
	l2.append(agg)
for reg in RegionList:
	agg=re.findall('\d+\.\d+',str(data.loc[data["Region"]==reg,['SouthWest-Monsoon']].mean()))
	l3.append(agg)
		
dframe=pd.DataFrame(newdata)
#print(newdata)
print(dframe)
'''
#creating column RAINFALL-PREV1, RAINFALL-PREV2 and RAINFALL-PREV3

data['RAINFALL-PREV1']=data["ANNUAL"].shift(1)
data['RAINFALL-PREV2']=data["ANNUAL"].shift(2)
data['RAINFALL-PREV3']=data["ANNUAL"].shift(3)
#print(data['RAINFALL-PREV1'])
print(data[1:10])
		





	




