answer = input('Would you like to continue?')

if answer == 'n' or answer == 'no':
    print('Exiting')
elif answer == 'y' or answer == 'yes':
    print('Continuing...')
    print('Complete!')
else:
    print('Please, try again and respond with yes or no.')
