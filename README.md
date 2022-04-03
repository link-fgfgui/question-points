# question-points
晚自习时提问加分
___
## 下载
[Releases](https://github.com/link-fgfgui/question-points/releases)
<br/>[蓝奏云](https://link-fgfgui.lanzoum.com/i8IwR012jh7c) 密码:link

___

## 使用
下载后运行安装程序即可

___

## 注意
对外公开链接没有配置文件,请自行搭建
### 手动搭建
**格式：**
```json
{
    "names": [
        "姓名1",
        "姓名2",
        "姓名3"
    ]
}
```
**请保存为`config.json`并存储至config文件夹下**
### 自动搭建
当程序没有发现配置文件会自动搭建，但没有任何数据<br/>您可以cd到安装路径，使用<br/>`main.exe setconfig`(Windows)<br/>`python setconfig.py`(Linux请cd到clone的仓库)<br/>来自动搭建<br/>
请保证您的输入格式为：<br/><br/>
姓名1<br/>姓名2<br/>姓名3<br/>姓名4<br/>姓名5
### 调试搭建
cd到安装路径，使用`main.exe debug`(Windows)启动调试，您可以在`names`页中添加<br/>(Linux请下载源文件，自行安装Python环境(推荐3.6)后，cd到源文件目录，使用`python main.py debug`开始)



___


## 说明
### 参数
程序有且仅有两个参数：`old`与`debug`,其中`old`已废，但我也不知道问题在哪。。。<br/>`debug`可以打开调试窗口（类似与”设置“），会持续有效
___
### 配置文件
配置文件（./config/config.json）保持了所有数据，请妥善保存<br/>格式如下<br/>
```json
{
  "names": [],
  "password": "",
  "allpoint": 20,
  "onepoint": 10,
  "countmode": "0",
  "maxtell": 2,
  "maxtime": 300,
  "mainidea": 0,
  "onceadd": 1,
  "color": "rgb(0,85,255);",
  "0000-00-00": [
    {
      "time": 1600000000,
      "stu": "",
      "tea": "",
      "start": 1.1111111
    }
  ]
}
```
___
### 更新
程序会自动更新（于将要关闭时），请记得点`下一步`完成安装
___
### 其他
使用该程序即表明您同意[《汉仪字库个人非商用许可协议》](http://www.hanyi.com.cn/faq-doc-2)
如果不同意,请删除config目录下的`zh-cn.ttf`
config中的字体与图片仅学习与交流使用，没有任何商业用途！

___