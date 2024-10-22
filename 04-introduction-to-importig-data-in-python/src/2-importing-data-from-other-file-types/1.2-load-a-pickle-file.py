# Import pickle package
import pickle

filename = './04-introduction-to-importig-data-in-python/files/data.pkl'
data = {'June': '69.4', 'Aug': '85', 'Airline': '8', 'Mar': '84.4'}
file = open(filename, 'wb')
pickle.dump(data, file)
file.close()

# Open pickle file and load data: d
with open(filename, 'rb') as file:
    d = pickle.load(file)

# Print d
print(d)

# Print datatype of d
print(type(d))