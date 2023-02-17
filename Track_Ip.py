import geoip

ip = geoip.getIp()
print(ip)

country = geoip.getCountry(ip,'plain')
print(country)

country = geoip.getCountry(ip,'json')
print(country)

geoData = geoip.getGeoData(ip)
print(geoData)

ptrData = geoip.getPTR(ip)
print(ptrData)

geoip.showIpDetails('216.239.32.0')

geoip.showCountryDetails('216.239.32.0')