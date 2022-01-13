# Load Input file
input_file = open(r".\Timestamps.txt", "r")

# Load Output file
output_file = open(r".\Timestamps.pbf", 'w')

# Initialize
full_line = []
count = 0
output_file.write("[Bookmark]" + '\n')

for line in input_file.readlines():
    split_lines = line.split('-', 2)
    
    # Get the time and convert to miliseconds
    time_part = split_lines[0].split(':')
    
    if(len(time_part)) < 3 :            # 3 == HH:MM:SS
        length = len(time_part)
        for i in range((3 - length)):
            time_part = [0] + time_part
    
    timestring = str(((int(time_part[0]) * 3600) + (int(time_part[1]) * 60) + (int(time_part[2]))) * 1000)
    
    
    # Get the file name
    name_part = split_lines[1].rstrip().lstrip()
    
    
    # Construct the line string
    full_line = str(count) + "=" + str(timestring) + "*" + name_part + "*" + '\n'
    output_file.write(full_line)
    
    count = count + 1

input_file.close()
output_file.close()
