# with is like your try .. finally block in this case
with open("C:/Users/GunagiSa/OneDrive - Unisys/Documents/ssg/repo/REDeploy/RE-Upgrade-Auto/Config/Default.cfg", "r") as file:
    # read a list of lines into data
    data = file.readlines()

# print (data)
print ("Your name: " + data[0])

# now change the 2nd line, note that you have to add a newline
data[1] = '  UseMQSeries           = 1\n\n'

# and write everything back
with open("C:/Users/GunagiSa/OneDrive - Unisys/Documents/ssg/repo/REDeploy/RE-Upgrade-Auto/Config/Default.cfg", "w") as file:
    file.writelines( data )


with open("C:/Users/GunagiSa/OneDrive - Unisys/Documents/ssg/repo/REDeploy/RE-Upgrade-Auto/Config/Default.cfg", "r") as f:
    lines = f.readlines()
with open("C:/Users/GunagiSa/OneDrive - Unisys/Documents/ssg/repo/REDeploy/RE-Upgrade-Auto/Config/Default.cfg", "w") as f:
    for line in lines:
        if line.strip("\n") != "  UseMQSeries           = 0":
            f.write(line)