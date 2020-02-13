#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'notebook')


# In[67]:


# Dependencies and Setup
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import pandas as pd
import csv
import os
import numpy as np

# Hide warning messages in notebook
import warnings
warnings.filterwarnings('ignore')

# File to Load (Remember to Change These)
ctd = os.path.join("data", "clinicaltrial_data.csv")
mdd = os.path.join("data", "mouse_drug_data.csv")



# In[77]:


# Read the Mouse and Drug Data and the Clinical Trial Data

df_ctd = pd.read_csv(ctd)

df_mdd = pd.read_csv(mdd)


# Combine the data into a single dataset


combined_df = pd.merge(df_ctd, df_mdd,
                    on ="Mouse ID",how='left')
combined.head()

# Display the data table for preview


# ## Tumor Response to Treatment

# In[79]:


# Store the Mean Tumor Volume Data Grouped by Drug and Timepoint 
 
merged_df = combined_df.groupby(["Drug", "Timepoint"])

mean_tumor_volume = merged_df["Tumor Volume (mm3)"].mean()

# Convert to DataFrame
merged_df = pd.DataFrame(mean_tumor_volume)
mean_tumor_volume_df = pd.DataFrame(mean_tumor_volume)

# Preview DataFrame
mean_tumor_volume_df = mean_tumor_volume_df.reset_index()
mean_tumor_volume_df.head()


# In[83]:


# # Store the Standard Error of Tumor Volumes Grouped by Drug and Timepoint
# standard_error = merged_df["Tumor Volume (mm3)"].sem()

# # # Convert to DataFrame
# standard_error_df = pd.DataFrame(standard_error)

# # Preview DataFrame
# # standard_error_df.reset_index(inplace=True)
# # standard_error_df.head()

standard_error = combined_df.groupby(["Drug","Timepoint"])["Tumor Volume (mm3)"].sem().reset_index()

# Convert to DataFrame
standard_error_df = pd.DataFrame(standard_error)

# Preview DataFrame
# standard_error_df.reset_index(inplace=True)
standard_error_df.head(100)


# In[44]:


# # Minor Data Munging to Re-Format the Data Frames
# reformat_tumor_df = 
# # Preview that Reformatting worked
reformat_tumor_df = mean_tumor_volume_df.pivot(index='Timepoint', columns='Drug', values='Tumor Volume (mm3)')
# Preview that Reformatting worked
reformat_tumor_df.head(5)


# In[45]:


# Generate the Plot (with Error Bars)

#plot options

drug=['Capomulin', 'Ceftamin', 'Infubinol', 'Ketapril', 'Naftisol', 'Placebo', 'Propriva', 'Ramicane', 'Stelasyn', 'Zoniferol']

x_axis=reshape_tumor_response_df.index
fig, ax = plt.subplots();

#ax.set_color_cycle(['red', 'black', 'yellow'])
ax.set(xlabel="Timepoint", ylabel= "Tumor Volume (mm3)", title="Plot with Error Bars")
ax.errorbar(x_axis, reshape_tumor_response_df['Capomulin'], yerr = None, linestyle="--", fmt='o', color='r', label="Capomulin")
ax.errorbar(x_axis, reshape_tumor_response_df['Infubinol'], yerr = None, linestyle="--", fmt= 'o', color='b', label="Infubinol")
ax.errorbar(x_axis, reshape_tumor_response_df['Ketapril'], yerr = None, linestyle="--", fmt='+', color='green', label="Ketapril")
ax.errorbar(x_axis, reshape_tumor_response_df['Placebo'], yerr = None, linestyle="--", fmt='D', color='black', label="Placebo")

ax.grid()
ax.legend(loc="best")

# Save the Figure
path=os.path.join(os.path.expanduser("~"), "Desktop", "Plot with Error Bar.png")
path
fig.savefig(path)


# ## Metastatic Response to Treatment

# In[84]:


# Store the Mean Met. Site Data Grouped by Drug and Timepoint 

average_met = combined_df.groupby(["Drug","Timepoint"])['Metastatic Sites'].mean().reset_index()

# Convert to DataFrame

met_response_df=pd.DataFrame(average_met)

# Preview DataFrame
met_response_df.head()


# In[86]:


# Store the Standard Error associated with Met. Sites Grouped by Drug and Timepoint 

# Store the Standard Error of Tumor Volumes Grouped by Drug and Timepoint
stderror_tumor_volume = combined_df.groupby(["Drug","Timepoint"])["Metastatic Sites"].sem().reset_index()
# Convert to DataFrame
standard_error_df=pd.DataFrame(stderror_tumor_volume)
# Preview DataFrame
standard_error_df.head()


# In[53]:


# Minor Data Munging to Re-Format the Data Frames
reshape_tumor_response_df = mean_tumor_volume_df.pivot(index='Timepoint', columns='Drug', values='Tumor Volume (mm3)')
# Preview that Reformatting worked
reshape_tumor_response_df.head()


# In[62]:



# Generate the Plot (with Error Bars)
x_axis=reshape_tumor_response_df.index
fig2, ax2 = plt.subplots();
ax2.set(xlabel="Treatment Duration (Days)", ylabel= "Met. Sites", title="Metastatic Spread During Treatment")
ax2.errorbar(x_axis, reshape_tumor_response_df['Capomulin'], yerr = None, linestyle="--", fmt='o', color='r', label="Capomulin")
ax2.errorbar(x_axis, reshape_tumor_response_df['Infubinol'], yerr = None, linestyle="--", fmt='d', color='b', label="Infubinol")
ax2.errorbar(x_axis, reshape_tumor_response_df['Ketapril'], yerr = None, linestyle="--", fmt='+', color='g', label="Ketapril")
ax2.errorbar(x_axis, reshape_tumor_response_df['Placebo'], yerr = None, linestyle="--", fmt='D', color='black', label="Placebo")
ax2.grid()
ax2.legend(loc="Inline label")

# Save the Figure
path=os.path.join(os.path.expanduser("~"), "Desktop", "Met Sites Plot with Error Bar.png")
path
fig.savefig(path)


# ## Survival Rates

# In[89]:


# Store the Count of Mice Grouped by Drug and Timepoint (W can pass any metric)
mouse_count= combined_df.groupby(["Drug","Timepoint"])['Mouse ID'].count().reset_index()
# Convert to DataFrame
mouse_count_df=pd.DataFrame(mouse_count)
#Rename Mouse ID to Mouse Count
mouse_count_df=mouse_count_df.rename(columns={"Mouse ID": "Mouse Count"})
# Preview DataFrame
mouse_count_df.head()


# In[91]:


# Minor Data Munging to Re-Format the Data Frames
reshape_mouse_count_df=mouse_count_df.pivot(index='Timepoint', columns='Drug', values='Mouse Count')
# Preview the Data Frame
reshape_mouse_count_df.head(100)


# In[93]:


#Convert survival rate into percentages
pct_survival_df=reshape_mouse_count_df.astype(float)
pct_survival_df["Capomulin_Survival_Percent"]=reshape_mouse_count_df["Capomulin"]/reshape_mouse_count_df["Capomulin"].iloc[0] * 100
pct_survival_df["Infubinol_Survival_Percent"]=reshape_mouse_count_df["Infubinol"]/reshape_mouse_count_df["Infubinol"].iloc[0] * 100
pct_survival_df["Ketapril_Survival_Percent"]=reshape_mouse_count_df["Ketapril"]/reshape_mouse_count_df["Ketapril"].iloc[0] * 100
pct_survival_df["Placebo_Survival_Percent"]=reshape_mouse_count_df["Placebo"]/reshape_mouse_count_df["Placebo"].iloc[0] * 100
pct_survival_df


# In[98]:


# Generate the Plot (Accounting for percentages)
fig3, ax3 = plt.subplots()
ax3.set(xlabel="Time (Days)", ylabel= "Survival Rate(%)", title="Survival During Treatment")
ax3.errorbar(pct_survival_df.index, pct_survival_df['Capomulin_Survival_Percent'], yerr = None, linestyle="--", fmt='o', color='r', label="Capomulin")
ax3.errorbar(pct_survival_df.index, pct_survival_df['Infubinol_Survival_Percent'], yerr = None, linestyle="--", fmt='d', color='b', label="Infubinol")
ax3.errorbar(pct_survival_df.index, pct_survival_df['Ketapril_Survival_Percent'], yerr = None, linestyle="--", fmt='-', color='g', label="Ketapril")
ax3.errorbar(pct_survival_df.index, pct_survival_df['Placebo_Survival_Percent'], yerr = None, linestyle="--", fmt='D', color='black', label="Placebo")
ax3.grid()
ax3.legend(loc="best")

# Save the Figure
path=os.path.join(os.path.expanduser("~"), "Desktop", "Survival During Treatment.png")
path
fig.savefig(path)


# Show the Figure
#plt.show()


# ## Summary Bar Graph

# In[112]:


# Calculate the percent changes for each drug
capomulin_per=(reshape_tumor_response_df["Capomulin"].iloc[9]-reshape_tumor_response_df["Capomulin"].iloc[0])/reshape_tumor_response_df["Capomulin"].iloc[0]*100
ceftamin_pert=(reshape_tumor_response_df["Ceftamin"].iloc[9]-reshape_tumor_response_df["Ceftamin"].iloc[0])/reshape_tumor_response_df["Ceftamin"].iloc[0]*100
infubinol_per=(reshape_tumor_response_df["Infubinol"].iloc[9]-reshape_tumor_response_df["Infubinol"].iloc[0])/reshape_tumor_response_df["Infubinol"].iloc[0]*100
ketapril_per=(reshape_tumor_response_df["Ketapril"].iloc[9]-reshape_tumor_response_df["Ketapril"].iloc[0])/reshape_tumor_response_df["Ketapril"].iloc[0]*100
naftisol_per=(reshape_tumor_response_df["Naftisol"].iloc[9]-reshape_tumor_response_df["Naftisol"].iloc[0])/reshape_tumor_response_df["Naftisol"].iloc[0]*100
placebo_per=(reshape_tumor_response_df["Placebo"].iloc[9]-reshape_tumor_response_df["Placebo"].iloc[0])/reshape_tumor_response_df["Placebo"].iloc[0]*100
propriva_per=(reshape_tumor_response_df["Propriva"].iloc[9]-reshape_tumor_response_df["Propriva"].iloc[0])/reshape_tumor_response_df["Propriva"].iloc[0]*100
ramicane_per=(reshape_tumor_response_df["Ramicane"].iloc[9]-reshape_tumor_response_df["Ramicane"].iloc[0])/reshape_tumor_response_df["Ramicane"].iloc[0]*100
stelasyn_per=(reshape_tumor_response_df["Stelasyn"].iloc[9]-reshape_tumor_response_df["Stelasyn"].iloc[0])/reshape_tumor_response_df["Stelasyn"].iloc[0]*100
zoniferol_per=(reshape_tumor_response_df["Zoniferol"].iloc[9]-reshape_tumor_response_df["Zoniferol"].iloc[0])/reshape_tumor_response_df["Zoniferol"].iloc[0]*100

# Store all Relevant Percent Changes into a Tuple
pct_tuple={'Capomulin': Capomulin_percent, 'Ceftamin': Ceftamin_percent, 'Infubinol': Infubinol_percent, 'Ketapril': Ketapril_percent,
          'Naftisol': Naftisol_percent, 'Placebo': Placebo_percent, 'Propriva': Propriva_percent, 'Ramicane': Ramicane_percent,
          'Stelasyn': Stelasyn_percent, 'Zoniferol': Zoniferol_percent}
# Display the data to confirm
pctchg_tumorvol=pd.Series(pct_tuple)
pctchg_tumorvol


# In[111]:


# Store all Relevant Percent Changes into a Tuple
meds=pctchg_tumorvol.keys()
meds
fig4, ax4 = plt.subplots()
x_axis = np.arange(0, len(meds))

# Splice the data between passing and failing drugs
colors=[]
for value in pctchg_tumorvol:
     if value>=0:
            colors.append('r')
     else: 
            colors.append('g')

# Orient widths. Add labels, tick marks, etc. 
ticks=[]
for x in x_axis:
    ticks.append(x + 0.)
plt.xticks(ticks, meds)

# Use functions to label the percentages of changes
pct_chg_bar = ax4.bar(x_axis, pctchg_tumorvol, color=colors, align="edge")
plt.xticks(rotation=45)
ax4.set(xlabel="Drugs", ylabel="Percentage Tumor Volume Change", title="Tumor Volume Change over 45 Days")

# Call functions to implement the function calls
for i, v in enumerate(pctchg_tumorvol):
    ax4.text(i+0.5, 
              v/pctchg_tumorvol[i]+10, 
              pctchg_tumorvol[i],
              fontsize=10, 
              color='white')

# Save the Figure
path=os.path.join(os.path.expanduser("~"), "Desktop", "Tumor Vol Chg over 45 Days")
path
fig3.savefig(path)

# Show the Figure
fig3.show()


# ![Metastatic Spread During Treatment](../Images/change.png)

# In[ ]:




