#!/bin/bash
source /home/gordon/p3env/bin/activate && cd /home/gordon/p3env/alice/alice/spiders && python standalone_tools.py harvest_email_heap_full_using_csv_triggers_filters >> /home/gordon/p3env/alice/alice/spiders/logfiles/harvest_email_using_filters_log_$(date +\%Y\%m\%d).logfile 2>&1
