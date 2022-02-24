import dropbox
import os
from dropbox.files import WriteMode
class TransferData:
  def __init__(self, access_token):
    self.access_token = access_token
  def upload_file(self, source, dest):
    d = dropbox.Dropbox(self.access_token)
    listDir = os.listdir(source)
    for file in listDir:
      newFile = os.path.join(source, file)
      f = open(newFile, "rb")
      destFile = os.path.join(dest, file)
      d.files_upload(f.read(),destFile)

acToken = input("Enter access token: ")
transferData = TransferData(acToken)
source = input("Enter the file path: ")
dest = input("Enter the dropbox destination: ")

transferData.upload_file(source, dest)

print("done")
