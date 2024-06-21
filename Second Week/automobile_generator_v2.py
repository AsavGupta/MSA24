import automobile as auto

#Func to load vehicle data from file
#Input: path to the file
#Output: list of automobiles
def load_vehicles(file_name):
        
    #Create empty list to store automobile data
    auto_list = []
    
    #Open the file
    auto_file = open(f'{file_name}', 'r')  
    auto_file.readline()

    #read each line of the file
    line_number = 1 
    
    for auto_line_of_data in auto_file:
        #increment line number
        line_number+=1
                
        #split at the comma
        auto_values = auto_line_of_data.split(',')
        try:
            if len(auto_values) != 6:
                raise Exception(f'\nThere is an error in your data file at {line_number}')
        except Exception as err:
            print(str(err))
            continue
        
        #get values from the list
        try:
            make = auto_values[0]
            model = auto_values[1]
            vin = auto_values[2]
            
            if auto_values[3].lower() == 'electric':
                engine_size = 0
            else:
                engine_size = float(auto_values[3])
                
            owner = auto_values[4]
            year = int(auto_values[5])
        except Exception as err:
            print(f'Error: {err} on line {line_number}')
            continue
        
        #create automobiles from the data
        new_auto = auto.Automobile(make, model, vin, engine_size, owner, year)
        
        #append each automobile to the list of automobiles 
        auto_list.append(new_auto)
     
    #Close and return automobile list   
    auto_file.close()    
    return auto_list   
        
def main():
    auto_list = load_vehicles('vehicle_data.csv')
    
    #print vehicle data
    print('\nVehicle Data\n---------------')
    for auto in auto_list:
        auto.print_info()
        print('-----------')


main()