### 介绍
本项目用于获取摩根太平洋人民币对冲基金（968061）最新持仓，并获取对应涨跌进行预估。注意，基金持仓并未全部公布，约占45%，结果为按照已知持仓计算，仅供参考。
### 安装使用
#### 第三方库

- 需要使用到的库已经放在requirements.txt，使用pip安装的可以使用指令  
`pip install -r requirements.txt`
- 如果国内安装第三方库比较慢，可以使用以下指令进行清华源加速
`pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/`
#### 运行
python mogen.py 结果输出在控制台
### 常见问题
脚本运行环境前提是网站可正常访问（可能需要科学上网），requests 可设置 proxies 代理
```
SSLError("bad handshake: SysCallError(-1, 'Unexpected EOF')")
``` 
未找到原因，基本重试几次即可解决
```
访问频次太高，触发网页脚本检查，请在网页访问进行人机检查后即可再使用
```
登录 [网站](https://www.bloomberg.com/quote/JFPTECI:HK) 进行人机检查通过就可继续使用