
#import data set
import pandas as pd
df = pd.read_excel ("/Users..")
df

#proximale landing zone 
df["prox_landing_zone"].value_counts()

#table 1
df[["Age", "Euroscore2", "Duration"]].describe()

# descriptive statistics 
df[["Aneur_diam", "Aneur_volume", "PDLZ_length", "OVP_diam"]].describe()

# survival analysis
from lifelines import KaplanMeierFitter
from lifelines import survival_function_at_times
kmf_survival = KaplanMeierFitter()
kmf_survival.fit(df["Months_Surv_FU"], df["Survival"], label='Survival Kaplan Meier Estimate')
kmf_survival.survival_function_at_times(times=(0.99, 11.99, 35.99, 59.99, 119.99))
kmf_survival_years = KaplanMeierFitter()
kmf_survival_years.fit(df["exact_Years_Surv_FU"], df["Survival"], label='Survival Kaplan Meier Estimate')
kmf_survival_years.plot()

#reintervention analysis
# the data on reintervention includes NaNs in one row, index = 75
df_reintervention = df
df_reintervention = df_reintervention.drop(labels=75, axis = 0)
kmf_reintervention = KaplanMeierFitter()
kmf_reintervention.fit(df_reintervention["Months_Reinterv_FU"], df_reintervention["Reinterv"], label='Reintervention Kaplan Meier Estimate')
kmf_reintervention.survival_function_at_times(times=(0.99, 11.99, 35.99, 59.99, 119.99))


# 
from lifelines import CoxPHFitter
cph_age = CoxPHFitter()
cph_age.fit(df[["Age", "Months_Surv_FU", "Survival"]], duration_col="Months_Surv_FU", event_col= "Survival")
cph_age.print_summary()  

cph_duration = CoxPHFitter()
cph_duration.fit(df[["Duration", "Months_Surv_FU", "Survival"]], duration_col="Months_Surv_FU", event_col= "Survival")
cph_duration.print_summary() 

cph_urgency = CoxPHFitter()
cph_urgency.fit(df[["operative_urgency", "Months_Surv_FU", "Survival"]], duration_col="Months_Surv_FU", event_col= "Survival")
cph_urgency.print_summary() 

cph_neuro = CoxPHFitter()
cph_neuro.fit(df[["post_OP_neuro_event", "Months_Surv_FU", "Survival"]], duration_col="Months_Surv_FU", event_col= "Survival")
cph_neuro.print_summary() 

cph_euroscore2 = CoxPHFitter()
df_euroscore2 = df[df['Euroscore2'].notna()]
cph_euroscore2.fit(df_euroscore2[["Euroscore2", "Months_Surv_FU", "Survival"]], duration_col="Months_Surv_FU", event_col= "Survival")
cph_euroscore2.print_summary() 

### in R
# multivariable cox
### cut off analyse R maximally selected rank statistics


#
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
df['LZ_012'] = np.where(df['prox_landing_zone'] != 3, 'LZ 0-2', 'LZ 3')
ax = sns.boxplot(x=df['LZ_012'], y=df['PDLZ_length'], data= df, color = "cornflowerblue").set(xlabel="proximal device landing zone", ylabel="length of landing zone (mm)")


#
df['LZ_01'] = np.where(df['prox_landing_zone'] == 1, 1, 0)
cph_LZ_reintervention = CoxPHFitter()
df_LZ_reintervention = df[df['LZ_01'].notna()]
df_LZ_reintervention = df[df['Months_Reinterv_FU'].notna()]
cph_LZ_reintervention.fit(df_LZ_reintervention[["LZ_01", "Months_Reinterv_FU", "Reinterv"]], duration_col="Months_Reinterv_FU", event_col= "Reinterv")
cph_LZ_reintervention.print_summary() 

#
cph_LZ_survival = CoxPHFitter()
df_LZ_survival= df[df['LZ_01'].notna()]
cph_LZ_survival.fit(df_LZ_survival[["LZ_01", "Months_Surv_FU", "Survival"]], duration_col="Months_Surv_FU", event_col= "Survival")
cph_LZ_survival.print_summary() 

