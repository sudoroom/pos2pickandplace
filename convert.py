import csv
import shutil
STRING_FORMAT = "1,1,1,237.871,103.0732,180,0.5,0,100,,,"

output_rows = []

with open('top.pos') as in_file:
    reader = csv.reader(in_file)
    # remove blank entries
    blank_filter = [[item for item in row if item != ''] for row in reader]
    # Remove pos file header
    rows = blank_filter[5:]

#print rows[0][0].split()

index = 0
for row in rows:
    clean_row = row[0].split()
    
    if len(clean_row) == 7:
        PosX = abs(float(clean_row[3]))
        PosY = abs(float(clean_row[4]))
        Rot = 90.0+abs(float(clean_row[5]))

        output_rows.append(str(index)+",1,1,"+str(PosX)+","+str(PosY)+","+str(Rot)+",0.5,0,100,,,")

        index += 1

#print output_rows

shutil.copyfile('blank_feeds.csv', 'test_output1.csv')
with open("test_output1.csv", "a") as output:
    for out in output_rows:
        unicode_trash = out+"\n" #.encode('iso-8859-1')
        output.write(unicode_trash)


# No negatives!
# Plus 90degrees?

# Increment, 1?, 1/3?, PosX, PosY, Rot(90+deg), 0.5?, 0?, 100?
# 1,1,1,237.871,103.0732,180,0.5,0,100,,,
