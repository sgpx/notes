const bucketInfo = {
  name: "mybucket",
  region: "us-east-1",
  profile: "myprofile",
};

// https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/S3.html#getObject-property
// https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/S3.html#putObject-property
// https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/S3.html#listObjects-property


const AWS = require("aws-sdk");
const credentials = new AWS.SharedIniFileCredentials({
  profile: bucketInfo.profile,
});
AWS.config.credentials = credentials;
AWS.config.update({ region: bucketInfo.region });
const s3 = new AWS.S3({ apiVersion: "2006-03-01" });

s3.getObject({ Bucket: bucketInfo.name, Key: "index.html" }, (_, s) =>
  console.log(s.Body.toString())
);

s3.putObject(
  {
    Body: require("fs").readFileSync("abc.txt"),
    Bucket: bucketInfo.name,
    Key: "abc-1.txt",
  },
  console.log
);

s3.listObjects(
  {
    Bucket: bucketInfo.name,
  },
  console.log
);
