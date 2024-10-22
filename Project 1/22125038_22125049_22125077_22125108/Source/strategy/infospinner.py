import time
import threading
import sys
from problem.searchnode import SearchNode
import tracemalloc
from enum import Enum
from colorama import init, Fore, Style

init()

class SpinnerStopCode(Enum):
    INTERRUPTED = 1
    FINISHED = 2
    TLE = 3
    MLE = 4
    ERROR = 5

class InfoSpinner:

    def __init__(self):
        self.running = False
        self.thread = None
        self.elapsed_time = 0  # Store elapsed time
        self.start_time = 0

    def start(self, start_time):
        self.running = True
        self.start_time = start_time
        self.thread = threading.Thread(target=self._spin)
        self.thread.start()
    
    def elapsed_info(self, color1, color2 = None, color3 = None):
        _, peak = tracemalloc.get_traced_memory()
        elapsed_time = time.time() - self.start_time
        if color2 is None: color2 = color1
        if color3 is None: color3 = color2

        string = ""
        string += f"Elapsed: {color1}{elapsed_time:.2f} sec{Style.RESET_ALL}"
        string += f", Generated: {color2}{SearchNode.node_count} nodes{Style.RESET_ALL}"
        string += f", Memory used: {color3}{peak / 10**6:.2f} MB{Style.RESET_ALL}"
        string += " " * 50
        return string

    def _spin(self):
        spinner_chars = ['|', '/', '-', '\\']
        i = 0

        try:
            while self.running:
                print(f"{spinner_chars[i]} {self.elapsed_info(Fore.YELLOW)}\r", end="")
                i = (i + 1) % len(spinner_chars)
                time.sleep(0.1)  # Control speed of spinner
        except KeyboardInterrupt:
            self.stop()

    def stop(self, stop_code: SpinnerStopCode = SpinnerStopCode.FINISHED):
        self.running = False
        if self.thread:
            self.thread.join()

        if stop_code == SpinnerStopCode.INTERRUPTED:
            print(f"{self.elapsed_info(Fore.RED)}\n{Fore.RED}User interrupted.{Style.RESET_ALL}")
        elif stop_code == SpinnerStopCode.FINISHED:
            print(f"{self.elapsed_info(Fore.GREEN)}\n{Fore.GREEN}Search finished.{Style.RESET_ALL}")
        elif stop_code == SpinnerStopCode.TLE:
            print(f"{self.elapsed_info(Fore.MAGENTA, Fore.RED)}\n{Fore.RED}Time limit exceeded.{Style.RESET_ALL}")
        elif stop_code == SpinnerStopCode.MLE:
            print(f"{self.elapsed_info(Fore.RED, Fore.RED, Fore.MAGENTA)}\n{Fore.RED}Memory limit exceeded.{Style.RESET_ALL}")
        elif stop_code == SpinnerStopCode.ERROR:
            print(f"{self.elapsed_info(Fore.RED)}\n{Fore.RED}Error occurred.{Style.RESET_ALL}")