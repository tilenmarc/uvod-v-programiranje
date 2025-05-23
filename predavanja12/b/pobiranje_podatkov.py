import re
import os


vzorec = re.compile(
    r'ipc-metadata-list-item__list-content-item--link" tabindex=".+?" '
    r'aria-disabled="false" href="/name/nm(?P<sifra>\d+)/\?ref_=tt_ov_st_.+?">(?P<ime>.+?)</a></li>'
)


print(len(filmi_info))
# print(filmi_info)
