# module to write stuff to csv - output

# create csv from master dictionary and use unique field names from fieldList
def output():
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldList)
        writer.writeheader()
        for k, v in master.items():
            writer.writerow(v)
