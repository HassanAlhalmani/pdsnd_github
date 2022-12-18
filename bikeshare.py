import time
import pandas as pd
import numpy as np

# this is the refactoring branch.

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # A time delay between texts.
    time.sleep(1)
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    # Declaring a variable of a city and asking for user Input.
    city = input("Please choose a city! Choose between these options --> (Chicago, New York City, Washington):\n--> ").lower()
    # A while loop that checks for correct input given by the user.
    while city not in CITY_DATA.keys():
        print('Invalid City')
        time.sleep(1)
        print('Please enter a valid city..')
        time.sleep(1)
        city = input("Please choose a city! Choose between these options --> (Chicago, New York City, Washington):\n--> ").lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    
    # Declaring a variable of a month and asking for user Input.
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    # A while loop that checks for correct input given by the user.
    while True:
        time.sleep(1)
        month = input("Please choose a month between these options --> (January, February, March, April, May, June, All):\n--> ").lower()
        if month in months:
            break
        else:
            print('Please enter a valid month: ')
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    # Declaring a variable of a day and asking for user Input.
    days =  ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']
    # A while loop that checks for correct input given by the user.
    while True:
        time.sleep(1)
        day = input('Please choose a day:\n--> ').lower()
        if day in days:
            break
        else:
            print('Please enter a valid day: ')
    
    print('-'*60)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # Reading the city data from the csv file.
    df =  pd.read_csv(CITY_DATA[city])
    
    
    # Creating dataframes for the columns named in the csv file. In order to do that we need to convert the string in the csv file to a datafram by using pandas library.
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['start hour'] = df['Start Time'].dt.hour
    
    if month !=  'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        # Adding 1 index to months to get a specific number for each month.
        month = months.index(month) + 1
        df = df[df['month'] ==  month]
        
    if month !=  'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('The most common month is: {}'.format(df['month'].mode()[0]))

    # TO DO: display the most common day of week
    print('The most common day is: {}'.format(df['day_of_week'].mode()[0]))

    # TO DO: display the most common start hour
    print('The most common start hour is: {}'.format(df['start hour'].mode()[0]))
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*60)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('The most common start station is: {}'.format(df['Start Station'].mode()[0]))

    # TO DO: display most commonly used end station
    print('The most common end station is: {}'.format(df['End Station'].mode()[0]))

    # TO DO: display most frequent combination of start station and end station trip
    df['road']=df['Start Station']+","+df['End Station']
    print('The most common road is: {}'.format(df['road'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*60)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('The total travel time is: ',(df['Trip Duration'].sum()).round())

    # TO DO: display mean travel time
    print('The mean travel time is: ',(df['Trip Duration'].mean()).round())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*60)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(df['User Type'].value_counts().to_frame)

    # TO DO: Display counts of gender
    if city != 'washington':
        print(df['Gender'].value_counts().to_frame())

    # TO DO: Display earliest, most recent, and most common year of birth
        print('The most common year of birth is: ',int(df['Birth Year'].mode()[0]))
        print('The most recent year of birth is: ',int(df['Birth Year'].max()))
        print('The earliest year of birth is: ',int(df['Birth Year'].min()))
        
    else:
        print('There is no data for this city')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*60)
    

def show_row_data(df):
    
    # To allow the user to choose if they want to see 5 lines of row data
    print('\nRaw data is availabe to check... \n')
    
    i=0
    user_input=input('Would you like to display 5 lines of raw data? Please enter: YES or NO:\n--> ').lower()
    if  user_input not in ['yes', 'no']:
        print('Invalid choice,  plesae type yes or no')
        user_input=input('Would you like to display 5 lines of raw data? Please enter: YES or NO:\n--> ').lower()
    elif user_input != 'yes':
        print('Alright')
    else:
        while i+5 < df.shape[0]:
            print(df.iloc[i:i+5])
            i += 5
            user_input = input('Would you like to display more 5 lines of raw data? Please enter: YES or NO:\n--> ').lower()
            if user_input != 'yes':
                print('Alright')
                break
    
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        show_row_data(df)

        restart = input('\nWould you like to restart? Enter YES or NO:\n--> ')
        if restart.lower() != 'yes':
            print('Good Bye!')
            break


if __name__ == "__main__":
	main()
