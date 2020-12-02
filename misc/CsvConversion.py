import csv

with open('report.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    with open('/home/vignesh/Documents/reltio/projects/hyperion/match-report/latest/part-00000-1256da96-41d3-4f77-960f'
              '-b9839dd017f9-c000.csv', 'rt') as f:
        csv_reader = csv.reader(f, quotechar="\"", escapechar='\\')

        count = 0
        for line in csv_reader:
            count += 1
            if "Automatic" in line[4]:
                if line[10] != line[23]:
                    writer.writerow(line)
