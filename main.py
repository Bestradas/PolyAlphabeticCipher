from PolyAlphabeticCipher import PolyAlphabeticCipher
from FileUtils import FileUtils

# Generamos una instancia de FileUtils para leer y escribir en los archivos
# Cargamos el texto del archivo a encriptar
fileUtils = FileUtils()
inputText = fileUtils.readEncryptedFile()

# Generamos una instancia de PolyAlphabeticCipher para llamar los metodos de encriptar y desencriptar
# Llamamos el metodo encrypt() con el texto a encriptar en el primer parametro y la llave en el segundo
# Llamamos al metodos decrypt() con el texto a desencriptar y la misma llave que se envio en el encriptado
polyAlphabeticCipher = PolyAlphabeticCipher()
encryptedData = polyAlphabeticCipher.encrypt(inputText, "latine")
decryptedData = polyAlphabeticCipher.decrypt(encryptedData, "latine")

# Escribimos los resultados en los archivos encrypt_result_file.txt y decrypt_result_file.txt
fileUtils.writeEncryptedData(encryptedData)
fileUtils.writeDecryptedData(decryptedData)