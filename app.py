from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import boto3
from config import S3_BUCKET, S3_KEY, S3_SECRET
from filters import datetimeformat, file_type


s3_resource = boto3.resource(
   "s3",
   aws_access_key_id=S3_KEY,
   aws_secret_access_key=S3_SECRET
)


app = Flask(__name__)
Bootstrap(app)
app.jinja_env.filters['datetimeformat'] = datetimeformat
app.jinja_env.filters['file_type'] = file_type


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/files')
def files():
    my_bucket = s3_resource.Bucket(S3_BUCKET)
    summaries = my_bucket.objects.all()
    print(my_bucket)
    print(summaries)
    return render_template('files.html', my_bucket=my_bucket, files=summaries)


if __name__ == "__main__":
    app.run(debug=True)
