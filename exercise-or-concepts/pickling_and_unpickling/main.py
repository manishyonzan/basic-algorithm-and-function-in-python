import pickle

data_to_pickle = [1,"helllo world", {"python":3,"library":"pickle"}]

pickle_file = "data.pkl"

# with open(pickle_file ,"wb") as file:
#     pickle.dump(data_to_pickle,file)
    
# print("Data saved successfully to ", pickle_file)

with open(pickle_file,"rb") as file:
    loaded_data = pickle.load(file)
    
print("data loaded form file",pickle_file)
print("file content",loaded_data)
