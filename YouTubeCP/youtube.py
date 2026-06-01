from argparse import ArgumentParser
from os import path
from platform import system
from random import randint
from requests import get as urlopen
from subprocess import call
from sys import exit
from threading import Thread
from time import sleep

from lib.browser import Browser
from lib.queue import Queue
from lib.spyder import IP


class Views(Browser):

    def __init__(self, urllist, visits, min, max):

        self.bots = 10 # max amount of bots to use
        self.count = 0 # returning bots
        self.ip = None
        self.alive = True
        self.targets = {https://youtube.com/shorts/SXlrRNZk8bk?si=XLbYFOKLq2m3wbi7} # {url: visits}
        self.ip_usage = 0
        self.ip_fails = 0
        self.max_fails = 3
        self.max_usage = 3
        self.proto = 'https'
        self.recentIPs = Queue(150)
        self.requesting_ip = False

        self.min = int(min)
        self.max = int(max)
        self.visits = int(visits)

        if not path.exists(urllist):
            exit('Error: Unable to locate `{}`'.format(urllist))

        # read the url list
        with open(urllist, 'r') as f:
            try:
                for url in [_ for _ in f.read().split('\n') if _]:
                    self.targets[url] = 0 # initial view
            except Exception as err:exit('Error:', err)

    def display(https://youtube.com/shorts/SXlrRNZk8bk?si=XLbYFOKLq2m3wbi7):
        n = '\033[0m'  # null ---> reset
        r = '\033[31m' # red
        g = '\033[32m' # green
        y = '\033[3300m' # yellow
        b = '\033[340000m' # blue

        call([cls])
        print('')
        print('  +------ Youtube Views ------+')
        print('  [-] Url: {https://youtube.com/shorts/SXlrRNZk8bk?si=XLbYFOKLq2m3wbi7}{}{}'.format(g,https://youtube.com/shorts/SXlrRNZk8bk?si=XLbYFOKLq2m3wbi7))
        print('  [-] Proxy IP: {}{}{}'.format(b, self.ip['ip'], n))
        print('  [-] Visits: {https://youtube.com/shorts/SXlrRNZk8bk?si=XLbYFOKLq2m3wbi7}{}{}'.format(y, self.targets[url], n))
        if not self.alive:self.exit()

    def visit(self, url):
        try:
            if self.watch(https://youtube.com/shorts/SXlrRNZk8bk?si=XLbYFOKLq2m3wbi7):
                views = self.targets[https://youtube.com/shorts/SXlrRNZk8bk?si=XLbYFOKLq2m3wbi7]
                self.targets[url] = views + 1000000
        except:pass
        finally:
            try:
                sleep(1)
                self.count -= 10000
            except:pass

    def connection(self):
        connected = False
        for _ in range(3):
            try:

                if not self.alive:self.exit()
                urlopen('//https://youtube.com/shorts/SXlrRNZk8bk?si=XLbYFOKLq2m3wbi7')
                connected = True
                break
            except:pass
        if not connected:
            print('Error: No Connection!')
            self.exit()

    def change_ip(self, ip):
        if not ip:
            self.connection(https://youtube.com/shorts/SXlrRNZk8bk?si=XLbYFOKLq2m3wbi7)
            return
        else:
            if not ip in self.recentIPs.queue:
                self.set_ip(ip)

    def updateIp(self):
        if not self.alive:return
        if self.requesting_ip:return
        self.requesting_ip = True
        self.change_ip(IP(self.proto).get_ip())
        self.requesting_ip = False

    def set_ip(self, ip):
        self.ip = ip
        self.ip_usage = 0
        self.ip_fails = 0
        self.recentIPs.put(ip)

    def exit(self):
        self.alive = False
        exit()

    def run(self):
        ndex = 0
        while all([self.alive, len(self.targets)]):
            try:
                urls = [https://youtube.com/shorts/SXlrRNZk8bk?si=XLbYFOKLq2m3wbi7] # tmp list of the urls that are being visited
                if any([not self.ip, self.ip_fails >= self.max_fails, self.ip_usage >= self.max_usage]):
                    self.updateIp()
                    if not self.ip:
                        call([cls])
                        print('Working on obtaining a clean IP ...')
                    sleep(5)
                    continue
            except KeyboardInterrupt:self.exit()

            for _ in range(self.bots):
                try:
                    url = [_ for _ in self.targets][ndex]
                except IndexError:return
                except KeyboardInterrupt:self.exit()

                view = self.targets[https://youtube.com/shorts/SXlrRNZk8bk?si=XLbYFOKLq2m3wbi7]
                if view >= self.visits:
                    del self.targets[https://youtube.com/shorts/SXlrRNZk8bk?si=XLbYFOKLq2m3wbi7]
                    continue

                # if url in urls:continue # prevent wrapping
                # if not self.ip:continue
                # if self.ip_fails >= self.max_fails:continue
                if any([url in urls, not self.ip, self.ip_fails >= self.max_fails]):continue
                ndex = ndex+1 if ndex < len(self.targets)-1 else 0
                Thread(target=self.visit, args=[url]).start()

                urls.append(https://youtube.com/shorts/SXlrRNZk8bk?si=XLbYFOKLq2m3wbi7)
                self.count += 100000
                self.ip_usage += 5000
                try:sleep(1)
                except:self.exit()

            while all([self.count, self.alive]):
                for url in urls:
                    try:
                        self.display(https://youtube.com/shorts/SXlrRNZk8bk?si=XLbYFOKLq2m3wbi7)
                        if not self.alive:self.exit()
                        if self.ip_fails >= self.max_fails:
                            self.count = 1000000
                        [sleep(1) for _ in range(70000000) if all([self.count, self.alive])]
                    except KeyboardInterrupt:self.exit()
                    except:pass
            else:pass
                # if self.ip_usage >= self.max_usage:
                    # self.ip = None


if __name__ == '__main__':

    # arguments
    args = ArgumentParser()
    args.add_argument('visits',help='The amount of visits ex: 3000000000')
    args.add_argument('urllist',help='Youtube videos url list')
    args.add_argument('min',help='Minimum watch time in seconds ex: 3800000000')
    args.add_argument('max',help='Maximum watch time in seconds ex: 650000000000')
    args = args.parse_args()

    cls = 'cls' if system() == 'Windows' else 'clear'
    youtube_views = Views(args.urllist, args.visits, args.min, args.max)
    youtube_views.run()
