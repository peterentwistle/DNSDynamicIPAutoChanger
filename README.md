DNSDynamicIPAutoChanger
==========

DNSDynamicIPAutoChanger changes the IP address of you dnsdynamic.org domain using crontab.

I wrote this script to be used on my Raspberry Pi webserver, so the IP address would be changed dynamically. 

Requirements
==========
Make sure you make an account on [dnsdynamic.org](https://www.dnsdynamic.org/signup.php) first.
* Python 2.7
* [Requests](http://www.python-requests.org)
* [Beautiful Soup 4](http://www.crummy.com/software/BeautifulSoup/bs4/doc/)
* Crontab

Installation
==========
    $ git clone https://github.com/peterentwistle/DNSDynamicIPAutoChanger.git
    $ mv DNSDynamicIPAutoChanger dns
    $ sudo pip install requests
    $ sudo pip install beautifulsoup4
    $ nano dns/dns.py

```python
Change the following lines to your dnsdynamic details:

username = 'youremail@example.com'
password = 'yourPassword'
hostname = 'yourDnsDynamicSubDomain'
```
    $ crontab -e
    
    Add the following line at the bottom of the file and change the path to
    the location that you downloaded the script to:
    
    */5 * * * * python /path/to/dns/dns.py
    
    This line tells cron to run the script every 5 minutes.
    Feel free to change how often the script is ran.

That's all you need to do, but to confirm that everything is running correctly go into the dns directory and see if an `ip` file has been created after 5 minutes. If you open the `ip` file with a text editor you should see an ip address like: `127.0.0.1` (but with your external IP instead) this means that the script is running correctly.
