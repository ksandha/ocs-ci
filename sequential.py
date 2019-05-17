import re
import os
import subprocess
import datetime
for i in range(1, 120):
    fp = open(r'pvc.yaml', 'r')
    str1 = 'claim' + str(i)
    replace_data = fp.read().replace('claim', str1)
    fp.seek(0, 0)
    fw = open(r'pvc.yaml', 'w')
    fw.write(replace_data)
    fw.seek(0, 0)
    s = datetime.datetime.now()
    os.system('oc create -f pvc.yaml')
    while True:
        str2 = subprocess.check_output("oc get pvc | grep '%s'" % str1, shell=True)
        if re.search(r'Bound', str2):
            break
    e = datetime.datetime.now()
    f = str(e-s)
    str3 = '\t'.join([str1, f])
    fs = open(r'pvc_create_time_new', 'a')
    fs.write(str3)
    fs.write('\n')
    fp = open(r'pvc.yaml', 'r')
    str1 = 'claim' + str(i)
    replace_data = fp.read().replace(str1, 'claim')
    fp.seek(0, 0)
    fw = open(r'pvc.yaml', 'w')
    fw.write(replace_data)
    fw.seek(0, 0)

