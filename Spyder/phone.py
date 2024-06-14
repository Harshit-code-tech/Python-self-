import phonenumbers
from test import numbers
from phonenumbers import geocoder
ch_nmber=phonenumbers.parse(number,"CH")
print(geocoder.description_of_number(ch_nmber,"en"))