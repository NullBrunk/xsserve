<div align="center">

# xsserve

![GitHub top language](https://img.shields.io/github/languages/top/NullBrunk/XSServe?style=for-the-badge)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/NullBrunk/XSServe?style=for-the-badge)
![repo size](https://img.shields.io/github/repo-size/NullBrunk/XSServe?style=for-the-badge)
</div>

![xsserve](https://github.com/user-attachments/assets/8ed817c2-2cc4-49f7-b86a-9286bfb2664e)


## 🚀 Usage

This tool simplifies XSS exploitation by combining a socket-based HTTP server with the power of ngrok. 
It enables you to quickly launch a local server and make it publicly accessible, making it easier to share payloads or demonstrate XSS vulnerabilities. 

There are basically three endpoints:
| Endpoint             | What does it to          | 
| :--------------------| :--------------- | 
| `/FILENAME`          | Serves the file named `FILENAME` in the `files/` directory, like a standard HTTP server.    | 
| `/*`                 | Logs any access to other endpoints directly in your console, giving you full visibility into unexpected requests. |   

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
