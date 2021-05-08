
FILE_WITH_TEXT_TO_ENCRYPTING = "Files/file_with_text_to_encrypt.txt"
ENCRYPTED_RESULT_FILE = "Files/encrypt_result_file.txt"
DECRYPTED_RESULT_FILE = "Files/decrypt_result_file.txt"

class FileUtils:

    def readEncryptedFile(self):
        with open(FILE_WITH_TEXT_TO_ENCRYPTING, 'r') as file:
            return file.read().replace('\n', '')

    def writeEncryptedData(self,text):
        f = open(ENCRYPTED_RESULT_FILE, "w")
        f.write(text)
        f.close()

    def writeDecryptedData(self, text):
        f = open(DECRYPTED_RESULT_FILE, "w")
        f.write(text)
        f.close()