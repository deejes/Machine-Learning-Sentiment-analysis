import json
with open("tesla728-us.txt", 'r') as infile:
    data = infile.read()




data = [float(x) for x in data[1:-1].split(',')]
# dates = [x for x in dates[1:-1].split(',')]

# print (len(dates))


interval = int(len(data)*.1)

mod_data = []
# mod_dates = []

# import pdb; pdb.set_trace()
start = 0
end = interval
for x in range(10):
    data_slice = data[start:end]
    slice_average = sum(data_slice) / float(len(data_slice))
    mod_data.append(slice_average)

    # date_slice = str(dates[start][5:18]+'-'+dates[end-1][13:18])
    # import pdb; pdb.set_trace()
    # mod_dates.append(date_slice)


    start += interval
    end += interval



print ('us-tesla',mod_data)
# print (mod_dates)


# with open("monsanto_sent_data.txt", 'w') as outfile:
#     json.dump(mod_data, outfile)
# with open("monsanto_sent_dates_data.txt", 'w') as outfile:
#     json.dump(mod_dates, outfile)
