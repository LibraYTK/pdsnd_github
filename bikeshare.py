import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}

cities = ['chicago', 'washington', 'new york city']
months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
days = ['monday', 'tuesday', 'wednesday', 'friday', 'saturday', 'sunday', 'all']


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
    while True:
        city = input('Please input the city name you want to see.').lower()
        if city in cities:
            break
        else:
            print('you can only choose chicago, new york city or washington.')

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('Please input the month you want to see or type all to see six months').lower()
        if month in months:
            break
        else:
            print('you can choose all or select one month from Jan to Jun')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Please input the day you want to search or type all to see seven days').lower()
        if day in days:
            break
        else:
            print('please input the correct day of week or input all to see seven days\' data')

    print('-' * 40)
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

    # load csv data file
    df = pd.read_csv(CITY_DATA[city])
    # change StartDate to be a datetime data
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['Month'] = pd.to_datetime(df['Start Time']).dt.month

    df['days of week'] = pd.to_datetime(df['Start Time']).dt.day_name()

    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        month = months.index(month)
        df = df.loc[df['Month'] == month]

        # filter by day of week if applicable
    if day != 'all':
        df = df.loc[df['days of week'] == day]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['Month'].mode()[0]

    print('Most common month:', common_month)

    # TO DO: display the most common day of week
    common_days_of_week = df['days of week'].mode()[0]

    print('Most common days of week:', common_days_of_week)

    # TO DO: display the most common start hour
    common_hour = df['hour'].mode()[0]

    print('Most common Start Hour:', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]

    print('Most common Start Station:', common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]

    print('Most common End Station:', common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    combination = (df['Start Station'] + ',' + df['End Station']).mode()[0]
    print('most common trip combination:', str(combination.split(',')))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_trip_duration = df['Trip Duration'].sum()
    print('The total trip duration is: {} seconds'.format(str(total_trip_duration)))

    # TO DO: display mean travel time
    average_trip_duration = df['Trip Duration'].mean()
    print('The average trip duration is: {} seconds'.format(str(average_trip_duration)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_user_types = df['User Type'].value_counts()
    print("The count of each user types:\n" + str(count_user_types))

    if 'Gender' in df.columns:
        # TO DO: Display counts of gender
        count_gender = df['Gender'].value_counts()
        print("The count of gender:\n" + str(count_gender))
    if 'Birth Year' in df.columns:
        # TO DO: Display earliest, most recent, and most common year of birth
        earliest_birth = df['Birth Year'].min()
        most_recent_birth = df['Birth Year'].max()
        most_common_birth = df['Birth Year'].mode()[0]
        print('The earliest birth is:', int(earliest_birth))
        print('Most recent birth:', int(most_recent_birth))
        print('Most common birth:', int(most_common_birth))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def display_data(df):
    """Display 5 trip data per page"""
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no?")
    start_loc = 0
    while True:
        if view_data != 'yes':
            break
        else:
            print(df.iloc[start_loc:start_loc + 5])
            start_loc += 5
            view_display = input("Do you wish to continue?: ").lower()
            if view_display != 'yes':
                break
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
