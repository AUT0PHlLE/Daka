# Dakav1_Modified.py

import json
import time
import threading

class Dakav1:
    def __init__(self):
        self.current_execution = 0
        self.is_running = False
        self.progress = 0
        self.total_tasks = 0
        self.delay_range = (0, 2)
        self.current_file = 'Current.json'

    def set_batch_feature(self, total_tasks):
        self.total_tasks = total_tasks
        self.progress = 0

    def track_progress(self):
        while self.is_running:
            print(f"Current execution: {self.current_execution}, Progress: {self.progress}/{self.total_tasks}")
            time.sleep(1)

    def set_delay_range(self, min_delay, max_delay):
        self.delay_range = (min_delay, max_delay)

    def execute_tasks(self):
        self.is_running = True
        threading.Thread(target=self.track_progress).start()

        for i in range(self.total_tasks):
            self.current_execution = i + 1
            self.progress += 1
            delay = random.uniform(*self.delay_range)
            time.sleep(delay)  # Simulates task execution
            self.save_current_execution()

        self.is_running = False

    def save_current_execution(self):
        data = {'current_execution': self.current_execution}
        with open(self.current_file, 'w') as f:
            json.dump(data, f)

    def cancel_execution(self):
        self.is_running = False
        print('Execution canceled.')

# Example usage
if __name__ == '__main__':
    dakav1 = Dakav1()
    dakav1.set_batch_feature(5)  # Set to execute 5 tasks
    dakav1.set_delay_range(1, 3)  # Set delay range between 1 to 3 seconds
    dakav1.execute_tasks()