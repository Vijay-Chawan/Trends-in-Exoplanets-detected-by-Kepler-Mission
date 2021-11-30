# importing libraries
import numpy as np

# importing data file named kepler_data.csv
planet_radius = np.genfromtxt('/home/vijay/Desktop/NIT R/T Sem/Technical writing/readable-data/kepler_data_planet_size.csv', delimiter=',')

j_lim_lower = 11.2*(1 - 0.25)  # range 10% of jupiter's radius.
j_lim_upper = 11.2*(1 + 0.25)

e_lim_lower = 1*(1 - 0.25)  # range 10% of earth's radius.
e_lim_upper = 1*(1 + 0.25)

jupiter_size_planet = np.array([0])
earth_size_planet = np.array([0])

for i in range(0, len(planet_radius) - 1):

    j_1 = planet_radius[i]
    j_2 = planet_radius[i]
    e_1 = planet_radius[i]
    e_2 = planet_radius[i]

    if j_1 <= j_lim_upper and j_2 >= j_lim_lower:
        jupiter_size_planet = np.append(jupiter_size_planet, j_1)

    if e_1 <= e_lim_upper and e_2 >= e_lim_lower:
        earth_size_planet = np.append(earth_size_planet, e_1)

c_jupiter_size_planet = np.delete(jupiter_size_planet, 0)
c_earth_size_planet = np.delete(earth_size_planet, 0)

print(len(c_jupiter_size_planet), len(c_earth_size_planet))