dist_in_km = 150
time_in_hr = 2

dist_in_mi = dist_in_km / 1.6
dist_in_m = dist_in_km * 1000
time_in_sec = time_in_hr * 3600

speed_kmph = dist_in_km / time_in_hr
speed_mph = dist_in_mi / time_in_hr
speed_mps = dist_in_m / time_in_sec

print(f"The speed in kilometers per hour is:{speed_kmph}")
print(f"The speed in miles per hour is:{speed_mph}")
print(f"The speed in meters per second is:{speed_mps}")