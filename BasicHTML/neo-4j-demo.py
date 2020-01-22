import csv

with open("bloom2.csv", 'r') as file:
    reader = csv.DictReader(file,delimiter=',')

    keys = reader.fieldnames

    node = []
    created = []
    i = 0
    for line in reader:
        var1 = "test" + str(i)
        var2 = "temp" + str(i)
        call_type = str(line[keys[4]])
        number1 = line[keys[0]]
        number2 = line[keys[1]]
        status = line[keys[6]]
        start_time = str(line[keys[2]])
        end_time = str(line[keys[3]])
        print("MERGE ("+var1+":"+"mobile_number"+ "{ number: \""+number1+"\"})MERGE("+var2+":"+"mobile_number"+ "{ number:\""+number2+"\"})MERGE("+var1+")-[:"+status+"{typeb:\""+call_type+"\",start_time:\""+start_time+"\",end_time:\""+end_time+"\"}]->("+var2+")")
        i =i+1