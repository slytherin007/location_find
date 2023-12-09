import phonenumbers
from test import number
from phonenumbers import carrier
from phonenumbers import geocoder

ch_number=phonenumbers.parse(number,"CH")
service_provider=phonenumbers.parse(number,"RO")

print("The location of number is: ",geocoder.description_for_number(ch_number,"en"))

print("The service provider: ",carrier.name_for_number(service_provider,"en"))