from google_images_download import google_images_download

response = google_images_download.googleimagesdownload()

search_queries=["sweet","sweets","indian sweet"]

def downloadimg(query):
  args={"keywords":query,"limit":100,"--chromedriver":"/usr/lib/chromium-browser"}
  response.download(args)

for i in search_queries:
  downloadimg(i)
  
