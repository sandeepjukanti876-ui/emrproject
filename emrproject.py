import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(0)
n=100
data=pd.DataFrame({"patient_id":np.random.randint(1,20,n),
                   "age":np.random.randint(10,80,n),
                   "diagnosis":np.random.choice(["Diabetes","Hypertensior","Asthma","Flu"],n),
                   "date":pd.date_range(start="2023-01-01",periods=n,freq="D"),
                   "glucose":np.random.randint(70,200,n),
                   "bp_systolic":np.random.randint(90,180,n)})
print("Sample Data:")
print(data.head())
plt.figure()
plt.hist(data["age"],bins=10)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()
diag_counts=data["diagnosis"].value_counts()
plt.figure()
diag_counts.plot(kind="bar")
plt.title("most Frequent Diagnoses")
plt.xlabel("Diagnosis")
plt.ylabel("Count")
plt.show()
patient_sample=data[data["patient_id"]==data["patient_id"].iloc[0]]
plt.figure()
plt.plot(patient_sample["date"],patient_sample["glucose"])
plt.title("Glucose Over Time(Sample Patient)")
plt.xlabel("Date")
plt.ylabel("Glucose Level")
plt.xticks(rotation=45)
plt.show()
plt.figure()
plt.scatter(data["glucose"],data["bp_systolic"])
plt.title("Glucose vs Blood Pressure")
plt.xlabel("Glucose")
plt.ylabel("Systolic BP")
plt.show()
