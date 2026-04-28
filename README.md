# Weather Dashboard using API calls

A **CLI** weather dashboard which uses api calls to **Open-Meteo** to retrieve and display weather data for a city given by the user.

## User Interface

When the program is run, the user is asked to enter the city name the first time. When they enter, the get current temperature and windspeed. It also gives the temperature forecast for next seven days.

After the first time, it will display previous searches in an ordered list so that you just have to type the number. You can still go for a new city by typing zero.

## Program Execution

When a city is entered, the latitude and longitude are retrived by using api call to Open-Meteo. Then another api call to Open-meteo provides the weather details. 
After the first search, the city name and coordinates are stored in a database using sqlite3. They are retrieved after when the program is rerun.