def cph(total, farms_per_parishes):
    county = 1
    parish = 1
    holding = 1    
        
    farms_per_parish =  total // farms_per_parishes
    farms_in_parish = 0

    for count in range(total):
        yield county, parish, holding        
        
        holding+=1
        farms_in_parish+=1
        if farms_in_parish>farms_per_parishes:
            parish=1
            county+=1
            holding=1
            farms_in_parish=0

def main():
    print("Running")
    for county,parish,holding in cph(30,3):
        print("County:", county)
        print("Parish:", str(parish).zfill(3))
        print("Holding:", str(holding).zfill(5))

if __name__ == '__main__':
    main()