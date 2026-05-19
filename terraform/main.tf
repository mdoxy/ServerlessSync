resource "aws_s3_bucket" "documents" {
  bucket = "serverlesssync-documents-mayuri"
}

resource "aws_dynamodb_table" "metadata" {
  name         = "file-metadata"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "file_id"

  attribute {
    name = "file_id"
    type = "S"
  }
}

resource "aws_sns_topic" "notifications" {
  name = "file-upload-notifications"
}
