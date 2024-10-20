# Open a file as read-only and bind it to file
with open('/home/jorge/Projects/DataCamp/data-engineer-in-python/04-introduction-to-importig-data-in-python/files/moby_dick.txt', 'r') as file:
  	# Print it
    print(file.read())