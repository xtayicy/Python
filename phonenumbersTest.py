import phonenumbers
from phonenumbers import geocoder,carrier

phone = "+8618301307050";

number = phonenumbers.parse(phone)
print(number)
print(number.country_code)
print(number.national_number)

print(carrier.name_for_number(number, "us"));
print(geocoder.description_for_number(number, "us"));

m = phonenumbers.PhoneNumberMatcher("欢迎致电+8618301307050","CN");
numbers = list(m);
for x in numbers:
    print(x.raw_string);