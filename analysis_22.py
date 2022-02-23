import pandas as pd
import matplotlib.pyplot as plt

ress_2 = pd.read_csv("KCSE_2016_2.csv", header=0, sep=",", skipinitialspace=True)

alls_2 = pd.read_csv("alls_2.csv", header=0, sep=",")
fems_2 = pd.read_csv("fems_2.csv", header=0, sep=",")
quals_2 = pd.read_csv("UniQual_2.csv", header=0, sep=",")

# print(ress_2)
# print(ress_2.info())
# print(ress_2.describe())


ress_2[["Gender", "Year"]] = ress_2["Gender"].str.split("(", expand=True)
ress_2[["Year", "Noo"]] = ress_2["Year"].str.split(")", expand=True)

ress_2 = ress_2.drop(columns=["Noo"])

cols_pos = list(ress_2.columns)
ress_2 = ress_2[[cols_pos[0]] + [cols_pos[-1]] + cols_pos[1:15]]

ress_2 = ress_2.loc[:, ~ress_2.columns.duplicated()]

ress_2["Total"] = ress_2.iloc[:, 2:].sum(axis=1)

ress_2 = ress_2.sort_values(["Year", "Gender"], ascending=[1, 0])
ress_2["Gender"].str.strip()
# print(ress_2)

ress_m2 = ress_2.loc[ress_2["Gender"] == "MALE"]
# print(ress_m2)
# ress_m2.to_csv("males_2.csv")

ress_f2 = ress_2.loc[ress_2["Gender"] == "FEMALE"]
# print(ress_f2)
# ress_f2.to_csv("fems_2.csv")


ress_a2 = ress_2.loc[ress_2["Gender"] == "ALL"]
# print(ress_a2)
# ress_a2.to_csv("alls_2.csv")


# Separating Quality Grades
cols_pos2 = list(ress_2.columns)
ress_q_2 = ress_2[cols_pos2[0:8]]
# print(ress_2[cols_pos2[0:8]])  // Same as the one below
# print(ress_q_2)
# ress_q_2.to_csv("UniQual_2.csv")

# Did not qualify to join university
cols_pos3 = list(ress_2.columns)
ress_nq_2 = ress_2[cols_pos[0:1] + [cols_pos[-1]] + cols_pos3[8:14]]
# print(ress_nq_2)
# ress_nq_2.to_csv("UniDNQ_2.csv")

fems_2.drop(fems_2.columns[fems_2.columns.str.contains("unnamed", case=False)], axis=1, inplace=True)
# print(fems_2)


# Comparing the total number of candidates over the Years

# print(alls_2)

# cols_t = alls_2.columns
# fig_t, ax_t = plt.subplots()

# plt.xlabel("Year")
# plt.ylabel("No. of Candidates")
# plt.title("Total Number of Candidates over the Years")
# ax_t.bar(alls_2[cols_t[2]], alls_2[cols_t[15]])
# plt.show()

alls_2.drop(alls_2.columns[alls_2.columns.str.contains('unnamed', case=False)], axis=1, inplace=True)
alls_2.set_index("Year", drop=True, inplace=True)

# Line graph showing the total number of candidates over the years

# print(alls_2["Total"])
# alls_2["Total"].plot(kind="line")
# plt.ylabel("No. of Candidates")
# plt.title("Total Number of Candidates over the years")
# plt.show()

# Grade Distribution of Candidates over the years

# alls_2 = alls_2.drop(columns="Total")
# alls_2 = alls_2.drop(columns=["0"])
# print(alls_2)

# alls_2_bar = alls_2.plot.bar()
# plt.xlabel("Year")
# plt.ylabel("No. of Candidates")
# plt.title("Grade Distribution of Candidates")
# plt.show()


# How does the performance between men and won=men compare?

# Grade performance in males

males_results = ress_2[ress_2.Gender.str.startswith("MALE")].drop(columns=["Gender", "Total"]).set_index("Year")
# print(males_results)
# plt.figure(figsize=(12, 4))
# plt.subplot(1, 2, 1)
# plt.xlabel("Years")
# plt.ylabel("Number of Male Candidates")
# plt.legend(males_results.columns)
# plt.title("Grade Performance in Males ")
# plt.plot(males_results)
# plt.show()

# Grade performance in females
females_results = ress_2[ress_2.Gender.str.startswith("FEMALE")].drop(columns=["Gender", "Total"]).set_index("Year")
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

# plt.subplot(1, 1, 1)
# plt.title("Mean of Each Grade Over the Years")
# males_mean.plot()
# females_mean.plot()
# plt.legend(["Male", "Female"])
# plt.show()

# This shows that the most common grade between both genders over the years is D


# How do quality grades compare to non-quality grades?

alls_2["Quality_Sum"] = alls_2["A"] + alls_2["A-"] + alls_2["B+"] + alls_2["B"] + alls_2["B-"] + alls_2["C+"]
alls_2["NQuality_Sum"] = alls_2["C"] + alls_2["C-"] + alls_2["D+"] + alls_2["D"] + alls_2["D-"] + alls_2["E"]

alls_2["Quality_Difference"] = alls_2["NQuality_Sum"] - alls_2["Quality_Sum"]
alls_2["Quality_Percentage"] = (alls_2["Quality_Sum"] / alls_2["Total"]) * 100
alls_2["NQuality_Percentage"] = (alls_2["NQuality_Sum"] / alls_2["Total"]) * 100
alls_2["Quality_Percentage_Difference"] = alls_2["NQuality_Percentage"] - alls_2["Quality_Percentage"]
print(alls_2)

# Pie graph showing the difference between quality grades and non-quality grades
# In 2011, there was the least gap between quality grades and non-quality grades

print(alls_2["Quality_Percentage_Difference"].idxmin())

# In 2016, there was the largest gap between quality grades and non-quality grades
print(alls_2["Quality_Percentage_Difference"].idxmax())

quals_2.drop(quals_2.columns[quals_2.columns.str.contains("unnamed", case=False)], axis=1, inplace=True)
# quals_2["Total_Sum"] = quals_2.iloc[:, 2:8].sum(axis=1)
# print(quals_2)

# Has the gap in difference increased or decreased?


# cols_alls2 = list(alls_2.columns)
# quality_comparison = alls_2[cols_alls2[-3] + [cols_alls2[-1]] + alls_2[cols_alls2[-2]]]
# print(quality_comparison)


alls_2["Quality_Total"] = (alls_2.sum(axis=0).loc["Quality_Sum"] / alls_2.sum(axis=0).loc["Total"]) * 100
alls_2["NQuality_Total"] = (alls_2.sum(axis=0).loc["NQuality_Sum"] / alls_2.sum(axis=0).loc["Total"]) * 100

print(alls_2)

# The average of students with quality grades over the years is 25.91% while
# the average of students with non-quality grades was 74.09%

# NB: Comparison gives incorrect data - Says NQuality percent = 69.52%

# plt.pie(alls_2["Quality_Total"], alls_2["NQuality_Total"])
# plt.title("Comparison of Quality and Non-Quality Grades")
# plt.show()
