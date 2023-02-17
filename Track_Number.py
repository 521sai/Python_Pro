import phonenumbers
from phonenumbers import carrier , geocoder, timezone

mobileno = input("Enter Mobile Number with Country Code: ")
mobileno = phonenumbers.parse(mobileno)

print(timezone.time_zones_for_number(mobileno))

print(carrier.name_for_number(mobileno,'en'))

print(geocoder.description_for_number(mobileno,'en'))

print("valid Mobile NumberL", phonenumbers.is_valid_number(mobileno))

print("Checking possibility of Number:",phonenumbers.is_possible_number(mobileno))