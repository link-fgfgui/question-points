# question-points
晚自习时提问加分
## 下载
[Releases](https://github.com/link-fgfgui/question-points/releases)<br/>[蓝奏云](https://link-fgfgui.lanzoum.com/i8IwR012jh7c) 密码:link

___

## 使用
下载后运行安装程序即可

___

## **注意**
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
当程序没有发现配置文件会自动搭建，但没有任何数据<br/>您可以cd到安装路径，使用<br/>`main.exe setconfig`(Windows)<br/>`python main.py setconfig`(Linux)<br/>来自动搭建<br/>
请保证您的输入格式为：<br/>
姓名1<br/>姓名2<br/>姓名3<br/>姓名4<br/>姓名5
### 调试搭建
cd到安装路径，使用`main.exe debug`(Windows)启动调试，您可以在`names`页中添加<br/>(Linux请下载源文件，自行安装Python环境(推荐3.6)后，cd到源文件目录，使用`python main.py debug`开始)



___