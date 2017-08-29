import json
scores = [0.7, 0.9, 1.3, 0.2, 0.2, 0.8, 0.6, 0.9, 1.3, 1.7, 1.7, 2, 0.7, 1, 0.7, 1.5, 0.9, 3.3, 1.5, 0.7, 0.9, 0.9, 0.9, 0.6, 0.5, 0.2, 0, 0.8, 0.6, 1.4, 2.4, 1.4, 2, 1.5, 0.8, 0.8, 2.4, 0.9, 1.7, 1.7, 0.6, 1.7, 1.5, 1.8, 1.2, 3.3, 0.8, 0.8, 1.3, 1.8, 0.9, 1.1, 0.6, 0.7, 0.7, 0.7, 1.2, 0.9, 0.9, 0.9, 0.9, 0.9, 1.1, 1.4, 0.3, 0.9, 2, 0.8, 1.8, 2, 0.9, 1.4, 0.9, 0.9, 1.5, 1.5, 1.8, 2.2, 1.4, 0.6, 1.5, 0.3, 2.4, 0.9, 2, 0.3, 1, 1.3, 1.4, 1.5, 1, 1.3, 1.1, 1.2, 0.8, 0.9, 1.4, 1.7, 1.1, 1.3, 2.3, 0.9, 0.9, 0.9, 0.9, 0.7, 1.3, 1.5, 0.9, 0.2, 1.8, 1.9, 0.9, 1.3, 0.9, 1.8, 0.1, 0.9, 0.9, 0.9, 1.6, 0.6, 0.8, 1, 0.8, 0.7, 0.9, 0.8, 1.7, 1, 1.2, 1.1, 0.8, 0.5, 0.2, 0.9, 0.8, 0.8, 0.8, 0.8, 1.1, 0.8, 0.8, 2, 0.8, 0.7, 1.1, 0.9, 0.8, 0.8, 0.7, 0.9, 0.8, 1.1, 1.4, 0, 1.1, 0.1, 0.1, 0.8, 0.8, 1.3, 1.2, 0.7, 0.9, 0.8, 0.8, 1.1, 0.8, 1.6, 0.8, 0.9, 1.6, 1.3, 0.9, 0.6, 0.8, 0.9, 0.6, 1.4, 1.7, 1.7, 1.8, 1, 0.9, 1.5, 0.9, 1.7, 1.3, 1.6, 0.8, 0.6, 1.4, 1.1, 0.9, 1.2, 1.3, 1.9, 1, 0.8, 0.7, 0.7, 0.6, 0.8, 1.4, 1, 0.4, 1.4, 1.8, 0.3, 3.3, 1.6, 0.5, 1.1, 0.7, 0.8, 0.9, 1.1, 1.3, 0.7, 0.8, 0.9, 1.5, 0.9, 1.1, 1.4, 0.4, 0, 0.7, 0.2, 0.7, 0.3, 2.1, 1.6, 0.4, 1.5, 1.2, 0.7, 0.5, 0.5, 1.2, 1, 1.1, 1.5, 1.1, 0.9, 1.5, 0.6, 0, 1.6, 0.9, 1.5, 0.8, 1.8, 0.9, 0.7, 1, 0.9, 0.3, 0.9, 0.7, 0.8, 0.2, 0.8, 0.8, 0.9, 0.8, 0.8, 0.8, 1.3, 0.4, 0.8, 1.1, 1.9, 1.7, 0.5, 1.3, 1.8, 0.5, 0.8, 1, 1.7, 0.8, 1.1, 2.1, 2.1, 1.4, 1.4, 1.5, 1.5, 0.1, 0.6, 1.8, 1.1, 0.9, 1.7, 0.9, 2.4, 1.7, 1.2, 0.9, 1, 0.7, 0.4, 0.9, 3.3, 0.8, 0.8, 0.9, 1.8, 0.8, 0.7, 1, 0.8, 0.9, 1, 1.7, 0.2, 0.9, 0.9, 1.3, 0.7, 0.9, 1.1, 0.4, 0.5, 1.9, 0.6, 1.5, 1.5, 1.3, 1.3, 1.2, 0.8, 0.6, 0.7, 0.8, 0.3, 1.5, 0.7, 0.6, 0.9, 0.7, 0.8, 2, 1.1, 0.1, 1.7, 0.8, 1.7, 0.6, 0.5, 2.8, 0.3, 0.8, 1.5, 1.8, 0.3, 0.6, 1.4, 1.3, 0.8, 0.9, 0.6, 0.9, 1.4, 1, 0.8, 1.3, 0.5, 1.7, 1, 1, 0.8, 0.8, 0.8, 1, 0.6, 0.6, 1, 0.8, 0.4, 0.9, 0.5, 0.6, 0.5, 0.3, 1.9, 1, 0.9, 0.7, 1.5, 0.7, 0.9, 1.7, 0.7, 0.9, 0.9, 0.8, 0.6, 0.8, 1.5, 2.7, 0.5, 1.2, 0.6, 0.9, 0, 1, 0.9, 0.7, 1, 1, 1.4, 1.5, 0.9, 1.3, 0.7, 1.6, 1.4, 0.8, 0.8, 1.5, 0.6, 0.3, 0.7, 1.9, 1, 2.1, 0.8, 2.7, 0.3, 1.2, 1.4, 0, 1, 0.9, 1.8, 0.7, 1.1, 0.9, 0.8, 2, 1.4, 1.2, 0.9, 0.1, 0.8, 1, 1.5, 2.3, 1.6, 1.1, 1.2, 0.8, 2, 0.5, 0.5, 0.6, 0, 0.9, 1.5, 0.8, 0.7, 0.9, 1, 1, 0.9, 0.9, 1.8, 0.2, 0.7, 0.7, 0.9, 0, 0, 0, 0, 0.7, 0.7, 0, 0, 0, 0, 0, 0.7, 0, 1.8, 0, 0.5, 2.3, 1.1, 0.8, 0.7, 1, 1.8, 0.9, 0.9, 0.7, 0.7,0.7, 0.8, 0.8, 0.9, 0.7, 0.9, 0.7, 0.8, 0.9, 0.9, 0.9, 0.8, 1, 0.7, 1.7, 1, 1, 0.8, 1.3, 0.8, 1.6, 0.9, 1.5, 1.5, 1.3, 0.9, 0.7, 1.7, 2.9, 0.8, 0.8, 1.2, 0.5, 0.8, 0.8, 0.8, 1.4, 1.6, 2.7, 1.1, 0.9, 1, 1.8, 1.7, 1.6, 1.5, 1.8, 0.5, 0.9, 0.6, 1.3, 1.2, 0.9, 1.4, 1.2, 0.9, 0.8, 1.2, 1, 0.9, 1, 0.9, 0.8, 0.9, 1.1, 0.8, 0.9, 1, 0.2, 1.3, 1.3, 1.3, 0.4, 1.8, 1.6, 1.7, 1.3, 0.7, 1.3, 0.8, 1.6, 0.9, 0.8, 0.2, 0.7, 2, 1.2, 0.7, 1.6, 0.9, 0.8, 0.6, 0.9, 0.3, 1, 0.6, 0.9, 0.9, 1, 0.9, 0.1, 0.7, 1.5, 1.3, 0.7, 0.7, 0.9, 0.9, 2.3, 0.9, 1.6, 0.7, 1, 1.7, 0.7, 0.9, 0.9, 0.9, 1, 0.7, 0.8, 1.8, 0.6, 0.1, 0.5, 0.9, 1, 0.9, 1.9, 0.7, 0.7, 0.5, 1.3, 0.5, 1.4, 0.9, 0.8, 0.8, 0.5, 1, 1.5, 0.6, 0.9, 1.1, 0.5, 1.2, 0.7, 0.7, 0.9, 0.8, 0.6, 0.9, 1.1, 0.6, 1, 0.8, 0.7, 1.2, 1, 1.1, 1.1, 0.7, 1.9, 0.8, 0.9, 1.8, 0.4, 0.9, 1, 0.9, 1, 0.9, 1, 1.3, 0.8, 0.8, 0.2, 0.6, 0.9, 0.5, 0.5, 0.9, 0.5, 0.7, 1.1, 0.9, 0.9, 1.3, 0.6, 0.9, 1, 0.1, 0.8, 0.3, 2.1, 0.6, 0.6, 0.8, 0.9, 0.6, 1.8, 1.5, 1.6, 1.2, 0.9, 1.7, 0.9, 0.8, 2.2, 1.6, 0.7, 0.8, 0.8, 0.8, 1.4, 1.4, 0.8, 0.8, 1.4, 1.3, 0.2, 0.8, 0.9, 1.9, 0.2, 0.8, 0.9, 2.8, 0.9, 1.5, 1.5, 1.6, 0.9, 0.9, 0.6, 1.1, 0.9, 0.9, 0.5, 0.9, 0.3, 1.5, 0.7, 0.3, 0.9, 1.6, 0.9, 1, 0.9, 0.8, 2, 0.9, 0.9, 1.4, 1, 1.1, 0.6, 1.1, 0.4, 0.9, 0.9, 0.7, 1.5, 0.6, 2.3, 1, 0.9, 0.8, 1.8, 1.2, 1, 0.6, 0.7, 0.7, 1.1, 0.7, 2.5, 1.6, 1.8, 1.6, 1.2, 0.9, 0.9, 0.9, 1.5, 0.9, 1.3, 1, 0.9, 0.6, 1.3, 1.4, 0.9, 0.8, 1, 1.4, 1, 0.1, 0.6, 0.8, 0.6, 0.7, 0.2, 0.8, 0.9, 1.2, 2, 0.7, 0.7, 0.9, 1.7, 0.9, 0.8, 0.8, 0.8, 2.7, 0.9, 1.3, 0.9, 0.8, 0.8, 0.5, 1.7, 1.7, 0.2, 1.4, 0.7, 0.7, 0.9, 1.5, 0.9, 1.2, 0.9, 0.3, 0.9, 0.1, 0.1, 0.5, 1, 0.5, 1.3, 1.2, 1.5, 0.7, 0.7, 0.7, 0.4, 0.8, 0.8, 0.3, 0.5, 1.1, 1.1, 0.8, 1, 1.8, 1.3, 1, 1, 0.1, 1.1, 2.8, 1.6, 1.1, 1.8, 1.2, 1.4, 0.8, 0.3, 0.8, 1.5, 0.1, 1.2, 1.2, 0.9, 0.9, 0.9, 1.2, 0, 0, 0.1, 1.9, 1, 0.6, 0.7, 1.4, 1.9, 2.1, 0.8, 1.4, 1.4, 0.9, 0.5, 0.6, 0.9, 1, 1.4, 0.7, 1, 1.4, 1.1, 0.6, 1, 0.9, 0.7, 0.9, 0, 1, 1, 0.9, 0.9, 0.7, 2, 1, 1, 1.5, 0.7, 0.7, 0.9, 0.8, 2.1, 1.2, 0.8, 0.9, 0.6, 0.3, 0.8, 0.8, 0.9, 1.5, 2.1, 0.7, 1.4, 0.7, 1, 1, 0.8, 0.9, 1.1, 1.9, 2.1, 1.6, 2.1, 1.9, 1.9, 2.1, 0.9, 1.9, 0.8, 0.7, 0.4, 1, 1.6, 2, 0.8, 0.1, 1.8, 1.2, 0.9, 1.4, 2.9, 0.8, 0.9, 0.9, 0.9, 1, 2, 0.7, 0.4, 1.4, 1.7, 0.7, 0.7, 0.8, 0.8, 0.8, 0.8, 0.8, 0.4, 1.8, 0.9, 0.7, 0.7, 0.8, 0.9, 0.7, 0.9, 1.8, 0.9, 0.7, 0.6, 1.1, 0.9, 0.9, 0.9, 1.7, 1.4, 0.7, 0.9, 0.6, 0.6, 0.9, 0.5, 0.3, 0.6, 1.1, 0.1, 1.5, 0.1, 1, 1.5, 0.8, 0.6, 1.6, 0.9, 0.5, 0.6, 0.9, 1.3, 1]



mags = [0.7, 0.9, 1.3, 0.2, 0.2, 0.8, 0.6, 0.9, 1.3, 1.7, 1.7, 2, 0.7, 1, 0.7, 1.5, 0.9, 3.3, 1.5, 0.7, 0.9, 0.9, 0.9, 0.6, 0.5, 0.2, 0, 0.8, 0.6, 1.4, 2.4, 1.4, 2, 1.5, 0.8, 0.8, 2.4, 0.9, 1.7, 1.7, 0.6, 1.7, 1.5, 1.8, 1.2, 3.3, 0.8, 0.8, 1.3, 1.8, 0.9, 1.1, 0.6, 0.7, 0.7, 0.7, 1.2, 0.9, 0.9, 0.9, 0.9, 0.9, 1.1, 1.4, 0.3, 0.9, 2, 0.8, 1.8, 2, 0.9, 1.4, 0.9, 0.9, 1.5, 1.5, 1.8, 2.2, 1.4, 0.6, 1.5, 0.3, 2.4, 0.9, 2, 0.3, 1, 1.3, 1.4, 1.5, 1, 1.3, 1.1, 1.2, 0.8, 0.9, 1.4, 1.7, 1.1, 1.3, 2.3, 0.9, 0.9, 0.9, 0.9, 0.7, 1.3, 1.5, 0.9, 0.2, 1.8, 1.9, 0.9, 1.3, 0.9, 1.8, 0.1, 0.9, 0.9, 0.9, 1.6, 0.6, 0.8, 1, 0.8, 0.7, 0.9, 0.8, 1.7, 1, 1.2, 1.1, 0.8, 0.5, 0.2, 0.9, 0.8, 0.8, 0.8, 0.8, 1.1, 0.8, 0.8, 2, 0.8, 0.7, 1.1, 0.9, 0.8, 0.8, 0.7, 0.9, 0.8, 1.1, 1.4, 0, 1.1, 0.1, 0.1, 0.8, 0.8, 1.3, 1.2, 0.7, 0.9, 0.8, 0.8, 1.1, 0.8, 1.6, 0.8, 0.9, 1.6, 1.3, 0.9, 0.6, 0.8, 0.9, 0.6, 1.4, 1.7, 1.7, 1.8, 1, 0.9, 1.5, 0.9, 1.7, 1.3, 1.6, 0.8, 0.6, 1.4, 1.1, 0.9, 1.2, 1.3, 1.9, 1, 0.8, 0.7, 0.7, 0.6, 0.8, 1.4, 1, 0.4, 1.4, 1.8, 0.3, 3.3, 1.6, 0.5, 1.1, 0.7, 0.8, 0.9, 1.1, 1.3, 0.7, 0.8, 0.9, 1.5, 0.9, 1.1, 1.4, 0.4, 0, 0.7, 0.2, 0.7, 0.3, 2.1, 1.6, 0.4, 1.5, 1.2, 0.7, 0.5, 0.5, 1.2, 1, 1.1, 1.5, 1.1, 0.9, 1.5, 0.6, 0, 1.6, 0.9, 1.5, 0.8, 1.8, 0.9, 0.7, 1, 0.9, 0.3, 0.9, 0.7, 0.8, 0.2, 0.8, 0.8, 0.9, 0.8, 0.8, 0.8, 1.3, 0.4, 0.8, 1.1, 1.9, 1.7, 0.5, 1.3, 1.8, 0.5, 0.8, 1, 1.7, 0.8, 1.1, 2.1, 2.1, 1.4, 1.4, 1.5, 1.5, 0.1, 0.6, 1.8, 1.1, 0.9, 1.7, 0.9, 2.4, 1.7, 1.2, 0.9, 1, 0.7, 0.4, 0.9, 3.3, 0.8, 0.8, 0.9, 1.8, 0.8, 0.7, 1, 0.8, 0.9, 1, 1.7, 0.2, 0.9, 0.9, 1.3, 0.7, 0.9, 1.1, 0.4, 0.5, 1.9, 0.6, 1.5, 1.5, 1.3, 1.3, 1.2, 0.8, 0.6, 0.7, 0.8, 0.3, 1.5, 0.7, 0.6, 0.9, 0.7, 0.8, 2, 1.1, 0.1, 1.7, 0.8, 1.7, 0.6, 0.5, 2.8, 0.3, 0.8, 1.5, 1.8, 0.3, 0.6, 1.4, 1.3, 0.8, 0.9, 0.6, 0.9, 1.4, 1, 0.8, 1.3, 0.5, 1.7, 1, 1, 0.8, 0.8, 0.8, 1, 0.6, 0.6, 1, 0.8, 0.4, 0.9, 0.5, 0.6, 0.5, 0.3, 1.9, 1, 0.9, 0.7, 1.5, 0.7, 0.9, 1.7, 0.7, 0.9, 0.9, 0.8, 0.6, 0.8, 1.5, 2.7, 0.5, 1.2, 0.6, 0.9, 0, 1, 0.9, 0.7, 1, 1, 1.4, 1.5, 0.9, 1.3, 0.7, 1.6, 1.4, 0.8, 0.8, 1.5, 0.6, 0.3, 0.7, 1.9, 1, 2.1, 0.8, 2.7, 0.3, 1.2, 1.4, 0, 1, 0.9, 1.8, 0.7, 1.1, 0.9, 0.8, 2, 1.4, 1.2, 0.9, 0.1, 0.8, 1, 1.5, 2.3, 1.6, 1.1, 1.2, 0.8, 2, 0.5, 0.5, 0.6, 0, 0.9, 1.5, 0.8, 0.7, 0.9, 1, 1, 0.9, 0.9, 1.8, 0.2, 0.7, 0.7, 0.9, 0, 0, 0, 0, 0.7, 0.7, 0, 0, 0, 0, 0, 0.7, 0, 1.8, 0, 0.5, 2.3, 1.1, 0.8, 0.7, 1, 1.8, 0.9, 0.9, 0.7, 0.7,0.7, 0.8, 0.8, 0.9, 0.7, 0.9, 0.7, 0.8, 0.9, 0.9, 0.9, 0.8, 1, 0.7, 1.7, 1, 1, 0.8, 1.3, 0.8, 1.6, 0.9, 1.5, 1.5, 1.3, 0.9, 0.7, 1.7, 2.9, 0.8, 0.8, 1.2, 0.5, 0.8, 0.8, 0.8, 1.4, 1.6, 2.7, 1.1, 0.9, 1, 1.8, 1.7, 1.6, 1.5, 1.8, 0.5, 0.9, 0.6, 1.3, 1.2, 0.9, 1.4, 1.2, 0.9, 0.8, 1.2, 1, 0.9, 1, 0.9, 0.8, 0.9, 1.1, 0.8, 0.9, 1, 0.2, 1.3, 1.3, 1.3, 0.4, 1.8, 1.6, 1.7, 1.3, 0.7, 1.3, 0.8, 1.6, 0.9, 0.8, 0.2, 0.7, 2, 1.2, 0.7, 1.6, 0.9, 0.8, 0.6, 0.9, 0.3, 1, 0.6, 0.9, 0.9, 1, 0.9, 0.1, 0.7, 1.5, 1.3, 0.7, 0.7, 0.9, 0.9, 2.3, 0.9, 1.6, 0.7, 1, 1.7, 0.7, 0.9, 0.9, 0.9, 1, 0.7, 0.8, 1.8, 0.6, 0.1, 0.5, 0.9, 1, 0.9, 1.9, 0.7, 0.7, 0.5, 1.3, 0.5, 1.4, 0.9, 0.8, 0.8, 0.5, 1, 1.5, 0.6, 0.9, 1.1, 0.5, 1.2, 0.7, 0.7, 0.9, 0.8, 0.6, 0.9, 1.1, 0.6, 1, 0.8, 0.7, 1.2, 1, 1.1, 1.1, 0.7, 1.9, 0.8, 0.9, 1.8, 0.4, 0.9, 1, 0.9, 1, 0.9, 1, 1.3, 0.8, 0.8, 0.2, 0.6, 0.9, 0.5, 0.5, 0.9, 0.5, 0.7, 1.1, 0.9, 0.9, 1.3, 0.6, 0.9, 1, 0.1, 0.8, 0.3, 2.1, 0.6, 0.6, 0.8, 0.9, 0.6, 1.8, 1.5, 1.6, 1.2, 0.9, 1.7, 0.9, 0.8, 2.2, 1.6, 0.7, 0.8, 0.8, 0.8, 1.4, 1.4, 0.8, 0.8, 1.4, 1.3, 0.2, 0.8, 0.9, 1.9, 0.2, 0.8, 0.9, 2.8, 0.9, 1.5, 1.5, 1.6, 0.9, 0.9, 0.6, 1.1, 0.9, 0.9, 0.5, 0.9, 0.3, 1.5, 0.7, 0.3, 0.9, 1.6, 0.9, 1, 0.9, 0.8, 2, 0.9, 0.9, 1.4, 1, 1.1, 0.6, 1.1, 0.4, 0.9, 0.9, 0.7, 1.5, 0.6, 2.3, 1, 0.9, 0.8, 1.8, 1.2, 1, 0.6, 0.7, 0.7, 1.1, 0.7, 2.5, 1.6, 1.8, 1.6, 1.2, 0.9, 0.9, 0.9, 1.5, 0.9, 1.3, 1, 0.9, 0.6, 1.3, 1.4, 0.9, 0.8, 1, 1.4, 1, 0.1, 0.6, 0.8, 0.6, 0.7, 0.2, 0.8, 0.9, 1.2, 2, 0.7, 0.7, 0.9, 1.7, 0.9, 0.8, 0.8, 0.8, 2.7, 0.9, 1.3, 0.9, 0.8, 0.8, 0.5, 1.7, 1.7, 0.2, 1.4, 0.7, 0.7, 0.9, 1.5, 0.9, 1.2, 0.9, 0.3, 0.9, 0.1, 0.1, 0.5, 1, 0.5, 1.3, 1.2, 1.5, 0.7, 0.7, 0.7, 0.4, 0.8, 0.8, 0.3, 0.5, 1.1, 1.1, 0.8, 1, 1.8, 1.3, 1, 1, 0.1, 1.1, 2.8, 1.6, 1.1, 1.8, 1.2, 1.4, 0.8, 0.3, 0.8, 1.5, 0.1, 1.2, 1.2, 0.9, 0.9, 0.9, 1.2, 0, 0, 0.1, 1.9, 1, 0.6, 0.7, 1.4, 1.9, 2.1, 0.8, 1.4, 1.4, 0.9, 0.5, 0.6, 0.9, 1, 1.4, 0.7, 1, 1.4, 1.1, 0.6, 1, 0.9, 0.7, 0.9, 0, 1, 1, 0.9, 0.9, 0.7, 2, 1, 1, 1.5, 0.7, 0.7, 0.9, 0.8, 2.1, 1.2, 0.8, 0.9, 0.6, 0.3, 0.8, 0.8, 0.9, 1.5, 2.1, 0.7, 1.4, 0.7, 1, 1, 0.8, 0.9, 1.1, 1.9, 2.1, 1.6, 2.1, 1.9, 1.9, 2.1, 0.9, 1.9, 0.8, 0.7, 0.4, 1, 1.6, 2, 0.8, 0.1, 1.8, 1.2, 0.9, 1.4, 2.9, 0.8, 0.9, 0.9, 0.9, 1, 2, 0.7, 0.4, 1.4, 1.7, 0.7, 0.7, 0.8, 0.8, 0.8, 0.8, 0.8, 0.4, 1.8, 0.9, 0.7, 0.7, 0.8, 0.9, 0.7, 0.9, 1.8, 0.9, 0.7, 0.6, 1.1, 0.9, 0.9, 0.9, 1.7, 1.4, 0.7, 0.9, 0.6, 0.6, 0.9, 0.5, 0.3, 0.6, 1.1, 0.1, 1.5, 0.1, 1, 1.5, 0.8, 0.6, 1.6, 0.9, 0.5, 0.6, 0.9, 1.3, 1]


plot_points = []
start = 0
end = 100

while True:
    # print
    total = 0
    try:
        for x in range(start,end):
            total += (mags[x]*scores[x])
        plot_points.append(total/100)
        start +=100
        end += 100
    except:
        break

print (plot_points)
# print (len(mags))
#
# with open("wtf_cloud_plotpoints.txt","w") as f:
#     json.dump(plot_points,f)
#
# print ([x for x in range(1,len(mags))])
