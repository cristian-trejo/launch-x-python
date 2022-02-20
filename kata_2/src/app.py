# To create a venv
#> python3 -m venv name_virtual_env
# Then to activate the venv
#> source name_virtual_env/bin/activate
# To see the installed packages
#> ls env/lib/python3.9/site-packages/

from datetime import *
from dateutil.relativedelta import *

now = datetime.now()
print(now)

now = now + relativedelta(months=1, weeks=1, hour=10)
print(now)