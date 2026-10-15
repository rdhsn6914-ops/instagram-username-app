from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs
from html import escape
import json
import random
import string
import threading
import webbrowser

PAGE = """<!doctype html>
<html lang="ar" dir="rtl">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta charset="utf-8">
<title>فاحص اليوزرات</title>
<style>
body{background:#101323;color:white;font-family:Arial;padding:18px}
main{max-width:600px;margin:auto;background:#20263b;padding:20px;border-radius:18px}
h2{color:#b9a3ff}button,input,select{box-sizing:border-box;width:100%;padding:13px;margin:7px 0;border-radius:10px;border:0;font-size:16px}
button{background:#8064ed;color:white;font-weight:bold}
.item{padding:10px;margin:7px 0;background:#303953;border-radius:8px}
</style>
<main>
<h2>فاحص اليوزرات</h2>
<p>ولّد اقتراحات من 4 أو 5 خانات واحفظ نتائج فحصك اليدوي.</p>
<select id="length"><option value="4">4 خانات</option><option value="5">5 خانات</option></select>
<input id="amount" type="number" min="1" max="100" value="20">
<button onclick="generate()">توليد يوزرات</button>
<div id="results"></div>
<script>
function generate(){
 let n=+document.getElementById('length').value;
 let amount=Math.max(1,Math.min(100,+document.getElementById('amount').value||20));
 let chars='abcdefghijklmnopqrstuvwxyz0123456789_.';
 let out=document.getElementById('results'); out.innerHTML='';
 for(let i=0;i<amount;i++){
  let u='';
  for(let j=0;j<n;j++)u+=chars[Math.floor(Math.random()*chars.length)];
  let d=document.createElement('div'); d.className='item';
  d.textContent='@'+u+' — غير مؤكد';
  let b=document.createElement('button');b.textContent='نسخ اليوزر';
  b.onclick=()=>navigator.clipboard.writeText(u);
  d.appendChild(b);out.appendChild(d);
 }
}
</script>
</main></html>"""

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        data=PAGE.encode()
        self.send_response(200)
        self.send_header("Content-Type","text/html; charset=utf-8")
        self.send_header("Content-Length",str(len(data)))
        self.end_headers()
        self.wfile.write(data)
    def log_message(self,*args):
        pass

if __name__ == "__main__":
    print("افتح Chrome على: http://127.0.0.1:8765")
    HTTPServer(("127.0.0.1",8765),Handler).serve_forever()
