# CPPM *main* bucket
The default CPPM bucket.
## Submitting packages
Create a file containing the URL to the app.
Only portable apps (apps with `.zip` extension) are allowed, to avoid UAC prompts on CPPM NT variants and
the `sudo` requirement for CPPM POSIX variants.

No malware or pirated software can be allowed on official CPPM buckets.

## Update buckets
Run `bucket quickfix main` to update the main bucket.

## Other buckets
* [Admin](https://github.com/cppmbucket/admin): Non-portable apps that may require UAC on CPPM NT and `sudo` on CPPM POSIX
* [Python](https://github.com/cppmbucket/python): Python 3.8-3.11 modules (you must run `install python3`)
* [Ports](https://github.com/cppmbucket/ports): Apps made for other systems, then had a port to another OS
* [Multiverse](https://github.com/cppmbucket/multiverse): Nonfree apps
