```bash
aws --endpoint-url=http://localhost:4566 s3 mb s3://nyc-duration
```

```bash
aws --endpoint-url=http://localhost:4566 s3 ls
```

```bash
aws --endpoint-url=http://localhost:4566 s3 ls s3://nyc-duration --recursive
```

```bash
>aws --endpoint-url=http://localhost:4566 s3 ls s3://nyc-duration \
 --recursive --human-readable --summarize
```

```bash: Dummy AWS credentials:
export AWS_ACCESS_KEY_ID=test
export AWS_SECRET_ACCESS_KEY=test
export AWS_DEFAULT_REGION=us-east-1
```