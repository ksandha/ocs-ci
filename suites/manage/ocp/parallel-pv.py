
import os
for i in range(1, 100):
    fp = open(r'pvc.yaml', 'r')
    str1 = 'claim' + str(i)
    replace_data = fp.read().replace('claim', str1)
    fp.seek(0,0)
    fw = open(r'pvc.yaml', 'w')
    fw.write(replace_data)
    fw.seek(0,0)
    os.system('oc create -f pvc.yaml')
    fp = open(r'pvc.yaml', 'r')
    str1 = 'gcs-pvc' + str(i)
    replace_data = fp.read().replace(str1, 'claim')
    fp.seek(0, 0)
    fw = open(r'pvc.yaml', 'w')
    fw.write(replace_data)
    fw.seek(0, 0)
