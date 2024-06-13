def main():
    #create a while loop that prints ints between 0 and 10
    i = 0
    #run the loop while i is less than or equal to 10
    while i <= 10:
        print(i)
        i+=1

    print("\n\n")

    i = 0
    while True:
        print(i)
        i+=1
        if i > 10:
            break


main()