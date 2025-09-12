import numpy as np

temp_data_untitled = np.random.randint(low=32, high=55, size=(7*24, 1))
temp_data_titled = np.array(temp_data_untitled, dtype=[('NYC', 'i4'), ('Los Angeles', 'i4'), ('Chicago', 'i4')])
np.save("../data/simulated_temperature.npy", temp_data_titled)