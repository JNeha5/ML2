import time
import random
import hashlib
import csv

API_KEY = "C91B000085C07407E8C01B000089305E8BC75FC9C36A0C68"

print("Starting virtual sensor simulation using API key as data source...")

# Create CSV file to log simulated data
with open("ml_sensor_data.csv", "w", newline="") as csvfile:
    fieldnames = ["timestamp", "sensor1", "sensor2", "sensor3"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    try:
        while True:
            # Use the API key to generate deterministic numbers
            hash_obj = hashlib.sha256((API_KEY + str(time.time())).encode())
            hash_int = int(hash_obj.hexdigest(), 16)

            # Simulate 3 sensor readings from the hash
            sensor1 = hash_int % 100          # 0–99
            sensor2 = (hash_int // 100) % 100 # 0–99
            sensor3 = (hash_int // 10000) % 100

            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

            # Print sensor readings
            print(f"{timestamp} | Sensor1: {sensor1}, Sensor2: {sensor2}, Sensor3: {sensor3}")

            # Save to CSV
            writer.writerow({
                "timestamp": timestamp,
                "sensor1": sensor1,
                "sensor2": sensor2,
                "sensor3": sensor3
            })

            time.sleep(1)  # 1-second interval

    except KeyboardInterrupt:
        print("\nSimulation stopped by user.")
