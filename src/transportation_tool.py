
# required fields for 1
region = ['US', 'UK', 'Other']
mode_of_transport = ['Road', 'Rail', 'Water', 'Aircraft', 'Offroad']
scope = [1,2,3]
type_of_activity = [
    'Fuel Use','Fuel Use and Vehicle Distance', 
    'Vehicle Distance (e.g. Road Transport)', 
    'Custom fuel', 
    'Custom vehicle']


# required fields for 2
fuel_type = [
    "Petrol (100% mineral petrol) (Motor Gasoline)",
    "Diesel (100% mineral diesel)",
    "Hybrid",
    "Compressed Natural Gas (CNG)",
    "Liquefied Petroleum Gases (LPG)"
]



units_of_measure = ['miles','kilometer']


fuel_used = [
    'Sub Bitumious Coal', 
    'Jet Kerosene', 
    'Aviation Gasoline', 
    'Motor Gaoline/Petrol', 
    'On-Road Diesel Fuel', 
    'Recidual Fuel',
    'Liquefied Petrolium Gases (LPG)',
    'Compressed Natural Gas (CNG)'
    ]

unit_of_fuel_amount = [
    'US Gallon', 
    'UK Gallon', 
    'Litre', 
    'Barrel', 
    'Standard Cubic Foot', 
    ' Cubic Foot', 
    'Cubic Meter'
    ]


# required fields for 3
fossil_fuel_output = "NA" # in metric tons of CO2e
ch4_output = "NA" # in kilograms of ch4
n2o_output = "NA" # in kilograms of n2o
total_ghg_emissions_excluding_biofuel_co2 = "NA" # in metric tons of CO2e
biofuel_co2_emissions = "NA" # in metric tons of CO2e


# required fields for 4 - applied emission factors
applied_co2_emission_factor = "NA" # in kilograms of CO2e per litre
applied_ch4_emission_factor = "NA" # in grams of ch4 per kilometer
applied_n2o_emission_factor = "NA" # in grams of n2o per kilometer
applied_biofuel_co2_emission_factor = "NA" # in ???




## Suboptimal first suggestion 
fuel_economy_data = {
    "Petrol (100% mineral petrol) (Motor Gasoline)": {
        "Passenger Car": {
            # engine size
            "Small car, <1.4 litre": {"mpg": 39.1, "km/L": 16.6},
            "Medium car, 1.4 - 2.0 litres": {"mpg": 30.9, "km/L": 13.1},
            "Large car, >2.0 litres": {"mpg": 20.2, "km/L": 8.6},
            "Average car": {"mpg": 33.6, "km/L": 14.3},
        },
        "Vans": {
            # weight
            "Class I, ≤1.305 tonnes": {"mpg": 30.2, "km/L": 12.8},
            "Class II, >1.305 to ≤1.74 tonnes": {"mpg": 28.1, "km/L": 11.9},
            "Class III, >1.74 to ≤3.5 tonnes": {"mpg": 17.5, "km/L": 7.4},
            "Average (up to 3.5 tonnes)": {"mpg": 27.3, "km/L": 11.6},
        },
        "Motorbike": {
            # engine size
            "Small, ≤125 cc": {"mpg": 67.7, "km/L": 28.8},
            "Medium, >125 and ≤500 cc": {"mpg": 55.8, "km/L": 23.7},
            "Large, >500 cc": {"mpg": 41.9, "km/L": 17.8},
            "Average": {"mpg": 49.2, "km/L": 20.9},
        }
    },
    "Diesel (100% mineral diesel)": {
        "Passenger Car": {
            # engine size
            "Small car, <1.7 litre": {"mpg": 44.9, "km/L": 19.1},
            "Medium car, 1.7 - 2.0 litres": {"mpg": 37.3, "km/L": 15.9},
            "Large car, >2.0 litres": {"mpg": 29.9, "km/L": 12.7},
            "Average car": {"mpg": 36.7, "km/L": 15.6},
        },
        "Vans": {
            # weight
            "Average (up to 3.5 tonnes)": {"mpg": 26.9, "km/L": 11.4},
        },
        "HGV": {
            # weight -> laden = (loaded??)
            "Rigid - 3.5 - 7.5 tonnes - 0% Weight Laden": {"mpg": 13.8, "km/L": 5.9},
            "Rigid - 3.5 - 7.5 tonnes - 50% Weight Laden": {"mpg": 12.7, "km/L": 5.4},
            "Rigid - 3.5 - 7.5 tonnes - 100% Weight Laden": {"mpg": 11.8, "km/L": 5.0},
            "Rigid - 3.5 - 7.5 tonnes - Average Laden": {"mpg": 12.9, "km/L": 5.5},
            "Rigid - 7.5 - 17 tonnes - 0% Weight Laden": {"mpg": 11.6, "km/L": 4.9},
            "Rigid - 7.5 - 17 tonnes - 50% Weight Laden": {"mpg": 10.1, "km/L": 4.3},
            "Rigid - 7.5 - 17 tonnes - 100% Weight Laden": {"mpg": 9.0, "km/L": 3.8},
            "Rigid - 7.5 - 17 tonnes - Average Laden": {"mpg": 10.5, "km/L": 4.5},
            "Rigid - >17 tonnes - 0% Weight Laden": {"mpg": 8.4, "km/L": 3.6},
            "Rigid - >17 tonnes - 50% Weight Laden": {"mpg": 6.9, "km/L": 2.9},
            "Rigid - >17 tonnes - 100% Weight Laden": {"mpg": 5.8, "km/L": 2.5},
            "Rigid - >17 tonnes - Average Laden": {"mpg": 6.4, "km/L": 2.7},
            "Rigid - Average - Average Laden": {"mpg": 7.6, "km/L": 3.2},
            "Articulated - 3.5 - 33 tonnes - 0% Weight Laden": {"mpg": 10.2, "km/L": 4.4},
            "Articulated - 3.5 - 33 tonnes - 50% Weight Laden": {"mpg": 8.2, "km/L": 3.5},
            "Articulated - 3.5 - 33 tonnes - 100% Weight Laden": {"mpg": 6.8, "km/L": 2.9},
            "Articulated - 3.5 - 33 tonnes - Average Laden": {"mpg": 8.2, "km/L": 3.5},
            "Articulated - >33 tonnes - 0% Weight Laden": {"mpg": 10.0, "km/L": 4.2},
            "Articulated - >33 tonnes - 50% Weight Laden": {"mpg": 7.5, "km/L": 3.2},
            "Articulated - >33 tonnes - 100% Weight Laden": {"mpg": 6.0, "km/L": 2.5},
            "Articulated - >33 tonnes - Average Laden": {"mpg": 6.9, "km/L": 2.9},
            "Articulated - Average - Average Laden": {"mpg": 6.9, "km/L": 2.9},
            "Type Unknown - Average - Average Laden": {"mpg": 7.2, "km/L": 3.1},
        }
    },
    "Hybrid": {
        "Passenger Car": {
            # engine size
            "Small car, <1.4 litre": {"mpg": 54.6, "km/L": 23.2},
            "Medium car, 1.4 - 2.0 litres": {"mpg": 50.8, "km/L": 21.6},
            "Large car, >2.0 litres": {"mpg": 36.3, "km/L": 15.4},
            "Average car": {"mpg": 46.5, "km/L": 19.8}
            }
    },
    "Compressed Natural Gas (CNG)": {
        "Passenger Car": {
            # engine size
            "Medium car, 1.4 - 2.0 litres": {"mpg": 38.4, "km/L": 16.3},
            "Large car, >2.0 litres": {"mpg": 25.1, "km/L": 10.7},
            "Average car": {"mpg": 34.3, "km/L": 14.6}
            },
        "Vans":{
            # weight
            "Average (up to 3.5 tonnes)": {"mpg": 25.7, "km/L": 10.9}
            }
    },
    "Liquefied Petroleum Gases (LPG)": {
        "Passenger Car": {
            # engine size
            "Medium car, 1.4 - 2.0 litres": {"mpg": 42.3, "km/L": 18.0},
            "Large car, >2.0 litres": {"mpg": 27.7, "km/L": 11.8},
            "Average car": {"mpg": 37.8, "km/L": 16.1}
        },
        "Vans":{
            # weight
            "Average (up to 3.5 tonnes)": {"mpg": 29.2, "km/L": 12.4}
        }
    }
}


