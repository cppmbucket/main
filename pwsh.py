man = "PowerShell for every operating system!"
APP = "PowerShell Core"
APPLICENSE = "MIT" # SPDX ID https://spdx.org/licenses/MIT (json version: https://spdx.org/licenses/MIT.json)

from cppmutils import dwnld as cppmget # /!\ Meaning: download
cppmget(DOWNLOAD, license=LICENSE, name=APP, description=man)
