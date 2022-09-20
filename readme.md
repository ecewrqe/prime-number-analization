# table & judgment of the prime numbers

素数はより小さいいずれの自然数に割り切れない数を指す。素数配列は点在分布数列の一種集合、その上、自然界に数えきれないほど存在している  
1,2,3,5といういずれ十以内の数は大量な意味を付けている。その中には特に7はそれほど意味が多くないゆえに、素数であるだけに人に引かないかと思うに  
この度素数を取り上げて綺麗に分布を見せようと思うに基づいて作ったという簡易な素数二次元表  
なお、拙いアルゴリズム力が容赦してください。pythonのtkinterフレームワークスで作ったので、素数二次元表と素数判定いずれも直観的に示している  

## 基本情報
language: python3.6.5  
framework: tkinter8.6, PySide6, qtCreator, pyinstaller  
OS: windows10  
author: euewrqe  
requiring software: python3.6.5, pip3, tkinter8.6  

## 機能
あ：最大数と最小数という両端を定めてから出来る素数二次元表  
い：一つの自然数を指定してから、素数であることを判定することができる  

## note
アルゴリズムによって、素数表の機能について最大数制限は八桁。最小数は7以下を入力しても自ら7以上と定められる  
素数判定機能では16桁の判定は可能
>> 配布: pyinstaller --onefile --noconsole qt_prime_num.py

## 新機能
ハッピー素数判定機能とハッピー素数一覧表作成可能になりました
あ：二次元表には「ハッピー?」をチェックするとハッピー素数一覧表作成可能
い：素数やハッピー素数のいずれも判定できるようになっている
う：qtバージョン
