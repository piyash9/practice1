import pickle

cars = ["bmw", "suzuki", "kbjewkd", "bcrewcjube", "kijweibc", "bcec"]
file  = "mycar.pkl"
file_obj = open(file, 'wb')
pickle.dump(cars, file_obj)
file_obj.close()

new_obj = open(file, 'rb')
mycars = pickle.load(new_obj)
print(mycars)