import os
import zipfile
import requests

# ১. ড্রাইভ ফাইল আইডি এবং আপনার তথ্য
FILE_ID = '1MW4Lx_FFEBYWPfM8McXHdiORvYkHLpDS'
DOWNLOAD_URL = f'https://drive.google.com/file/d/1MW4Lx_FFEBYWPfM8McXHdiORvYkHLpDS/view?usp=drivesdk'

def main():
    # ২. ফাইল ডাউনলোড করা
    print("গুগল ড্রাইভ থেকে ডাউনলোড হচ্ছে...")
    r = requests.get(DOWNLOAD_URL, stream=True)
    with open(ZIP_NAME, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
    
    # ৩. আনজিপ করা
    print("আনজিপ করা হচ্ছে...")
    with zipfile.ZipFile(ZIP_NAME, 'r') as zip_ref:
        # বর্তমান ফোল্ডারেই সব ফাইল বের করা হবে
        zip_ref.extractall(".")
    
    # ৪. জিপ ফাইলটি মুছে ফেলা (পরিষ্কার রাখার জন্য)
    os.remove(ZIP_NAME)
    print("কাজ শেষ! এখন ফাইলগুলো গিটহাবে পুশ করার জন্য তৈরি।")

if __name__ == "__main__":
    main()
