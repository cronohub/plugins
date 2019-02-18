# S3

Simple S3 archiving plugin. Files over 10MB in size are uploaded in chunks.

# Configuration

Requires a fully configured local aws client. This, in turn, configures boto,
the python library used by this plugin.

Also requires a bucket name in the form of an environment variables called:

```
CRONOHUB_S3_BUCKETNAME
```