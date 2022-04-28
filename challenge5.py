#Challenge Problem 5
#Using Pandas Dataframe
#I worked alongside Jake and Josiah

#Imports for Python
import pandas as pd
import os

#opens csv and builds two new csv files.
#if the "build" directory does not already exist, it creates one
def import_csv(filename):
    file = pd.read_csv(filename)
    print(file.to_string())
    institution, team = split(file)
    if not os.path.exists(os.path.abspath("./build/")):
        os.mkdir(os.path.abspath("./build/"))
    institution.to_csv("build/Institutions.csv", index=False)
    team.to_csv("build/Team.csv", index=False)

#Splits the csv to string file by institution attributes and team attributes.
#Dropped the duplicate entries
#Then sorts the institution csv file by insitution id and the team csv file by team number
def split(file):
    for col in file:
        if file.dtypes[col] == object:
            file[f"l_{col}"] = file[col].str.lower()
    file["Institution ID"] = file.groupby(["l_ï»¿Institution", "l_City"]).ngroup()
    institution = file[["Institution ID", "ï»¿Institution", "City", "State/Province", "Country"]]
    institution = institution.drop_duplicates(subset=["Institution ID"])
    team = file[["Team Number", "Institution ID", "Advisor", "Problem", "Ranking"]]
    institution = institution.sort_values(["Institution ID"])
    team = team.sort_values(["Team Number"])
    return institution, team

if __name__ == '__main__':
    import_csv("data/2015.csv")
