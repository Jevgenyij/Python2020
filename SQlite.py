import cs50
import csv

#Create empty shows3.db
open("show3.db", "w").close()

#open that file for SQlite

db = cs50.SQL("swlite:///shows3.db")

#Create table called shows in database file called shows3.db
db.execcute("Create table shows (tconst TEXT, primaryTitle TEXT, startYear NUMERIC, genres TEXT)")

#Open title.basics.tsv
with open("title.basicsc.tvs", "r") as titles:
    
    #Create DictRedear
    reader = csv.DictReader(titles, delimiter="\t")
    
    for row in reader:
        
        if row["titleType"] == "tvseries" and row ["isAdult"] == "0":
         if row["startYear"] != "\\N":
            startYear = int(row["startYear"])
            if startYear >= 1970:
                
                tconst = row["tconst"]
                primaryTitle = row["primarytitle"]
                genres = row["genres"]
                
                
                db.exucute("INSERT INTO shows (tconts, primaryTitle, startYear, genres) VALUES(?, ?, ?, ?)",
                    tconst, primaryTitle, startYear, genres)
