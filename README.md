<div align="center">

# xsserve

![GitHub top language](https://img.shields.io/github/languages/top/NullBrunk/XSServe?style=for-the-badge)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/NullBrunk/XSServe?style=for-the-badge)
![repo size](https://img.shields.io/github/repo-size/NullBrunk/XSServe?style=for-the-badge)
</div>

<img width="1449" height="943" alt="image" src="https://github.com/user-attachments/assets/554aa722-e2b4-4844-a427-6b6832d41067" />


## 🚀 Usage

This tool simplifies XSS exploitation by combining a socket-based HTTP server with the power of ngrok. 
It enables you to quickly launch a local server and make it publicly accessible, making it easier to share payloads or demonstrate XSS vulnerabilities. 

There are basically three endpoints:
| Endpoint             | What does it to          | 
| :--------------------| :--------------- | 
| `/FILENAME`          | Serves the file named `FILENAME` in the `files/` directory, like a standard HTTP server.    | 
| `/*`                 | Logs any access to other endpoints directly in your console, giving you full visibility into unexpected requests. |   

Ideal for pentesters, security researchers, and cybersecurity enthusiasts who need a lightweight and versatile tool for XSS testing.

Some CLI argument are provided to enhance user experience:

| Argument             | What does it to          | 
| :--------------------| :--------------- | 
| `-v`, `--verbose`    | By default, only the first line of every request and the body are printed. With `-v`, all headers sent along with the request are also printed | 
| `-p`, `--port`       | By default, xsserve listens on a random port between `65000` and `65100`. With `-p` you can specify a custom port |
| `-n`, `--ngrok`      | Launches an ngrok tunnel that listens on the xsserve port. Ngrok provides a public address, which is useful if you don’t have a VPS or don’t want to set up port forwarding. | 


## ⚒️ Installation
>[!IMPORTANT]
> The script requires ngrok if you want to use the `-n` option

```bash
git clone https://github.com/NullBrunk/xsserve
cd xsserve

# Install the needed requirements
pip install -r requirements.txt
```
