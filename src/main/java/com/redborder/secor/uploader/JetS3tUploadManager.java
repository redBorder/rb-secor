package com.redborder.secor.uploader;

import com.pinterest.secor.common.LogFilePath;
import com.pinterest.secor.common.SecorConfig;
import com.pinterest.secor.uploader.FutureHandle;
import com.pinterest.secor.uploader.Handle;
import com.pinterest.secor.uploader.UploadManager;
import org.jets3t.service.S3Service;
import org.jets3t.service.S3ServiceException;
import org.jets3t.service.impl.rest.httpclient.RestS3Service;
import org.jets3t.service.model.S3Object;
import org.jets3t.service.security.AWSCredentials;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import scala.tools.nsc.Global;

import java.io.File;
import java.io.IOException;
import java.security.NoSuchAlgorithmException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;


/* S3 uploader implementation using JetS3t library to allow use Secor with other S3 implementations like Riak-CS */
public class JetS3tUploadManager extends UploadManager {

    private static final Logger LOG = LoggerFactory.getLogger(JetS3tUploadManager.class);
    private static final ExecutorService executor = Executors.newFixedThreadPool(256);
    private S3Service s3Service;
    private String s3Bucket;

    public JetS3tUploadManager(SecorConfig config) {
        super(config);

        final String accessKey = mConfig.getAwsAccessKey();
        final String secretKey = mConfig.getAwsSecretKey();
        s3Bucket = mConfig.getS3Bucket();
        AWSCredentials awsCredentials = new AWSCredentials(accessKey, secretKey);
        s3Service = new RestS3Service(awsCredentials);
    }

    public Handle<?> upload(LogFilePath localPath) throws Exception {
        String s3Key = localPath.withPrefix(mConfig.getS3Path()).getLogFilePath().split("\\/(?=[^\\/]+$)")[0];
        final File localFile = new File(localPath.getLogFilePath());
        final String s3Path = s3Bucket + "/" + s3Key;
        LOG.debug("s3path = " + s3Path);
        final Future<?> f = executor.submit(new Runnable() {
            @Override
            public void run() {
                try {
                    S3Object object = new S3Object(localFile);
                    s3Service.putObject(s3Path, object);
                } catch (IOException e) {
                    throw new RuntimeException(e);
                } catch (NoSuchAlgorithmException e) {
                    throw new RuntimeException(e);
                } catch (S3ServiceException e) {
                    LOG.error("Failed putting object in S3", e);
                    throw new RuntimeException(e);
                }
            }
        });

        return new FutureHandle(f);
    }
}
