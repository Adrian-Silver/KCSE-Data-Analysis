import pandas as pd
import matplotlib.pyplot as plt
import re
from sqlalchemy import create_engine

ress = pd.read_csv("KCSE_2016.csv", header=0, sep=",", skipinitialspace=True)
alls = pd.read_csv("All_Cs.csv", header=0, sep=",")
fems = pd.read_csv("Fems.csv", header=0, sep=",")
quals = pd.read_csv("UniQual.csv", header=0, sep=",")

# print(ress)
# print(ress.info())
# print(ress.describe())

# print(ress.loc[ress["Gender"] == "FEMALE"])

# print(ress.sort_values("Gender"))
# print(ress.iloc[0:4])

# ress2 = ress.loc[ress["Gender"].str.contains("FEMALE")]

# ress3 = ress.loc[~ress["Gender"].str.contains("FEMALE" and "MALE")]

ress2 = ress.loc[ress["Gender"].str.contains("FEM*")]

# ress2 = ress.loc[ress["Gender"].str.contains("FEMALE")]

# print(ress2)
# print(ress.iloc[19, 0])

# print(ress2)

# ress2.to_csv("Females.csv")

# ress4 = ress.loc[~ress["Gender"].str.contains("FEMALE")]

# print(ress)

# print(ress4)

# ress3.to_csv("All_Cands.csv")

# ress5 = ress.loc[ress["Gender"].str.contains("MALE") and (~"FEM*")]
# print(ress5)

# print(ress3)
# ress2 = ress.loc[ress["Gender"].str.contains("FEMALE")]
# ress2 = ress.loc[ress["Gender"].str.contains("FEMALE")]

ress[["Gender", "Year"]] = ress["Gender"].str.split("(", expand=True)
ress[["Year", "Noo"]] = ress["Year"].str.split(")", expand=True)

ress = ress.drop(columns=["Noo"])

cols_pos = list(ress.columns)
ress = ress[[cols_pos[0]] + [cols_pos[-1]] + cols_pos[1:15]]

ress = ress.loc[:, ~ress.columns.duplicated()]

ress["Total"] = ress.iloc[:, 2:].sum(axis=1)

ress = ress.sort_values(["Year", "Gender"], ascending=[1, 0])

# ress["Gender"].str.strip()

# print(ress)

# ress_m = ress.loc[ress["Gender"] == "MALE"]
# print(ress_m)

# ress_m.to_csv("Males.csv")

# ress_f = ress.loc[ress["Gender"] == "FEMALE"]
# print(ress_f)
# ress_f.to_csv("Fems.csv")

# Separating Quality Grades
# cols_pos2 = list(ress.columns)

# ress_q = ress[cols_pos2[0:8]]
# print(ress[cols_pos2[0:8]])
# print(ress_q)

# ress_q.to_csv("UniQual.csv")

# Did not qualify to join university
# cols_pos3 = list(ress.columns)
# ress_nq = ress[cols_pos[0:1] + [cols_pos[-1]] + cols_pos3[8:14]]
# print(ress_nq)

# ress_nq.to_csv("UniDNQ.csv")

fems.drop(fems.columns[fems.columns.str.contains("unnamed", case=False)], axis=1, inplace=True)
# print(fems)

# Comparing the total number of candidates over the Years

# print(alls)
# cols_t = alls.columns
# fig_t, ax_t = plt.subplots()

# plt.xlabel("Year")
# plt.ylabel("No. of Candidates")
# plt.title("Total Number of Candidates over the Years")
# ax_t.bar(alls[cols_t[2]], alls[cols_t[15]])
# plt.show()


# ress_a = ress.loc[ress["Gender"] == "ALL"]

# print(ress_a)
# ress_a.to_csv("All_Cs.csv")
alls.drop(alls.columns[alls.columns.str.contains('unnamed', case=False)], axis=1, inplace=True)
alls.set_index("Year", drop=True, inplace=True)
# alls = alls.drop(columns="Total")
# alls = alls.drop(columns=["0"])
print(alls)

# alls_bar = alls.plot.bar()
# plt.xlabel("Year")
# plt.ylabel("No. of Candidates")
# plt.title("Grade Distribution of Candidates")
# plt.show()

# plt.plot.bar()
# print(alls_bar)

# How do quality grades compare to non-quality grades?

alls["Quality_Sum"] = alls["A"] + alls["A-"] + alls["B+"] + alls["B"] + alls["B-"] + alls["C+"]
alls["NQuality_Sum"] = alls["C"] + alls["C-"] + alls["D+"] + alls["D"] + alls["D-"] + alls["E"]

alls["Quality_Difference"] = alls["NQuality_Sum"] - alls["Quality_Sum"]
alls["Quality_Percentage"] = (alls["Quality_Sum"] / alls["Total"]) * 100
alls["NQuality_Percentage"] = (alls["NQuality_Sum"] / alls["Total"]) * 100
alls["Quality_Percentage_Difference"] = alls["NQuality_Percentage"] - alls["Quality_Percentage"]
print(alls)

quals.drop(quals.columns[quals.columns.str.contains("unnamed", case=False)], axis=1, inplace=True)
# quals["Total_Sum"] = quals.iloc[:, 2:8].sum(axis=1)
# print(quals)

# Line graph showing the total number of candidates over the years

# print(alls["Total"])
# alls["Total"].plot(kind="line")
# plt.ylabel("No. of Candidates")
# plt.title("Total Number of Candidates over the years")
# plt.show()

# Pie graph showing the difference between quality grades and non-quality grades
# In 2015, there was the least gap between quality grades and non-quality grades

print(alls["Quality_Percentage_Difference"].idxmin())

# In 2016, there was the largest gap between quality grades and non-quality grades
print(alls["Quality_Percentage_Difference"].idxmax())

# How does the performance between men and won=men compare?

# Grade performance in males

males_results = ress[ress.Gender.str.startswith("MALE")].drop(columns=["Gender", "Total"]).set_index("Year")
# print(males_results)
# plt.figure(figsize=(12, 4))
# plt.subplot(1, 2, 1)
# plt.xlabel("Years")
# plt.ylabel("Number of Male Candidates")
# plt.legend(males_results)
# plt.title("Grade Performance in Males ")
# plt.plot(males_results)
# plt.show()

# Grade performance in females
females_results = ress[ress.Gender.str.startswith("FEMALE")].drop(columns=["Gender", "Total"]).set_index("Year")
# print(females_results)
# plt.figure(figsize=(12, 4))
# plt.subplot(1, 2, 1)
# plt.xlabel("Years")
# plt.ylabel("Number of Female Candidates")
# plt.legend(females_results.columns)
# plt.title("Grade Performance in Females")
# plt.plot(females_results)
# plt.show()

# Issue: Legend does not display column values


# Mean grade over the years
males_mean = males_results.mean(axis=0)
females_mean = females_results.mean(axis=0)

plt.subplot(1, 1, 1)
plt.title("Mean of Each Grade Over the Years")

males_mean.plot()
females_mean.plot()
plt.legend(["Male", "Female"])
plt.show()

# This shows that the most common grade in males over the years is D+ while
#    the most common grade in females over the years is D

# Has the gap in difference increased or decreased?
# quality_comparison = alls(alls["NQuality_Percentage"], alls["Quality_Percentage"])
# print(quality_comparison)

# cols_alls2 = list(alls.columns)
# quality_comparison = alls[cols_alls2[-3] + [cols_alls2[-1]] + alls[cols_alls2[-2]]]
# print(quality_comparison)


alls["Quality_Total"] = (alls.sum(axis=0).loc["Quality_Sum"] / alls.sum(axis=0).loc["Total"]) * 100
alls["NQuality_Total"] = (alls.sum(axis=0).loc["NQuality_Sum"] / alls.sum(axis=0).loc["Total"]) * 100
# dataframe_copy.loc['Percent_Totals'] = [dataframe_grade_quality_percent, dataframe_grade_non_quality_percent]
# percents = [alls.loc[alls["Quality_Total"], alls["NQuality_Total"]]]
# alls.loc["Totals_Percent"] = [Quality_Total, NQuality_Total]

print(alls)

# The average of students with quality grades over the years is 24.54% while
# the average of students with non-quality grades was 75.46%

# plt.pie(alls["Quality_Total"], alls["NQuality_Total"])
# plt.title("Comparison of Quality and Non-Quality Grades")
# plt.show()




