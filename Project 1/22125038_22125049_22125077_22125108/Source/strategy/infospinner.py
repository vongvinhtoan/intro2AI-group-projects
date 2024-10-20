import time
import threading
import sys
from problem.searchnode import SearchNode
import tracemalloc

class InfoSpinner:
    def __init__(self):
        self.running = False
        self.thread = None
        self.elapsed_time = 0  # Store elapsed time

    def start(self):
        self.running = True
        self.elapsed_time = 0  # Reset timer
        self.start_time = time.time()
        self.thread = threading.Thread(target=self._spin)
        self.thread.start()

    def _spin(self):
        spinner_chars = ['|', '/', '-', '\\']  # Characters to show spinning effect
        i = 0

        try:
            while self.running:
                self.elapsed_time = time.time() - self.start_time
                _, peak = tracemalloc.get_traced_memory()
                sys.stdout.write(f"{spinner_chars[i % len(spinner_chars)]} Elapsed: \033[92m{self.elapsed_time:.2f} sec\033[0m, Generated: \033[92m{SearchNode.node_count} nodes\033[0m, Memory used: \033[92m{peak / 10**6:.2f} MB\033[0m" + " " * 10 + "\r")
                sys.stdout.flush()
                i += 1
                time.sleep(0.1)  # Control speed of spinner
        except KeyboardInterrupt:
            self.stop()

    def stop(self):
        self.running = False
        if self.thread:
            self.thread.join()
        self.elapsed_time = time.time() - self.start_time
        _, peak = tracemalloc.get_traced_memory()
        print(f"\rFinished algorithm in \033[92m{self.elapsed_time:.2f} sec\033[0m, Generated: \033[92m{SearchNode.node_count} nodes\033[0m, Memory used: \033[92m{peak / 10**6:.2f} MB\033[0m")