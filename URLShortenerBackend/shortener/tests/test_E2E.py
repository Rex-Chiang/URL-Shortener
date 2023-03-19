from concurrent import futures
import requests

def get_resource(long_url):
    return requests.post("http://0.0.0.0:8000/api/shorten", {"long_url": long_url})

def main():
    with futures.ThreadPoolExecutor(max_workers = 3) as executor:
        for _ in range(3):
            urls = ["https://www.google.1.com",
                    "https://www.google.2.com",
                    "https://www.google.3.com",
                    "https://www.google.4.com",
                    "https://www.google.5.com",
                    "https://www.google.6.com",
                    "https://www.google.7.com",
                    "https://www.google.8.com",
                    "https://www.google.9.com",
                    ] * 3

            results = executor.map(get_resource, urls)

            for i, res in enumerate(results):
                print(i, res)

if __name__ == "__main__":
    main()