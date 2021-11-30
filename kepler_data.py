# importing libraries
import pandas as pd

# importing data file named kepler_data.csv
exoplanet_data = pd.read_csv('/home/vijay/Desktop/NIT R/T Sem/Technical writing/readable-data/kepler_data.csv')

# taking out coloums and storing in arrays.
orbital_period_unit_days = exoplanet_data.iloc[:, :1]
eccentricity = exoplanet_data.iloc[:,1:2]
transit_duration_unit_hr = exoplanet_data.iloc[:,2:3]
transit_dept_ppm = exoplanet_data.iloc[:,3:4]
planet_star_radius_ratio = exoplanet_data.iloc[:,4:5]
planet_radius_unit_earth_radii = exoplanet_data.iloc[:,5:6]
orbital_semi_major_axis_unit_au = exoplanet_data.iloc[:,6:7]
inclination_unit_degree = exoplanet_data.iloc[:, 7:8]
planet_star_distance_over_star_radius = exoplanet_data.iloc[:, 8:9]
stellar_effective_temperature_unit_kelvin = exoplanet_data.iloc[:, 9:10]
stellar_radius_unit_solar_radius = exoplanet_data.iloc[:, 10:11]
stellar_mass_unit_solar_mass = exoplanet_data.iloc[:, 11:12]

# defining a function to calculate mean, median and std deviation
def statistical_quantities(array_input):
    """It calculates mean, median, std and confi. interval of the array"""

    mean = array_input.mean()
    median = array_input.median()
    std = array_input.std()

    print("The mean of " + str(mean))
    print("The median of " + str(median))
    print("The standard deviation of " + str(std))

# printing mean ... std deviation
statistical_quantities(orbital_period_unit_days)
statistical_quantities(eccentricity)
statistical_quantities(transit_dept_ppm)
statistical_quantities(transit_duration_unit_hr)
statistical_quantities(planet_star_radius_ratio)
statistical_quantities(planet_radius_unit_earth_radii)
statistical_quantities(orbital_semi_major_axis_unit_au)
statistical_quantities(inclination_unit_degree)
statistical_quantities(planet_star_distance_over_star_radius)
statistical_quantities(stellar_effective_temperature_unit_kelvin)
statistical_quantities(stellar_mass_unit_solar_mass)
statistical_quantities(stellar_radius_unit_solar_radius)

