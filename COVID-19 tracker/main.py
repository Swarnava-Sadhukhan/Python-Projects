from covid import Covid

covid=Covid(source='worldometers')
data=covid.get_data()

#input country name in small letters
c=input('Enter country name : ')
print('Showing Covide Results for '+c)

countries=covid.get_status_by_country_name(c)
print('Tests Performed: '+str(countries['total_tests']))
print('Confirmed Cases: '+str(countries['confirmed']))
print('Active Cases: '+str(countries['active']))
print('New Cases: '+str(countries['new_cases']))
death=countries['deaths']
print('Deaths: '+str(death))
print('New Deaths: '+str(countries['new_deaths']))
rec=countries['recovered']
print('Recovered: '+str(rec))

#Calculate mortality rate
rate=round(death*100/(death+rec),2)
print('Mortality Rate: '+str(rate))


