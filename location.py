location=[("New york",(40.7128,74.0060)),("Tokyo",(35.6895,139.6917)),("Paris",(48.8566,2.3522))]

def get_location(city):
    for for_name,coordinates in location:
        if for_name==city:
            return coordinates
    return None

city=input("Enter a city: ")
print(get_location(city))

if cordiantes:=get_location(city):
    print(cordiantes)
else:
    print("City not found")
