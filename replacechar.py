#re is module which is use for replace the word Road as Rd
#Road$ $ is use for The $ symbol is a special character in
#regular expressions that indicates the end of the string.
#sub is used for subtitution

import re
street = 'Nasik M.G. Road'
print(re.sub('Road$', 'Rd.', street))
