# TCPchat
請設計一個client/server 架構的程式，須滿足以下功能
1. 假設server內建帳號 user="pi", password="csie"
2. server端允許透過port 8080的所有連線
3. 連線成功 server端會送出"Login:"字串
4. client端收到"Login:"字串後，可以讓使用使透過input 指令輸入使用者帳號，然後傳給server
5A. 如果server收到帳號不是"pi"，回傳給client "No such user!"然後斷線
5B. 如果server收到帳號是"pi"，回傳給client "Password:"。
6. client端收到"Password:"後，，可以讓使用使透過input 指令輸入使用者密碼，然後傳給server
7A. 如果server收到帳號密碼是"csie"，回傳給client "Login OK!"然後斷線
7B. 如果server收到帳號密碼不是"csie"，回傳給client "Password Error!"然後斷線
