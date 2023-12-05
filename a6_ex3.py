import os

def merge_csv_files(*paths, delimiter=';', only_shared_columns=False):
    files_data = {} # Store the headers and rows of each file
    all_columns = set() # store the names of all columns across files
    shared_columns = None  # List to store the intersection of columns, when only_shared_columns=True

    for path in paths:
        with open(path, 'r') as file:
            headers = file.readline().strip().split(delimiter) # read line, rm \n and sep by delimiter
            all_columns.update(headers) # only add values which don't exist in all columns
            rows = file.readlines()
            # save headers, rows -> without \n and split by delimiter to files data
            files_data[path] = {'headers': headers, 'rows': [row.strip().split(delimiter) for row in rows]}

            if shared_columns is None: # True when reading first file -> no headers to compare
                shared_columns = set(headers) # add all of headers to shared_columns
            else:
                shared_columns.intersection_update(headers) # Keep only headers that are in shared_columns and headers

    if only_shared_columns: # only_shared_columns=True
        final_columns = shared_columns
    else: # only_shared_columns=False
        final_columns = all_columns

    output_dir = os.path.dirname(paths[0]) # finding operating directory
    output_path = os.path.join(output_dir, 'merged.csv') # saving merged file

    # Write data to merged.csv
    with open(output_path, 'w') as file:
        file.write(delimiter.join(final_columns) + '\n')  # Add headers

        for path, data in files_data.items(): # Go through files in data, call by path
            for row in data['rows']:
                # create dict for each header, linking to values of header going through dict with enumerate,
                # getting index (i) and value for elements
                row_data = {data['headers'][i]: value for i, value in enumerate(row)}

                # Create list (for merged row), if column form final_columns not existing, fill with NaN
                merged_row = [row_data.get(column, 'NaN') for column in final_columns]

                file.write(delimiter.join(merged_row) + '\n') # Merge new row to file, sep by \n



