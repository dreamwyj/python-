import urllib.request
import gevent
from gevent import monkey

monkey.patch_all()

def downloader(img_name, img_url):

    req = urllib.request.urlopen(img_url)

    img_content = req.read()

    with open(img_name,"wb") as f:
        f.write(img_content)


def main():
    gevent.joinall([
            gevent.spawn(downloader,"",""),

            gevent.spawn(downloader,"","")
        ])

if __name__ == "__main__":
    main()
