import request_handeling
import beatifulsoup
import numpy #Trying out a matrix 

#   For 3 day prediction: https://www.wetter.com/wetter_aktuell/wettervorhersage/3_tagesvorhersage/deutschland/thuine/DE0010504.html
url_wetter_com = 'https://www.wetter.com/wetter_aktuell/wettervorhersage/7_tagesvorhersage/deutschland/thuine/DE0010504.html'

def get_wetter_com_data():
    html_code_wetter_com = request_handeling.request_website(url_wetter_com)
    bs = beatifulsoup.bs4_convert(html_code_wetter_com)[0] #Only first output necessary

    #TEMPERATURE
    temperature_list = bs.find_all("span",class_ = 'swg-text-large')#list of all temperatures on a site
    all_temperatures = []

    for raw_temperature in temperature_list:
        real_temperature_with_degree = raw_temperature.get_text()

        #getting rid of the degree symbols
        legal_symbols = set('0123456789') #Legal Symbols of Temperature
        real_temperature = ''.join(char if char in legal_symbols else '' for char in real_temperature_with_degree) #every unknown charakter turns into nothing
        all_temperatures.append(real_temperature)
    
    #print(all_temperatures)

    #RAIN PROBABILITY (TO DO)

    return all_temperatures

def sort_wetter_com_data(all_temperatures):

    amount_of_temperatures_each_day = 5 #every day has 5 temperatures, first is the overall temperature, the next 4 are mornings, noon, evening, night
    amount_of_days = int(len(all_temperatures)/amount_of_temperatures_each_day) #amount of days
    matrix_temperature = numpy.zeros(shape=(amount_of_days,amount_of_temperatures_each_day)) #empty matrix
    
    for i in range(0,len(all_temperatures)):
        matrix_temperature.itemset(i,all_temperatures[i])
    print(matrix_temperature)
    #7 lines and 5 columns are 7 days and 5 temperatures

    pass 



all_temperatures = get_wetter_com_data()
sort_wetter_com_data(all_temperatures)