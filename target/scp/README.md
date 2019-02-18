# SCP

This plugin is used to simply SCP files to a remote host.

# Configuration

```
Help (scp target plugin):
    - Environment Property:
        CRONOHUB_SCP_HOST: host name to connect to. This can be one of two:
    #1: a hostname as defined under ~/.ssh/config file exp:
        Host pi
            HostName 1.2.3.4
            User username
            Port 1234
            IdentityFile ~/.ssh/id_rsa

        In this case the environment property would be `pi`.
    #2: an IP address or a web site address in which case it will be tried as is.
```