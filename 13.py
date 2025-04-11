filtered_data =[]
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)