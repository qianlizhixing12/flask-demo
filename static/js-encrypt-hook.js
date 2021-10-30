const hook_urls = ["aes_hook.do"];

(function () {


    let proxy_open = window.XMLHttpRequest.prototype.open;
    // let proxy_send = window.XMLHttpRequest.prototype.send;

    window.XMLHttpRequest.prototype.open = function (method, url) {
        const encryptkey_c = Math.random();

        this.onprogress = function (event) {
            if (event.loaded == event.total) {
                if (this.readyState >= 3 && this.status === 200 && this.getResponseHeader("encryptkey")) {
                    const encryptkey_s = this.getResponseHeader("encryptkey");
                    const mode = "a".charCodeAt() - "0".charCodeAt();
                    const key_ = ((encryptkey_c + parseFloat(encryptkey_s)).toString().replace(".", "") + "0000000000000000").substr(0, 16);
                    let key = "";
                    for (let i = 0; i < key_.length; ++i) {
                        key += String.fromCharCode((key_[i].charCodeAt() + mode))
                    }
                    let response = JSON.parse(this.responseText);
                    if (response.code === "0000") {
                        response.data = aes_cbc_pkcs7_decrypt(key, response.data);
                        response.data = JSON.parse(response.data);
                        Object.defineProperty(this, 'responseText', {
                            writable: true
                        });
                        this.responseText = JSON.stringify(response);
                        console.log("result:", key, this.responseText);
                    }
                }
            }
        }

        // this.send = function (body) {
        //     for (let i = 0; i < hook_urls.length; ++i) {
        //         if (url.startsWith(hook_urls[i])) {
        //             body = aes_cbc_pkcs7_encrypt(encryptkey_c.toString().substr(0, 16), body);
        //             break;
        //         }
        //     }
        //     proxy_send.apply(this, [].slice.call(body));
        // }

        let result = proxy_open.apply(this, [].slice.call(arguments));
        for (let i = 0; i < hook_urls.length; ++i) {
            if (url.startsWith(hook_urls[i])) {
                this.setRequestHeader("encryptkey", aes_cbc_pkcs7_encrypt(IV, encryptkey_c.toString()));
                break;
            }
        }
        return result;
    };
})();