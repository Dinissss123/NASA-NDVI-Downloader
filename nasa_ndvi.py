import requests, time
url = "https://api.nasa.gov/planetary/apod"
params = {"api_key": "MTaLqDj1GKJoojiNfIOj9HApQHs2OTfCbSCV7DDv"}
t0 = time.time()
try:
    r = requests.get(url, params=params, timeout=30)
    print("status:", r.status_code, "elapsed:", time.time()-t0)
    print("headers:", r.headers.get("Content-Type"))
    print("text (first 300 chars):", r.text[:300])
except Exception as e:
    print("ERROR:", e)