#import data set
import pandas as pd
df = pd.read_excel ("/Users/kathi/Desktop/dgthg/TAA_prox.xlsx")
df

#proximale landing zone CAVE LZ 1 sind eig LZ 1 und 0
df["prox_landing_zone"].value_counts()

# descriptive statistics - proximale landing zone
df[["Aneur_diam", "Aneur_volume", "PDLZ_length", "OVP_diam"]].describe()

# survival analysis
from lifelines import KaplanMeierFitter
kmf_survival = KaplanMeierFitter()
kmf_survival.fit(df["Months_Surv_FU"], df["Survival"], label='Survival Kaplan Meier Estimate')
kmf_survival.plot()

#reintervention analysis
# the data on reintervention includes NaNs in one row, index = 75
df_reintervention = df
df_reintervention = df_reintervention.drop(labels=75, axis = 0)


kmf_reintervention = KaplanMeierFitter()
kmf_reintervention.fit(df_reintervention["Months_Reinterv_FU"], df_reintervention["Reinterv"], label='Reintervention Kaplan Meier Estimate')
kmf_reintervention.plot()



# univariable analysis - cox regression Age, operative urgency, duration, Euroscore 2, post OP Neuro event
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
df_neuro = df[df['Euroscore2'].notna()]
cph_euroscore2.fit(df_neuro[["Euroscore2", "Months_Surv_FU", "Survival"]], duration_col="Months_Surv_FU", event_col= "Survival")
cph_euroscore2.print_summary() 
