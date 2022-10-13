import concurrent.futures
import requests
import sys
import time
from http.cookies import SimpleCookie

URLS = []

file = sys.argv[1] #passing file through args
raw_cookie = str(sys.argv[2]) #passing cooking through arguments
cookie = SimpleCookie()
cookie.load(raw_cookie)

cookies = {}
for k, v in cookie.items():
    cookies[k] = v.value

requests.packages.urllib3.disable_warnings()

start = time.perf_counter()


def file_input():
    with open(file) as f:
        for line in f:
            line.strip()
            URLS.append(line)
file_input()


# Retrieve a single page and report the URL and contents
def get_request(target_url):
    res = requests.get(target_url, cookies=cookies, verify=False,allow_redirects=True)
    code = str(res.status_code)
    print(f"{target_url.strip()} {code}")



# Post request with custom data
def post_request(target):
    target_url = str(target).strip()
    res = requests.post(target_url, cookies=cookies, data={"key": "value"}, verify=False)
    code = res.status_code
    print(f"{target} {code}")


def workers(function):
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        future_to_url = {executor.submit(function, url): url for url in URLS}
        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]
            try:
                data = future.result()
            except Exception as exc:
                print('%r generated an exception: %s' % (url, exc))


workers(get_request)

end = time.perf_counter() - start

print(f'Process finished in {end:.2f}s !')
