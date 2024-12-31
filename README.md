<div align="center">

# XSServe

![GitHub top language](https://img.shields.io/github/languages/top/NullBrunk/XSServe?style=for-the-badge)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/NullBrunk/XSServe?style=for-the-badge)
![repo size](https://img.shields.io/github/repo-size/NullBrunk/XSServe?style=for-the-badge)
</div>

![xsserve](https://github.com/user-attachments/assets/ba788344-952d-430f-8ace-fbc4d4de5369)


## 🚀 Usage

This tool simplifies XSS exploitation by combining a socket-based HTTP server with the power of ngrok. 
It enables you to quickly launch a local server and make it publicly accessible, making it easier to share payloads or demonstrate XSS vulnerabilities. 
There are basically two endpoints

- `/FILENAME`: Serves a file from the `files/` directory, like a standard HTTP server.
- `/?cookie=XXX`: Only logs the value of `XXX`, useful for testing cookie capture scenarios.
- `/.*`: Logs any access to other endpoints directly in your console, giving you full visibility into unexpected requests.

Ideal for pentesters, security researchers, and cybersecurity enthusiasts who need a lightweight and versatile tool for XSS testing.


## ⚒️ Installation
>[!IMPORTANT]
> The script requires ngrok

```bash
git clone https://github.com/NullBrunk/xsserve
cd xsserve

# Install the needed requirements
pip install -r requirements.txt
```
