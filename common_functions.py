def get_columns():
    '''
    Get a subset of the columns, according to instructions
    '''
    data_columns = ['corporation', 'lastmonth_activity',
                    'lastyear_activity', 'number_of_employees', 'exited']

    X_columns = ['lastmonth_activity',
                 'lastyear_activity', 'number_of_employees']

    y_column = ['exited']

    return X_columns, y_column
