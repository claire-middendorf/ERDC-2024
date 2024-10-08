# -*- coding: utf-8 -*-

"""
Claire Middendorf

    Required, constant data structures for Log-Pearson Type III analysis

"""

frequency_factors_records = [
    {'cs': 3, '1.0101': -0.667, '2': -0.396, '5': 0.42, '10': 1.18, '25': 2.278, '50': 3.152, '100': 4.051, '200': 4.97},
    {'cs': 2.9, '1.0101': -0.69, '2': -0.39, '5': 0.44, '10': 1.195, '25': 2.277, '50': 3.134, '100': 4.013, '200': 4.904},
    {'cs': 2.8, '1.0101': -0.714, '2': -0.384, '5': 0.46, '10': 1.21, '25': 2.275, '50': 3.114, '100': 3.973, '200': 4.847},
    {'cs': 2.7, '1.0101': -0.74, '2': -0.376, '5': 0.479, '10': 1.224, '25': 2.272, '50': 3.093, '100': 3.932, '200': 4.783},
    {'cs': 2.6, '1.0101': -0.769, '2': -0.368, '5': 0.499, '10': 1.238, '25': 2.267, '50': 3.071, '100': 3.889, '200': 4.718},
    {'cs': 2.5, '1.0101': -0.799, '2': -0.36, '5': 0.518, '10': 1.25, '25': 2.262, '50': 3.048, '100': 3.845, '200': 4.652},
    {'cs': 2.4, '1.0101': -0.832, '2': -0.351, '5': 0.537, '10': 1.262, '25': 2.256, '50': 3.023, '100': 3.8, '200': 4.584},
    {'cs': 2.3, '1.0101': -0.867, '2': -0.341, '5': 0.555, '10': 1.274, '25': 2.248, '50': 2.997, '100': 3.753, '200': 4.515},
    {'cs': 2.2, '1.0101': -0.905, '2': -0.33, '5': 0.574, '10': 1.284, '25': 2.24, '50': 2.97, '100': 3.705, '200': 4.444},
    {'cs': 2.1, '1.0101': -0.946, '2': -0.319, '5': 0.592, '10': 1.294, '25': 2.23, '50': 2.942, '100': 3.656, '200': 4.372},
    {'cs': 2, '1.0101': -0.99, '2': -0.307, '5': 0.609, '10': 1.302, '25': 2.219, '50': 2.912, '100': 3.605, '200': 4.298},
    {'cs': 1.9, '1.0101': -1.037, '2': -0.294, '5': 0.627, '10': 1.31, '25': 2.207, '50': 2.881, '100': 3.553, '200': 4.223},
    {'cs': 1.8, '1.0101': -1.087, '2': -0.282, '5': 0.643, '10': 1.318, '25': 2.193, '50': 2.848, '100': 3.499, '200': 4.147},
    {'cs': 1.7, '1.0101': -1.14, '2': -0.268, '5': 0.66, '10': 1.324, '25': 2.179, '50': 2.815, '100': 3.444, '200': 4.069},
    {'cs': 1.6, '1.0101': -1.197, '2': -0.254, '5': 0.675, '10': 1.329, '25': 2.163, '50': 2.78, '100': 3.388, '200': 3.99},
    {'cs': 1.5, '1.0101': -1.256, '2': -0.24, '5': 0.69, '10': 1.333, '25': 2.146, '50': 2.743, '100': 3.33, '200': 3.91},
    {'cs': 1.4, '1.0101': -1.318, '2': -0.225, '5': 0.705, '10': 1.337, '25': 2.128, '50': 2.706, '100': 3.271, '200': 3.828},
    {'cs': 1.3, '1.0101': -1.383, '2': -0.21, '5': 0.719, '10': 1.339, '25': 2.108, '50': 2.666, '100': 3.211, '200': 3.745},
    {'cs': 1.2, '1.0101': -1.449, '2': -0.195, '5': 0.732, '10': 1.34, '25': 2.087, '50': 2.626, '100': 3.149, '200': 3.661},
    {'cs': 1.1, '1.0101': -1.518, '2': -0.18, '5': 0.745, '10': 1.341, '25': 2.066, '50': 2.585, '100': 3.087, '200': 3.575},
    {'cs': 1, '1.0101': -1.588, '2': -0.164, '5': 0.758, '10': 1.34, '25': 2.043, '50': 2.542, '100': 3.022, '200': 3.489},
    {'cs': 0.9, '1.0101': -1.66, '2': -0.148, '5': 0.769, '10': 1.339, '25': 2.018, '50': 2.498, '100': 2.957, '200': 3.401},
    {'cs': 0.8, '1.0101': -1.733, '2': -0.132, '5': 0.78, '10': 1.336, '25': 1.993, '50': 2.453, '100': 2.891, '200': 3.312},
    {'cs': 0.7, '1.0101': -1.806, '2': -0.116, '5': 0.79, '10': 1.333, '25': 1.967, '50': 2.407, '100': 2.824, '200': 3.223},
    {'cs': 0.6, '1.0101': -1.88, '2': -0.099, '5': 0.8, '10': 1.328, '25': 1.939, '50': 2.359, '100': 2.755, '200': 3.132},
    {'cs': 0.5, '1.0101': -1.955, '2': -0.083, '5': 0.808, '10': 1.323, '25': 1.91, '50': 2.311, '100': 2.686, '200': 3.041},
    {'cs': 0.4, '1.0101': -2.029, '2': -0.066, '5': 0.816, '10': 1.317, '25': 1.88, '50': 2.261, '100': 2.615, '200': 2.949},
    {'cs': 0.3, '1.0101': -2.104, '2': -0.05, '5': 0.824, '10': 1.309, '25': 1.849, '50': 2.211, '100': 2.544, '200': 2.856},
    {'cs': 0.2, '1.0101': -2.178, '2': -0.033, '5': 0.83, '10': 1.301, '25': 1.818, '50': 2.159, '100': 2.472, '200': 2.763},
    {'cs': 0.1, '1.0101': -2.252, '2': -0.017, '5': 0.836, '10': 1.292, '25': 1.785, '50': 2.107, '100': 2.4, '200': 2.67},
    {'cs': 0, '1.0101': -2.326, '2': 0, '5': 0.842, '10': 1.282, '25': 1.751, '50': 2.054, '100': 2.326, '200': 2.576},
    {'cs': -0.1, '1.0101': -2.4, '2': 0.017, '5': 0.846, '10': 1.27, '25': 1.716, '50': 2, '100': 2.252, '200': 2.482},
    {'cs': -0.2, '1.0101': -2.472, '2': 0.033, '5': 0.85, '10': 1.258, '25': 1.68, '50': 1.945, '100': 2.178, '200': 2.388},
    {'cs': -0.3, '1.0101': -2.544, '2': 0.05, '5': 0.853, '10': 1.245, '25': 1.643, '50': 1.89, '100': 2.104, '200': 2.294},
    {'cs': -0.4, '1.0101': -2.615, '2': 0.066, '5': 0.855, '10': 1.231, '25': 1.606, '50': 1.834, '100': 2.029, '200': 2.201},
    {'cs': -0.5, '1.0101': -2.686, '2': 0.083, '5': 0.856, '10': 1.216, '25': 1.567, '50': 1.777, '100': 1.955, '200': 2.108},
    {'cs': -0.6, '1.0101': -2.755, '2': 0.099, '5': 0.857, '10': 1.2, '25': 1.528, '50': 1.72, '100': 1.88, '200': 2.016},
    {'cs': -0.7, '1.0101': -2.824, '2': 0.116, '5': 0.857, '10': 1.183, '25': 1.488, '50': 1.663, '100': 1.806, '200': 1.926},
    {'cs': -0.8, '1.0101': -2.891, '2': 0.132, '5': 0.856, '10': 1.166, '25': 1.448, '50': 1.606, '100': 1.733, '200': 1.837},
    {'cs': -0.9, '1.0101': -2.957, '2': 0.148, '5': 0.854, '10': 1.147, '25': 1.407, '50': 1.549, '100': 1.66, '200': 1.749},
    {'cs': -1, '1.0101': -3.022, '2': 0.164, '5': 0.852, '10': 1.128, '25': 1.366, '50': 1.492, '100': 1.588, '200': 1.664},
    {'cs': -1.1, '1.0101': -3.087, '2': 0.18, '5': 0.848, '10': 1.107, '25': 1.324, '50': 1.435, '100': 1.518, '200': 1.581},
    {'cs': -1.2, '1.0101': -3.149, '2': 0.195, '5': 0.844, '10': 1.086, '25': 1.282, '50': 1.379, '100': 1.449, '200': 1.501},
    {'cs': -1.3, '1.0101': -3.211, '2': 0.21, '5': 0.838, '10': 1.064, '25': 1.24, '50': 1.324, '100': 1.383, '200': 1.424},
    {'cs': -1.4, '1.0101': -3.271, '2': 0.225, '5': 0.832, '10': 1.041, '25': 1.198, '50': 1.27, '100': 1.318, '200': 1.351},
    {'cs': -1.5, '1.0101': -3.33, '2': 0.24, '5': 0.825, '10': 1.018, '25': 1.157, '50': 1.217, '100': 1.256, '200': 1.282},
    {'cs': -1.6, '1.0101': -3.88, '2': 0.254, '5': 0.817, '10': 0.994, '25': 1.116, '50': 1.166, '100': 1.197, '200': 1.216},
    {'cs': -1.7, '1.0101': -3.444, '2': 0.268, '5': 0.808, '10': 0.97, '25': 1.075, '50': 1.116, '100': 1.14, '200': 1.155},
    {'cs': -1.8, '1.0101': -3.499, '2': 0.282, '5': 0.799, '10': 0.945, '25': 1.035, '50': 1.069, '100': 1.087, '200': 1.097},
    {'cs': -1.9, '1.0101': -3.553, '2': 0.294, '5': 0.788, '10': 0.92, '25': 0.996, '50': 1.023, '100': 1.037, '200': 1.044},
    {'cs': -2, '1.0101': -3.605, '2': 0.307, '5': 0.777, '10': 0.895, '25': 0.959, '50': 0.98, '100': 0.99, '200': 0.995},
    {'cs': -2.1, '1.0101': -3.656, '2': 0.319, '5': 0.765, '10': 0.869, '25': 0.923, '50': 0.939, '100': 0.946, '200': 0.949},
    {'cs': -2.2, '1.0101': -3.705, '2': 0.33, '5': 0.752, '10': 0.844, '25': 0.888, '50': 0.9, '100': 0.905, '200': 0.907},
    {'cs': -2.3, '1.0101': -3.753, '2': 0.341, '5': 0.739, '10': 0.819, '25': 0.855, '50': 0.864, '100': 0.867, '200': 0.869},
    {'cs': -2.4, '1.0101': -3.8, '2': 0.351, '5': 0.725, '10': 0.795, '25': 0.823, '50': 0.83, '100': 0.832, '200': 0.833},
    {'cs': -2.5, '1.0101': -3.845, '2': 0.36, '5': 0.711, '10': 0.711, '25': 0.793, '50': 0.798, '100': 0.799, '200': 0.8},
    {'cs': -2.6, '1.0101': -3.899, '2': 0.368, '5': 0.696, '10': 0.747, '25': 0.764, '50': 0.768, '100': 0.769, '200': 0.769},
    {'cs': -2.7, '1.0101': -3.932, '2': 0.376, '5': 0.681, '10': 0.724, '25': 0.738, '50': 0.74, '100': 0.74, '200': 0.741},
    {'cs': -2.8, '1.0101': -3.973, '2': 0.384, '5': 0.666, '10': 0.702, '25': 0.712, '50': 0.714, '100': 0.714, '200': 0.714},
    {'cs': -2.9, '1.0101': -4.013, '2': 0.39, '5': 0.651, '10': 0.681, '25': 0.683, '50': 0.689, '100': 0.69, '200': 0.69},
    {'cs': -3, '1.0101': -4.051, '2': 0.396, '5': 0.636, '10': 0.66, '25': 0.666, '50': 0.666, '100': 0.667, '200': 0.667},
]
