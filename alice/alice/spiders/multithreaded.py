
# multithreaded.py

import threading
import time
from queue import Queue
import requests

def make_request(url):
    """Makes a web request, prints the thread name, URL, and 
    response code.
    """
    resp = requests.get(url)
    with print_lock:
        print("Thread name: {}".format(threading.current_thread().name))
        print("Url: {}".format(url))
        print("Response code: {}\n".format(resp.status_code))

def manage_queue():
    """Manages the url_queue and calls the make request function"""
    while True:

        # Stores the URL and removes it from the queue so no 
        # other threads will use it. 
        current_url = url_queue.get()

        # Calls the make_request function
        make_request(current_url)

        # Tells the queue that the processing on the task is complete.
        url_queue.task_done()

if __name__ == '__main__':

    # Set the number of threads.
    number_of_threads = 5
    
    # Needed to safely print in mult-threaded programs.
    # https://stackoverflow.com/questions/40356200/python-printing-in-multiple-threads
    print_lock = threading.Lock()
    
    # Initializes the queue that all threads will pull from.
    url_queue = Queue()

    # The list of URLs that will go into the queue.
    urls = ["https://duckduckgo.com/"] * 5

    # Start the threads.
    for i in range(number_of_threads):

        # Send the threads to the function that manages the queue.
        t = threading.Thread(target=manage_queue)

        # Makes the thread a daemon so it exits when the program finishes.
        t.daemon = True
        t.start()
    
    start = time.time()

    # Puts the URLs in the queue
    for current_url in urls:
        url_queue.put(current_url)

    # Wait until all threads have finished before continuing the program.
    url_queue.join()

    print("Execution time = {0:.5f}".format(time.time() - start))