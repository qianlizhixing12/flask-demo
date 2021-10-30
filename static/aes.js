const IV = "abcdefghijklmnop";

function aes_cbc_pkcs7_encrypt(key, data) {
    // CryptoJS.AES.encrypt 需要utf8编码的字符串
    let result = CryptoJS.AES.encrypt(
        data,
        CryptoJS.enc.Utf8.parse(key),
        {
            iv: CryptoJS.enc.Utf8.parse(IV),
            mode: CryptoJS.mode.CBC,
            padding: CryptoJS.pad.Pkcs7
        }
    );
    // return CryptoJS.enc.Hex.stringify(result.ciphertext); //HEX
    return CryptoJS.enc.Base64.stringify(result.ciphertext) //base64
}

function aes_cbc_pkcs7_decrypt(key, data) {
    // CryptoJS.AES.decryptf 需要Base64编码的字符串 base64不需要下面两行
    // data = CryptoJS.enc.Hex.parse(data);
    // data = CryptoJS.enc.Base64.stringify(data);
    let result = CryptoJS.AES.decrypt(
        data,
        CryptoJS.enc.Utf8.parse(key),
        {
            iv: CryptoJS.enc.Utf8.parse(IV),
            mode: CryptoJS.mode.CBC,
            padding: CryptoJS.pad.Pkcs7
        }
    );
    return CryptoJS.enc.Utf8.stringify(result);
}