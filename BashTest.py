coll_id = "aoimva"
supp_id = "fjowm"

import subprocess
command = ['rsync', '-r', '--progress', "./TestZone/root/1114/2565/.", ('./' + coll_id + '-' + supp_id)]
output, err = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).communicate()
# print(output)

# subprocess.run(['rsync', '-r', '--progress', "./TestZone/root/1114/2565/.", ('./' + coll_id + '-' + supp_id)])

# output = subprocess.call(command), output.wait