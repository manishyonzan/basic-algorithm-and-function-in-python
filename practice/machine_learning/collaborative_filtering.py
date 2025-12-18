data_movies = [
    {"product_name":"p1","feature_1":0.2, "feature_2":0.1, "feature_3":0.01, "feature_4":0.9},
    # {"product_name":"p2","feature_1":0.3, "feature_2":0.33, "feature_3":0.32, "feature_4":0.2},
    # {"product_name":"p3","feature_1":0.21, "feature_2":0.33, "feature_3":0.67, "feature_4":0.2},
    # {"product_name":"p4","feature_1":0.54, "feature_2":0.54, "feature_3":0.2, "feature_4":0.3},
    # {"product_name":"p5","feature_1":0.32, "feature_2":0.43, "feature_3":0.3, "feature_4":0.4},
    # {"product_name":"p6","feature_1":0.21, "feature_2":0.12, "feature_3":0.3, "feature_4":0.5},
    {"product_name":"p7","feature_1":0.43, "feature_2":0.22, "feature_3":0.03, "feature_4":0.5},
               ]


def find_difference_value(original_product_feature_array, target_product_feature_array):
    if len(target_product_feature_array) != len(target_product_feature_array):
        return False
    difference_value = 0
    for i in range(len(target_product_feature_array)):
        temp = (target_product_feature_array[i] - original_product_feature_array[i])**2
        difference_value += temp
    return difference_value

# for each in data_movies:
#     for a in each:
#         print(a)


def find_similar_product(total_data, target_product):
    
    for each in total_data:
        if each["product_name"] == target_product["product_name"]:
            continue
        
        
find_similar_product(data_movies, data_movies[0])
    