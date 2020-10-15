import time
import pandas as pd
import numpy as np

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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('What city do you want to explore? ').lower()
    cities = ('chicago', 'new york city', 'washington')

    while city not in cities:
        city = input('\nPlease enter chicago, new york city or washington: ').lower()

    # chooeses the filter inputted by the user

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('What month do you want to explore (all, january, february, ... , june)? ').lower()
    months = ('all', 'january', 'february', 'march', 'april', 'may', 'june')
    while month not in months:
        month = input('Please enter: all or january, february, ... , june: ').lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('What day of the week do you want to explore (all, monday, tuesday, ... sunday)? ').title()
    days = ('All', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
    while day not in days:
        day = input('Please enter: all or monday, tuesday, ... sunday: ').title()

    print('-'*40)
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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'All':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    common_month = df['month'].mode()[0]
    print('The most common month is the {}th month.'.format(common_month))

    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.month
    common_day = df['day_of_week'].mode()[0]
    print('\nThe most common day of the week is the {}th day.'.format(common_day))

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('\nThe most common hour is the {}th hour.'.format(common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('The most common start station is: {}.'.format(common_start_station))


    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('\nThe most common end station is: {}.'.format(common_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    common_comb_station = df.groupby(['Start Station','End Station']).size().nlargest(1)
    print('\nThe most common combination of start and end station is:\n{}.'.format(common_comb_station))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The total travel time is {} hours and {:.2f} minutes.'.format(total_travel_time//3600,
                                                     (total_travel_time/3600-total_travel_time//3600)*60))


    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('\nThe mean travel time is {} minutes and {:.2f} seconds.'.format(mean_travel_time//60,          (mean_travel_time/60-mean_travel_time//60)*60))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('The amount of users per type are:')
    print(user_types)


    # TO DO: Display counts of gender
    gender_count = df['Gender'].value_counts()
    print('\nThe amount of male and female users are:')
    print(gender_count)



    # TO DO: Display earliest, most recent, and most common year of birth
    most_common_birth = df['Birth Year'].mode()[0]
    earliest_birth = df['Birth Year'][df['Birth Year'].idxmin()]
    most_recent_birth = df['Birth Year'][df['Birth Year'].idxmax()]
    print('\nThe earliest year of birth is: {}.'.format(int(earliest_birth)))
    print('\nThe most recent year of birth is: {}.'.format(int(most_recent_birth)))
    print('\nThe most common year of birth is: {}.'.format(int(most_common_birth)))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
