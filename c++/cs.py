import csv

data = "1. KOSTIOUK, Evgueni, Alzey, Germany; Poland; DOB 13 Jun 1954; nationality Belarus; Gender Male (individual) [RUSSIA-EO14024]. Designated pursuant to sections 1(a)(i) of Executive Order 14024 of April 15, 2021, 'Blocking Property With Respect To Specified Harmful Foreign Activities of the Government of the Russian Federation,' 86 FR 20249, 3 CFR, 2021 Comp., p. 542 (Apr. 15, 2021) (E.O. 14024) for operating or having operated in the technology sector of the Russian Federation economy."

id_name = data.split(",")[0]
id_parts = id_name.split(". ")
id = id_parts[0]
name = id_parts[1]

description = ",".join(data.split(",")[1:]).strip()

output = [[id, name, description]]

with open('output.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['ID', 'NAME', 'DESCRIPTION'])
    writer.writerows(output)

print(f"ID={id}, NAME={name}, DESCRIPTION={description}")
