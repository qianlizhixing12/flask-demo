import base64
import binascii

from Crypto.Cipher import AES

iv = "abcdefghijklmnop"


def pkcs7padding(text):
    """
    明文使用PKCS7填充
    最终调用AES加密方法时，传入的是一个byte数组，要求是16的整数倍，因此需要对明文进行处理
    :param text: 待加密内容(明文)
    :return:
    """
    bs = AES.block_size  # 16
    length = len(text)
    bytes_length = len(bytes(text, encoding='utf-8'))
    # tips：utf-8编码时，英文占1个byte，而中文占3个byte
    padding_size = length if (bytes_length == length) else bytes_length
    padding = bs - padding_size % bs
    # tips：chr(padding)看与其它语言的约定，有的会使用'\0'
    padding_text = chr(padding) * padding
    return text + padding_text


def pkcs7unpadding(text):
    """
    处理使用PKCS7填充过的数据
    :param text: 解密后的字符串
    :return:
    """
    length = len(text)
    unpadding = ord(text[length - 1])
    return text[0:length - unpadding]


def aes_cbc_pkcs7_encrypt(key: str, data: str) -> str:
    """aes加密
    :Parameters:
        key: str    加密密钥(16位不足补空，超过截取)
        data : str  加密前字符串(16倍数不足补空)
    :Return:
        str 加密后字符串
    """
    data = pkcs7padding(data).encode("utf-8")
    cipher = AES.new(key.encode("utf-8"), AES.MODE_CBC, iv.encode("utf-8"))
    result = cipher.encrypt(data)
    # result = binascii.b2a_hex(result).decode("utf-8")  #输出Hex
    result = base64.b64encode(result).decode("utf-8")  # 输出Base64
    print("result", key, result)
    return result


def aes_cbc_pkcs7_decrypt(key: str, data: str) -> str:
    """aes解密
    :Parameters:
        key: str    加密密钥(16位不足补空，超过截取)
        data : str  加密字符串(16倍数不足补空)
    :Return:
        str 加密前字符串
    """
    # data = binascii.a2b_hex(data.encode("utf-8"))
    data = base64.b64decode(data.encode("utf-8"))
    cipher = AES.new(key.encode("utf-8"), AES.MODE_CBC, iv.encode("utf-8"))
    result = cipher.decrypt(data).decode("utf-8")
    return pkcs7unpadding(result)


__all__ = [aes_cbc_pkcs7_encrypt, aes_cbc_pkcs7_decrypt, iv]

if __name__ == "__main__":
    key, data = "test413435432512", "test孙悟空"
    data1 = aes_cbc_pkcs7_decrypt(key, aes_cbc_pkcs7_encrypt(key, data))
    assert data.strip() == data1.strip(), "加密解密错误"
