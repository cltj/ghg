import os
import pandas as pd

# first version of the vehicle distance emission factors
# def create_vehicle_distance_emission_factors_df():
#     data = [
#         [1, "Passenger Car", "Small car", "<1.4 litre - Petrol (100% mineral petrol) (Motor Gasoline)", "0.14 ", "0.0128 ", "0.00121 ", "Null"],
#         [2, "Passenger Car", "Medium car", "1.4 - 2.0 litres - Petrol (100% mineral petrol) (Motor Gasoline)", "0.178 ", "0.0128 ", "0.00121 ", "Null"],
#         [3, "Passenger Car", "Large car", ">2.0 litres - Petrol (100% mineral petrol) (Motor Gasoline)", "0.272 ", "0.0128 ", "0.00121 ", "Null"],
#         [4, "Passenger Car", "Average car", "Petrol (100% mineral petrol) (Motor Gasoline)", "0.163 ", "0.0128 ", "0.00121 ", "Fallback petrol cars"],
#         [5, "Passenger Car", "Small car", "<1.7 litre - Diesel (100% mineral diesel)", "0.138 ", "0.000166 ", "0.00631 ", "Null"],
#         [6, "Passenger Car", "Medium car", "1.7 - 2.0 litres - Diesel (100% mineral diesel)", "0.165 ", "0.000166 ", "0.00631 ", "Null"],
#         [7, "Passenger Car", "Large car", ">2.0 litres - Diesel (100% mineral diesel)", "0.207 ", "0.000166 ", "0.00631 ", "Null"],
#         [8, "Passenger Car", "Average car", "Diesel (100% mineral diesel)", "0.168 ", "0.000166 ", "0.00631 ", "Fallback diesel cars"],
#         [9, "Passenger Car", "Small car", "<1.4 litre - Hybrid", "0.1 ", "0.0084 ", "0.00292 ", "Null"],
#         [10, "Passenger Car", "Medium car", "1.4 - 2.0 litres - Hybrid", "0.108 ", "0.006 ", "0.00393 ", "Null"],
#         [11, "Passenger Car", "Large car", ">2.0 litres - Hybrid", "0.151 ", "0.0036 ", "0.005 ", "Null"],
#         [12, "Passenger Car", "Average car", "Hybrid", "0.118 ", "0.0068 ", "0.00369 ", "Fallback hybrid cars"],
#         [13, "Passenger Car", "Medium car", "1.4 - 2.0 litres - Compressed Natural Gas (CNG)", "0.154 ", "0.0632 ", "0.00138 ", "Null"],
#         [14, "Passenger Car", "Large car", ">2.0 litres - Compressed Natural Gas (CNG)", "0.236 ", "0.0632 ", "0.00138 ", "Null"],
#         [15, "Passenger Car", "Average car", "Compressed Natural Gas (CNG)", "0.173 ", "0.0632 ", "0.00138 ", "Fallback CNG cars"],
#         [16, "Passenger Car", "Medium car", "1.4 - 2.0 litres - Liquefied Petroleum Gases (LPG)", "0.176 ", "0.002 ", "0.00138 ", "Null"],
#         [17, "Passenger Car", "Large car", ">2.0 litres - Liquefied Petroleum Gases (LPG)", "0.269 ", "0.002 ", "0.00138 ", "Null"],
#         [18, "Passenger Car", "Average car", "Liquefied Petroleum Gases (LPG)", "0.197 ", "0.002 ", "0.00138 ", "Fallback LPG cars"],
#         [19, "Vans", "Class I", "≤1.305 tonnes", "Petrol (100% mineral petrol) (Motor Gasoline)", "0.181 ", "0.0096 ", "0.00164 ", "Null"],
#         [20, "Vans", "Class II", ">1.305 to ≤1.74 tonnes", "Petrol (100% mineral petrol) (Motor Gasoline)", "0.195 ", "0.0096 ", "0.00164 ", "Null"],
#         [21, "Vans", "Class III", ">1.74 to ≤3.5 tonnes", "Petrol (100% mineral petrol) (Motor Gasoline)", "0.314 ", "0.0096 ", "0.00164 ", "Null"],
#         [22, "Vans", "Average", "up to 3.5 tonnes", "Petrol (100% mineral petrol) (Motor Gasoline)", "0.201 ", "0.0096 ", "0.00164 ", "Fallback petrol vans"],
#         [23, "Vans", "Average", "up to 3.5 tonnes", "Diesel (100% mineral diesel)", "0.23 ", "0 ", "0.00624 ", "Fallback diesel vans"],
#         [24, "Vans", "Average", "up to 3.5 tonnes", "Liquefied Petroleum Gases (LPG)", "0.255 ", "0.0016 ", "0.00188 ", "Fallback LPG vans"],
#         [25, "Vans", "Average", "up to 3.5 tonnes", "Compressed Natural Gas (CNG)", "0.23 ", "0.0472 ", "0.00188 ", "Fallback CNG vans"],
#         [26, "Motorbike", "Small", "≤125 cc", "Petrol (100% mineral petrol) (Motor Gasoline)", "0.0809 ", "0.0624 ", "0.00188 ", "Null"],
#         [27, "Motorbike", "Medium", ">125 to ≤500 cc", "Petrol (100% mineral petrol) (Motor Gasoline)", "0.0983 ", "0.0816 ", "0.00201 ", "Null"],
#         [28, "Motorbike", "Large", ">500 cc", "Petrol (100% mineral petrol) (Motor Gasoline)", "0.131 ", "0.0452 ", "0.00201 ", "Null"],
#         [29, "Motorbike", "Average", "Petrol (100% mineral petrol) (Motor Gasoline)", "0.111 ", "0.0632 ", "0.00198 ", "Fallback petrol motorbikes"],
#         [30, "HGV", "Rigid", "3.5 - 7.5 tonnes - 0% Weight Laden", "Diesel (100% mineral diesel)", "0.447 ", "0.004 ", "0.0201 ", "Null"],
#         [31, "HGV", "Rigid", "3.5 - 7.5 tonnes - 50% Weight Laden", "Diesel (100% mineral diesel)", "0.486 ", "0.004 ", "0.0201 ", "Null"],
#         [32, "HGV", "Rigid", "3.5 - 7.5 tonnes - 100% Weight Laden", "Diesel (100% mineral diesel)", "0.524 ", "0.004 ", "0.0201 ", "Null"],
#         [33, "HGV", "Rigid", "3.5 - 7.5 tonnes - Average Laden", "Diesel (100% mineral diesel)", "0.48 ", "0.004 ", "0.0201 ", "Fallback HGV rigid 3.5-7.5 tonnes diesel (amount loaded)"],
#         [34, "HGV", "Rigid", "7.5 - 17 tonnes - 0% Weight Laden", "Diesel (100% mineral diesel)", "0.534 ", "0.0048 ", "0.0245 ", "Null"],
#         [35, "HGV", "Rigid", "7.5 - 17 tonnes - 50% Weight Laden", "Diesel (100% mineral diesel)", "0.611 ", "0.0048 ", "0.0245 ", "Null"],
#         [36, "HGV", "Rigid", "7.5 - 17 tonnes - 100% Weight Laden", "Diesel (100% mineral diesel)", "0.687 ", "0.0048 ", "0.0245 ", "Null"],
#         [37, "HGV", "Rigid", "7.5 - 17 tonnes - Average Laden", "Diesel (100% mineral diesel)", "0.586 ", "0.0048 ", "0.0245 ", "Fallback HGV rigid 7.5-17 tonnes diesel (amount loaded)"],
#         [38, "HGV", "Rigid", ">17 tonnes - 0% Weight Laden", "Diesel (100% mineral diesel)", "0.736 ", "0.008 ", "0.04 ", "Null"],
#         [39, "HGV", "Rigid", ">17 tonnes - 50% Weight Laden", "Diesel (100% mineral diesel)", "0.898 ", "0.008 ", "0.04 ", "Null"],
#         [40, "HGV", "Rigid", ">17 tonnes - 100% Weight Laden", "Diesel (100% mineral diesel)", "1.06 ", "0.008 ", "0.04 ", "Null"],
#         [41, "HGV", "Rigid", ">17 tonnes - Average Laden", "Diesel (100% mineral diesel)", "0.964 ", "0.008 ", "0.04 ", "Fallback HGV rigid >17 tonnes diesel (amount loaded)"],
#         [42, "HGV", "Articulated", "3.5 - 33 tonnes - 0% Weight Laden", "Diesel (100% mineral diesel)", "0.603 ", "0.0044 ", "0.0456 ", "Null"],
#         [43, "HGV", "Articulated", "3.5 - 33 tonnes - 50% Weight Laden", "Diesel (100% mineral diesel)", "0.754 ", "0.0044 ", "0.0456 ", "Null"],
#         [44, "HGV", "Articulated", "3.5 - 33 tonnes - 100% Weight Laden", "Diesel (100% mineral diesel)", "0.905 ", "0.0044 ", "0.0456 ", "Null"],
#         [45, "HGV", "Articulated", "3.5 - 33 tonnes - Average Laden", "Diesel (100% mineral diesel)", "0.754 ", "0.0044 ", "0.0456 ", "Fallback HGV articulated 3.5-33 tonnes diesel (amount loaded)"],
#         [46, "HGV", "Articulated", ">33 tonnes - 0% Weight Laden", "Diesel (100% mineral diesel)", "0.618 ", "0.0052 ", "0.0543 ", "Null"],
#         [47, "HGV", "Articulated", ">33 tonnes - 50% Weight Laden", "Diesel (100% mineral diesel)", "0.824 ", "0.0052 ", "0.0543 ", "Null"],
#         [48, "HGV", "Articulated", ">33 tonnes - 100% Weight Laden", "Diesel (100% mineral diesel)", "1.03 ", "0.0052 ", "0.0543 ", "Null"],
#         [49, "HGV", "Articulated", ">33 tonnes - Average Laden", "Diesel (100% mineral diesel)", "0.898 ", "0.0052 ", "0.0543 ", "Fallback HGV articulated >33 tonnes diesel (amount loaded)"],
#         [51, "HGV", "Articulated", "Average - Average Laden", "Diesel (100% mineral diesel)", "0.892 ", "0.0052 ", "0.0539 ", "Fallback HGV articulated diesel (weight & amount loaded)"],
#         [52, "HGV", "Type Unknown", "Average - Average Laden", "Diesel (100% mineral diesel)", "0.86 ", "0.0056 ", "0.0451 ", "Fallback HGV diesel (vehicle_type & weight & amount loaded)"]
#     ]

#     header = ["id", "vehicle_class", "vehicle_type", "engine_size_or_weight", "fuel_type", "co2_emission_factor (Kilogram CO2/Kilometer)", "ch4_emission_factor (Gram CH4/Kilometer)", "n2o_emission_factor (Gram N2O/Kilometer)", "comment"]
    
#     df = pd.DataFrame(data, columns=header)
#     return df

# # Create the DataFrame
# vehicle_distance_emission_factors_df = create_vehicle_distance_emission_factors_df()

# Try 2 ===============================


def create_vehicle_distance_emission_factors_df2():
    vehicle_classes = {
        # To make the data to a consistent format I had to split the engine size and fuel type into separate columns
        "Passenger car": [
            ("Small car", "<1.4 litre", "Petrol (100% mineral petrol) (Motor Gasoline)", 0.14, 0.0128, 0.00121, "Null"),
            ("Medium car", "1.4 - 2.0 litres", "Petrol (100% mineral petrol) (Motor Gasoline)", 0.178, 0.0128, 0.00121, "Null"),
            ("Large car", ">2.0 litres", "Petrol (100% mineral petrol) (Motor Gasoline)", 0.272, 0.0128, 0.00121, "Null"),
            ("Average car", "Unknown engine size", "Petrol (100% mineral petrol) (Motor Gasoline)", 0.163, 0.0128, 0.00121, "Fallback petrol cars"), # assuming the missing space was engine size
            ("Small car", "<1.7 litre", "Diesel (100% mineral diesel)", 0.138, 0.000166, 0.00631, "Null"),
            ("Medium car", "1.7 - 2.0 litres", "Diesel (100% mineral diesel)", 0.165, 0.000166, 0.00631, "Null"),
            ("Large car", ">2.0 litres", "Diesel (100% mineral diesel)", 0.207, 0.000166, 0.00631, "Null"),
            ("Average car", "Unknown engine size", "Diesel (100% mineral diesel)", 0.168, 0.000166, 0.00631, "Fallback diesel cars"), # assuming the missing space was engine size
            ("Small car", "<1.4 litre", "Hybrid", 0.1, 0.0084, 0.00292, "Null"),
            ("Medium car", "1.4 - 2.0 litres", "Hybrid", 0.108, 0.006, 0.00393, "Null"),
            ("Large car", ">2.0 litres", "Hybrid", 0.151, 0.0036, 0.005, "Null"),
            ("Average car", "Unknown engine size", "Hybrid",0.118, 0.0068, 0.00369, "Fallback hybrid cars"), # assuming the missing space was engine size
            ("Medium car", "1.4 - 2.0 litres","Compressed Natural Gas (CNG)", 0.154, 0.0632, 0.00138, "Null"),
            ("Large car", ">2.0 litres","Compressed Natural Gas (CNG)", 0.236, 0.0632, 0.00138, "Null"),
            ("Average car", "Unknown engine size","Compressed Natural Gas (CNG)", 0.173, 0.0632, 0.00138, "Fallback CNG cars"), # assuming the missing space was engine size
            ("Medium car", "1.4 - 2.0 litres", "Liquefied Petroleum Gases (LPG)", 0.176, 0.002, 0.00138, "Null"),
            ("Large car", ">2.0 litres", "Liquefied Petroleum Gases (LPG)", 0.269, 0.002, 0.00138, "Null"),
            ("Average car", "Unknown engine size","Liquefied Petroleum Gases (LPG)", 0.197, 0.002, 0.00138, "Fallback LPG cars") # assuming the missing space was engine size
        ],
        "Vans": [
            ("Class I", "≤1.305 tonnes", "Petrol (100% mineral petrol) (Motor Gasoline)", 0.181, 0.0096, 0.00164, "Null"),
            ("Class II", ">1.305 to ≤1.74 tonnes", "Petrol (100% mineral petrol) (Motor Gasoline)", 0.195, 0.0096, 0.00164, "Null"),
            ("Class III", ">1.74 to ≤3.5 tonnes", "Petrol (100% mineral petrol) (Motor Gasoline)", 0.314, 0.0096, 0.00164, "Null"),
            ("Average", "up to 3.5 tonnes", "Petrol (100% mineral petrol) (Motor Gasoline)", 0.201, 0.0096, 0.00164, "Fallback petrol vans"),
            ("Average", "up to 3.5 tonnes", "Diesel (100% mineral diesel)", 0.23, 0, 0.00624, "Fallback diesel vans"),
            ("Average", "up to 3.5 tonnes", "Liquefied Petroleum Gases (LPG)", 0.255, 0.0016, 0.00188, "Fallback LPG vans"),
            ("Average", "up to 3.5 tonnes", "Compressed Natural Gas (CNG)", 0.23, 0.0472, 0.00188, "Fallback CNG vans")
        ],
        "Motorbike": [
            ("Small", "≤125 cc", "Petrol (100% mineral petrol) (Motor Gasoline)", 0.0809, 0.0624, 0.00188, "Null"),
            ("Medium", ">125 to ≤500 cc", "Petrol (100% mineral petrol) (Motor Gasoline)", 0.0983, 0.0816, 0.00201, "Null"),
            ("Large", ">500 cc", "Petrol (100% mineral petrol) (Motor Gasoline)", 0.131, 0.0452, 0.00201, "Null"),
            ("Average", "Unknown engine size", "Petrol (100% mineral petrol) (Motor Gasoline)", 0.111, 0.0632, 0.00198, "Fallback petrol motorbikes")  # assuming the missing space was engine size
        ],
        "HGV": [
            ("Rigid", "3.5 - 7.5 tonnes - 0% Weight Laden", "Diesel (100% mineral diesel)", 0.447, 0.004, 0.0201, "Null"),
            ("Rigid", "3.5 - 7.5 tonnes - 50% Weight Laden", "Diesel (100% mineral diesel)", 0.486, 0.004, 0.0201, "Null"),
            ("Rigid", "3.5 - 7.5 tonnes - 100% Weight Laden", "Diesel (100% mineral diesel)", 0.524, 0.004, 0.0201, "Null"),
            ("Rigid", "3.5 - 7.5 tonnes - Average Laden", "Diesel (100% mineral diesel)", 0.48, 0.004, 0.0201, "Fallback HGV rigid 3.5-7.5 tonnes diesel (amount loaded)"),
            ("Rigid", "7.5 - 17 tonnes - 0% Weight Laden", "Diesel (100% mineral diesel)", 0.534, 0.0048, 0.0245, "Null"),
            ("Rigid", "7.5 - 17 tonnes - 50% Weight Laden", "Diesel (100% mineral diesel)", 0.611, 0.0048, 0.0245, "Null"),
            ("Rigid", "7.5 - 17 tonnes - 100% Weight Laden", "Diesel (100% mineral diesel)", 0.687, 0.0048, 0.0245, "Null"),
            ("Rigid", "7.5 - 17 tonnes - Average Laden", "Diesel (100% mineral diesel)", 0.586, 0.0048, 0.0245, "Fallback HGV rigid 7.5-17 tonnes diesel (amount loaded)"),
            ("Rigid", ">17 tonnes - 0% Weight Laden", "Diesel (100% mineral diesel)", 0.736, 0.008, 0.04, "Null"),
            ("Rigid", ">17 tonnes - 50% Weight Laden", "Diesel (100% mineral diesel)", 0.898, 0.008, 0.04, "Null"),
            ("Rigid", ">17 tonnes - 100% Weight Laden", "Diesel (100% mineral diesel)", 1.06, 0.008, 0.04, "Null"),
            ("Rigid", ">17 tonnes - Average Laden", "Diesel (100% mineral diesel)", 0.964, 0.008, 0.04, "Fallback HGV rigid >17 tonnes diesel (amount loaded)"),
            ("Articulated", "3.5 - 33 tonnes - 0% Weight Laden", "Diesel (100% mineral diesel)", 0.603, 0.0044, 0.0456, "Null"),
            ("Articulated", "3.5 - 33 tonnes - 50% Weight Laden", "Diesel (100% mineral diesel)", 0.754, 0.0044, 0.0456, "Null"),
            ("Articulated", "3.5 - 33 tonnes - 100% Weight Laden", "Diesel (100% mineral diesel)", 0.905, 0.0044, 0.0456, "Null"),
            ("Articulated", "3.5 - 33 tonnes - Average Laden", "Diesel (100% mineral diesel)", 0.754, 0.0044, 0.0456, "Fallback HGV articulated 3.5-33 tonnes diesel (amount loaded)"),
            ("Articulated", ">33 tonnes - 0% Weight Laden", "Diesel (100% mineral diesel)", 0.618, 0.0052, 0.0543, "Null"),
            ("Articulated", ">33 tonnes - 50% Weight Laden", "Diesel (100% mineral diesel)", 0.824, 0.0052, 0.0543, "Null"),
            ("Articulated", ">33 tonnes - 100% Weight Laden", "Diesel (100% mineral diesel)", 1.03, 0.0052, 0.0543, "Null"),
            ("Articulated", ">33 tonnes - Average Laden", "Diesel (100% mineral diesel)", 0.898, 0.0052, 0.0543, "Fallback HGV articulated >33 tonnes diesel (amount loaded)"),
            ("Articulated", "Average - Average Laden", "Diesel (100% mineral diesel)", 0.892, 0.0052, 0.0539, "Fallback HGV articulated diesel (weight & amount loaded)"),
            ("Type Unknown", "Average - Average Laden", "Diesel (100% mineral diesel)", 0.86, 0.0056, 0.0451, "Fallback HGV diesel (vehicle_type & weight & amount loaded)")
        ]
    }

    data = []
    id_counter = 1

    for vehicle_class, details in vehicle_classes.items():
        for detail in details:
            vehicle_type, engine_size_or_weight, fuel_type, co2, ch4, n2o, comment = detail
            data.append([id_counter, vehicle_class, vehicle_type, engine_size_or_weight, fuel_type, co2, ch4, n2o, comment])
            id_counter += 1

    header = ["id", "vehicle_class", "vehicle_type", "engine_size_or_weight", "fuel_type", "co2_emission_factor (Kilogram CO2/Kilometer)", "ch4_emission_factor (Gram CH4/Kilometer)", "n2o_emission_factor (Gram N2O/Kilometer)", "comment"]

    df = pd.DataFrame(data, columns=header)
    return df

# Create the DataFrame
vehicle_distance_emission_factors_df = create_vehicle_distance_emission_factors_df2()

# Define the output path
output_dir = 'src/model_generator/outputs'
output_path = os.path.join(output_dir, 'vehicle_distance_emission_factors2.csv')

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Save the DataFrame to CSV
vehicle_distance_emission_factors_df.to_csv(output_path, index=False)
print(f"CSV file 'vehicle_distance_emission_factors2.csv' created successfully at {output_path}.")


# For reference, this is the content of the transportation tool
# id, vehicle_class, vehicle_type, engine_size_or_weight, fuel_type, co2_emission_factor, ch4_emission_factor, n2o_emission_factor, comment
# 1, Passenger Car, Small car, <1.4 litre - Petrol (100% mineral petrol) (Motor Gasoline), 0.14 , 0.0128 , 0.00121 ,Null
# 2, Passenger Car, Medium car, 1.4 - 2.0 litres - Petrol (100% mineral petrol) (Motor Gasoline), 0.178 , 0.0128 , 0.00121 ,Null
# 3, Passenger Car, Large car, >2.0 litres - Petrol (100% mineral petrol) (Motor Gasoline), 0.272 , 0.0128 , 0.00121 ,Null
# 4, Passenger Car, Average car, Petrol (100% mineral petrol) (Motor Gasoline), 0.163 , 0.0128 , 0.00121 ,Fallback petrol cars
# 5, Passenger Car, Small car, <1.7 litre - Diesel (100% mineral diesel), 0.138 , 0.000166 , 0.00631 ,Null
# 6, Passenger Car, Medium car, 1.7 - 2.0 litres - Diesel (100% mineral diesel), 0.165 , 0.000166 , 0.00631 , Null
# 7, Passenger Car, Large car, >2.0 litres - Diesel (100% mineral diesel), 0.207 , 0.000166 , 0.00631 , Null
# 8, Passenger Car, Average car, Diesel (100% mineral diesel), 0.168 , 0.000166 , 0.00631 ,Fallback diesel cars
# 9, Passenger Car, Small car, <1.4 litre - Hybrid, 0.1 , 0.0084 , 0.00292 , Null
# 10, Passenger Car, Medium car, 1.4 - 2.0 litres - Hybrid, 0.108 , 0.006 , 0.00393 , Null
# 11, Passenger Car, Large car, >2.0 litres - Hybrid, 0.151 , 0.0036 , 0.005 , Null
# 12, Passenger Car, Average car, Hybrid, 0.118 , 0.0068 , 0.00369 , Fallback hybrid cars
# 13, Passenger Car, Medium car, 1.4 - 2.0 litres - Compressed Natural Gas (CNG), 0.154 , 0.0632 , 0.00138 , Null
# 14, Passenger Car, Large car, >2.0 litres - Compressed Natural Gas (CNG), 0.236 , 0.0632 , 0.00138 , Null
# 15, Passenger Car, Average car, Compressed Natural Gas (CNG), 0.173 , 0.0632 , 0.00138 , Fallback CNG cars
# 16, Passenger Car, Medium car, 1.4 - 2.0 litres - Liquefied Petroleum Gases (LPG), 0.176 , 0.002 , 0.00138 , Null
# 17, Passenger Car, Large car, >2.0 litres - Liquefied Petroleum Gases (LPG), 0.269 , 0.002 , 0.00138 , Null
# 18, Passenger Car, Average car, Liquefied Petroleum Gases (LPG), 0.197 , 0.002 , 0.00138 , Fallback LPG cars
# 19,Vans, Class I, ≤1.305 tonnes, Petrol (100% mineral petrol) (Motor Gasoline), 0.181 , 0.0096 , 0.00164 , Null
# 20,Vans, Class II, >1.305 to ≤1.74 tonnes, Petrol (100% mineral petrol) (Motor Gasoline), 0.195 , 0.0096 , 0.00164 , Null
# 21,Vans, Class III, >1.74 to ≤3.5 tonnes, Petrol (100% mineral petrol) (Motor Gasoline), 0.314 , 0.0096 , 0.00164 , Null
# 22,Vans, Average, up to 3.5 tonnes, Petrol (100% mineral petrol) (Motor Gasoline), 0.201 , 0.0096 , 0.00164 , Fallback petrol vans
# 23,Vans, Average, up to 3.5 tonnes, Diesel (100% mineral diesel), 0.23 , 0 , 0.00624 , Fallbak diesel vans
# 24,Vans, Average, up to 3.5 tonnes, Liquefied Petroleum Gases (LPG), 0.255 , 0.0016 , 0.00188 , Fallback LPG vans
# 25,Vans, Average, up to 3.5 tonnes, Compressed Natural Gas (CNG), 0.23 , 0.0472 , 0.00188 , Fallback CNG vans
# 26,Motorbike, Small, ≤125 cc, Petrol (100% mineral petrol) (Motor Gasoline), 0.0809 , 0.0624 , 0.00188 , Null
# 27,Motorbike, Medium, >125 to ≤500 cc, Petrol (100% mineral petrol) (Motor Gasoline), 0.0983 , 0.0816 , 0.00201 , Null
# 28,Motorbike, Large, >500 cc, Petrol (100% mineral petrol) (Motor Gasoline), 0.131 , 0.0452 , 0.00201 , Null
# 29,Motorbike, Average, Petrol (100% mineral petrol) (Motor Gasoline), 0.111 , 0.0632 , 0.00198 , Fallback petrol motorbikes
# 30,HGV, Rigid, 3.5 - 7.5 tonnes - 0% Weight Laden, Diesel (100% mineral diesel), 0.447 , 0.004 , 0.0201 , Null
# 31,HGV, Rigid, 3.5 - 7.5 tonnes - 50% Weight Laden, Diesel (100% mineral diesel), 0.486 , 0.004 , 0.0201 , Null
# 32,HGV, Rigid, 3.5 - 7.5 tonnes - 100% Weight Laden, Diesel (100% mineral diesel), 0.524 , 0.004 , 0.0201 , Null
# 33,HGV, Rigid, 3.5 - 7.5 tonnes - Average Laden, Diesel (100% mineral diesel), 0.48 , 0.004 , 0.0201 , Fallback HGV rigid 3.5-7.5 tonnes diesel (amount loaded)
# 34,HGV, Rigid, 7.5 - 17 tonnes - 0% Weight Laden, Diesel (100% mineral diesel), 0.534 , 0.0048 , 0.0245 , Null
# 35,HGV, Rigid, 7.5 - 17 tonnes - 50% Weight Laden, Diesel (100% mineral diesel), 0.611 , 0.0048 , 0.0245 , Null
# 36,HGV, Rigid, 7.5 - 17 tonnes - 100% Weight Laden, Diesel (100% mineral diesel), 0.687 , 0.0048 , 0.0245 , Null
# 37,HGV, Rigid, 7.5 - 17 tonnes - Average Laden, Diesel (100% mineral diesel), 0.586 , 0.0048 , 0.0245 , Fallback HGV rigid 7.5-17 tonnes diesel (amount loaded)
# 38,HGV, Rigid, >17 tonnes - 0% Weight Laden, Diesel (100% mineral diesel), 0.736 , 0.008 , 0.04 , Null
# 39,HGV, Rigid, >17 tonnes - 50% Weight Laden, Diesel (100% mineral diesel), 0.898 , 0.008 , 0.04 , Null
# 40,HGV, Rigid, >17 tonnes - 100% Weight Laden, Diesel (100% mineral diesel), 1.06 , 0.008 , 0.04 , Null
# 41,HGV, Rigid, >17 tonnes - Average Laden, Diesel (100% mineral diesel), 0.964 , 0.008 , 0.04 , Fallback HGV rigid >17 tonnes diesel (amount loaded)
# 42,HGV, Articulated, 3.5 - 33 tonnes - 0% Weight Laden, Diesel (100% mineral diesel), 0.603 , 0.0044 , 0.0456 , Null
# 43,HGV, Articulated, 3.5 - 33 tonnes - 50% Weight Laden, Diesel (100% mineral diesel), 0.754 , 0.0044 , 0.0456 , Null
# 44,HGV, Articulated, 3.5 - 33 tonnes - 100% Weight Laden, Diesel (100% mineral diesel), 0.905 , 0.0044 , 0.0456 , Null
# 45,HGV, Articulated, 3.5 - 33 tonnes - Average Laden, Diesel (100% mineral diesel), 0.754 , 0.0044 , 0.0456 , Fallback HGV articulated 3.5-33 tonnes diesel (amount loaded)
# 46,HGV, Articulated, >33 tonnes - 0% Weight Laden, Diesel (100% mineral diesel), 0.618 , 0.0052 , 0.0543 , Null
# 47,HGV, Articulated, >33 tonnes - 50% Weight Laden, Diesel (100% mineral diesel), 0.824 , 0.0052 , 0.0543 , Null
# 48,HGV, Articulated, >33 tonnes - 100% Weight Laden, Diesel (100% mineral diesel), 1.03 , 0.0052 , 0.0543 , Null
# 49,HGV, Articulated, >33 tonnes - Average Laden, Diesel (100% mineral diesel), 0.898 , 0.0052 , 0.0543 , Fallback HGV articulated >33 tonnes diesel (amount loaded)
# 51,HGV, Articulated, Average - Average Laden, Diesel (100% mineral diesel), 0.892 , 0.0052 , 0.0539 , Fallback HGV articulated diesel (weight & amount loaded)
# 52,HGV, Type Unknown, Average - Average Laden, Diesel (100% mineral diesel),0.86 , 0.0056 , 0.0451 , Fallback HGV diesel (vehicle_type & weight & amount loaded)
