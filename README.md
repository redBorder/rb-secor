# rb-secor

rb-secor is an extension of secor service, which you can find in this repo: https://github.com/pinterest/secor

## Platforms

- Rocky Linux 9.5

## Features

rb-secor provides two additional features in two new classes:

1. Support for classify messages in diferent folder depending of namespace (using namespace field in json messages). 

2. Support for upload files to s3 using jets3t library. It is useful because allows secor to send data to AWS S3 and to other S3 services implementation like Riak CS. 

## Installation

It is autoinstalled by redborder-manager, but can also be installed manually:

```bash
dnf install rb-secor
```

## Configuration

To use this extension you have to add rb-secor classes to classpath when you launch the secor service and configure the following.

To use first feature, you have to configure secor.message.parser.class to use class com.redborder.secor.parser.MessageRbParser:
```secor.message.parser.class=com.redborder.secor.parser.MessageRbParser```

To use second feature, you have to configure secor.upload.manager.class to use class com.redborder.secor.uploader.JetS3tUploadManager:
```secor.upload.manager.class=com.redborder.secor.uploader.JetS3tUploadManager```

In addition you have to configure jets3t.properties, whose configuration file is like this:

```
s3service.s3-endpoint=s3.redborder.cluster
s3service.https-only=false
s3service.s3-endpoint-http-port=8088
s3service.disable-dns-buckets=true
```

## Contributing

1. Fork the repository on Github
2. Create a named feature branch (like add_component_x)
3. Write your change
4. Write tests for your change (if applicable)
5. Run the tests, ensuring they all pass
6. Submit a Pull Request using Github
