import csv

with open("Python_Excel.csv", 'w') as csvFile:
    fieldnames = ['First_Name', 'Last_Name', 'Rank']
    writer = csv.DictWriter(csvFile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'Rank':'B', 'First_Name':'Parker', 'Last_Name': 'Brian'})
    writer.writerow({'Rank':'A', 'First_Name':'Smith', 'Last_Name': 'Rodriguez'})
    writer.writerow({'Rank':'C', 'First_Name':'Jane', 'Last_Name': 'Loive'})
    writer.writerow({'Rank':'B', 'First_Name':'Samak', 'Last_Name': 'Wardak'})
    print("Writing completed!")
    