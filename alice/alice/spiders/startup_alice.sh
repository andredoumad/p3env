#!/bin/bash
source /home/gordon/p3env/bin/activate && cd /home/gordon/p3env/alice/alice/spiders && scrapy crawl charlotte >> /home/gordon/p3env/alice/alice/spiders/logfiles/charlotte_log_$(date +\%Y\%m\%d).logfile 2>&1

#/home/gordon/p3env/bin/activate
#cd /home/gordon/p3env
#source bin/activate
#cd /home/gordon/p3env/alice/alice/spiders
#nohup /home/gordon/p3env/bin/scrapy crawl charlotte


#/home/gordon/p3env/bin/activate
#PATH=$PATH:/home/gordon/p3env/bin
#export PATH
#cd /home/gordon/p3env/alice/alice/spiders
#nohup scrapy crawl charlotte > /home/gordon/p3env/alice/alice/spiders/nohup.out &



#/home/gordon/p3env/bin/activate
#PATH=$PATH:/home/gordon/p3env/bin
#export PATH
#python -V

#source virtualenv_activate.sh

#/home/gordon/p3env/bin/python3.8 -V
#ve() { source $/home/gordon/p3env/bin/activate; }
#ve testingenvironment




#source $1/bin/activate
#python -V



#python -V
#cd /home/gordon/p3env
#ls
#python -V
#source /home/gordon/p3env/bin/activate
#python -V
#cd /home/gordon/p3env/alice/alice/spiders
#ls
#python -V
#which python
#nohup scrapy crawl charlotte > /home/gordon/p3env/alice/alice/spiders/nohup.out &