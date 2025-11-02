day = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

day_dict = {i+1:day[i] for i in range(len(day))}
print(day_dict)
day_dict = {n:i for (i, n) in day_dict.items()}
print(day_dict)