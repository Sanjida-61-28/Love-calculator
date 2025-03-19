import phonenumbers
from phonenumbers import geocoder
phone_number1 = phonenumbers.parse('+8801715076317') 
phone_number2 = phonenumbers.parse('+8801884067651')
print("\n Phone Numbers Location\n") 
print(geocoder.description_for_number(phone_number1,"en"));
print(geocoder.description_for_number(phone_number2,"en"));