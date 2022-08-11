# Python_in_CKIR
싸지방에서 vscode(or sublime text)로 파이썬을 실행해보자  
갑자기 vscode 다운이 안된다.  
sublime text 다운해서 쓰는중  
  
  
  
마이크로소프트 스토어에서 python 다운받고, vscode(or sublime text), git bash 다운받고 vscode 터미널을 git bash로 설정하고 쓰면 됨  

## vscode 기본 터미널 변경하는법  
```
Ctrl + Shift + p
```
```
Terminal: Select Default Profile
```
```
Git Bash
```
선택  


## 터미널 단축키
```
Ctrl + `  
```
  
## sublime text 터미널 변경하는법
```
Ctrl + Shift + p
```
```
Package Control: Install Package
```
```
Preferences -> Package Settings -> Terminus -> Settings
or
Preferences: Terminus Settings
```
왼쪽꺼 오른쪽에 붙여 넣은 후,
```
"shell_configs":
    [
        {
            "name": "Git Bash",
            "cmd": ["cmd.exe", "/k", "C:/Program Files (x86)/Git/bin/bash.exe"],
            "env": {},
            "enable": true,
            "default": true,
            "platforms": ["windows"]
        },
    ]
```
중간에 이거 껴넣어줌
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
# 왜 vscode 다운로드 안되냐고!!!!!!!!!!!!!!!!!!!!!!!!
