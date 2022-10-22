
import speedtest

def simple_speedtest():
    """Run a simple internet speedtest"""
    test = speedtest.Speedtest()
    download_speedtest = test.download()/1000000
    upload_speedtest = test.upload()/1000000
    download_speed = str(round(download_speedtest,2))
    upload_speed = str(round(upload_speedtest,2))
    print("Download speed: ", download_speed, "Mbit/s")
    print("Upload speed: ", upload_speed, "Mbps")
    return

simple_speedtest()