import csv
import sys
import shutil
import sys, getopt

# String Format:
# Increment, 1?, 1/3?, PosX, PosY, Rot(90+deg), 0.5?, 0?, 100?
# 1,1,1,237.871,103.0732,180,0.5,0,100,,,

# Should be no need to modify FEED_FILE_NAME, unless you have a different
# pick and place. The program appends new feeds to the end of this file,
# because weird unicode stuff is happening
FEED_FILE_NAME = 'blank_feeds.csv'
KICAD_POS_FILE = 'big_battery-top.pos'
BOARD_OUTPUT_FILE = 'pick_and_place_output6.csv'

args = []

# Get file names from args
try:
    opts, args = getopt.getopt(args,"hi:o:",["ifile=","ofile="])
except getopt.GetoptError:
    print 'pos2pickandplace.py -p <kicadposfile> -o <outputfile>'
    sys.exit(2)

for opt, arg in opts:
    if opt == '-h':
        print 'test.py -i <inputfile> -o <outputfile>'
        sys.exit()
    elif opt in ("-p", "--pos"):
        KICAD_POS_FILE = arg
    elif opt in ("-o", "--out"):
        BOARD_OUTPUT_FILE = arg

output_rows = []

offsetX = 0.0 # X offset
offsetY = 45.0 # Board Height + Y offset

# Specify X offsets for multiple boards
# [0.0, 75.0] means 2 boards, 1st board is at
# 0.0 origin, 2nd board is 0.0 + 75.0mm in x direction
x_offs = [0.0, 75.0]

# Specify Spools number by Part Name
spools = {'C_0603_1608Metric_Pad1.05x0.95mm_HandSolder': 2,
          'D_0603_1608Metric_Castellated': 9,
          'LED_0603_1608Metric_Pad1.05x0.95mm_HandSolder': 1,
          'L_0603_1608Metric_Pad1.05x0.95mm_HandSolder': 1,
          'R_0603_1608Metric_Pad1.05x0.95mm_HandSolder': 1}

with open(KICAD_POS_FILE) as in_file:
    reader = csv.reader(in_file)
    # remove blank entries
    blank_filter = [[item for item in row if item != ''] for row in reader]
    # Remove pos file header and footer
    rows = blank_filter[5:-1]

# TODO: - Warn if negative pos or angle
#       - Add comments and vals to csv
for offs in x_offs:
    Index = 0
    for row in rows:
        clean_row = row[0].split()

        # Only deal with the important rows
        try:
            Package = clean_row[2]
            PosX = (float(clean_row[3]))+offs
            PosY = (float(clean_row[4]))
            Rot = 90+(int(float(clean_row[5])))

            
            output_rows.append(str(Index)+",1,"+str(spools[Package])+","+str(PosX+offsetX)+","+str(PosY+offsetY)+","+str(Rot)+",0.5,0,100,,,")
        except:
            pass #print "CANNOT PARSE: ", clean_row

        Index += 1
        
shutil.copyfile(FEED_FILE_NAME, BOARD_OUTPUT_FILE)
with open(BOARD_OUTPUT_FILE, "a") as output:
    for out in output_rows:
        # encode into iso format that the pick and place likes
        unicode_trash = out+"\r\n"
        output.write(unicode_trash)


