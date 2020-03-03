#!/bin/bash
source /home/gordon/p3env/bin/activate && cd /home/gordon/p3env/alice/alice/spiders && python standalone_tools.py mass_mail_ahap_introduction >> /home/gordon/p3env/alice/alice/spiders/logfiles/mass_mail_ahap_introduction_log_$(date +\%Y\%m\%d).logfile 2>&1
