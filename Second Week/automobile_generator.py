import automobile

def main():
    #Create Automobile Object
    auto_1 = automobile.Automobile("Ford","Focus","1234", 2.2, "Alice", 2013)
    auto_2 = automobile.Automobile("Honda", 'Accord', '23456', 3.0, "Bob", 2017)
    
    print(f"{auto_1.make} {auto_1.model}: {auto_1.year}")
    
main()