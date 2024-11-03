from model_generator import generate_currencies, generate_fuel_economy_data, generate_fuel_types, generate_mode_of_transport,generate_regions, generate_scope, generate_type_of_activity


def main():
    generate_mode_of_transport()
    generate_fuel_types()
    generate_fuel_economy_data()
    generate_regions()
    generate_currencies()
    generate_scope()
    generate_type_of_activity()
    
if __name__ == "__main__":
    main()



