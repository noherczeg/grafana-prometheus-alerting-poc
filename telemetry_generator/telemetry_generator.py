import time
import random
import requests

PROMETHEUS_PUSHGATEWAY = "http://pushgateway:9091/metrics/job/telemetry_generator"

def generate_data():
    metrics = ["cpu_usage", "memory_usage", "disk_usage"]
    host = "host1"

    while True:
        metric_name = random.choice(metrics)
        value = random.uniform(0, 100)
        timestamp = int(time.time())

        # Push data to Prometheus Pushgateway
        payload = f'{metric_name}{{host="{host}"}} {value}\n'
        response = requests.post(PROMETHEUS_PUSHGATEWAY, data=payload)

        print(f"Pushed data: {payload.strip()} with status: {response.status_code}")

        time.sleep(1)

if __name__ == "__main__":
    generate_data()
