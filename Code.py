# Load Input file
input_file = open(r".\Timestamps.txt", "r")

# Create if not exists, clear and then write
output_file = open(r".\Timestamps.pbf", "a+")
output_file.close() 
output_file = open(r".\Timestamps.pbf", "r+")

# Write to file
full_line = []
count = 0
lines = input_file.readlines()

output_file.write("[Bookmark]" + '\n')

for line in lines:
    split_lines = line.split('-', 2)
    
    # Get the time and convert to miliseconds
    time_part = split_lines[0].split(':')
    timestring = ((int(time_part[0]) * 3600) + (int(time_part[1]) * 60) + (int(time_part[2]))) * 1000
    
    # Get the file names
    name_part = split_lines[1]
    
    # Construct the line string
    full_line = str(count) + "=" + str(timestring) + "*" + name_part.rstrip().lstrip() + "*" + '\n'
    output_file.write(full_line)
    
    count = count + 1



input_file.close()
output_file.close()
