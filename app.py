import time
import numpy as np
from datetime import datetime

while True:
    # Create random array using numpy
    random_array = np.random.randint(1, 100, 5)
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{current_time}] Hello from Docker! Random numbers: {random_array}")
    time.sleep(5)
