import datetime
import os

"""
Create the yaml file with naming pvc.yaml
"""
for i in range(1, 10):
    s = datetime.datetime.now()
    os.system('oc delete pvc/claim%s' % i)
    e = datetime.datetime.now()
    f = str(e - s)
    fp = open(r'delete_results', 'a')
    str1 = 'claim%s' % i + '\t' + f
    fp.write(str1)
    fp.write('\n')


