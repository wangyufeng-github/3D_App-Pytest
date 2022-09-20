## 项目说明
技术栈python+uiautomation+behave+allure
本项目为医学图像处理软件UI自动化测试方案，采用PO设计模式，将页面元素定位与操作进行分层设计，测试框架采用BDD行为驱动框架behave，同时针对无法准确定位的元素，采用了opencv图像识别技术与pyautogui库结合，
达到了操作控件的目的。

## 项目部署
首先，下载项目源码后，在根目录下找到 ```requirements.txt``` 文件，然后通过 pip 工具安装 requirements.txt 依赖，执行命令：

```
pip3 install -r requirements.txt
```
需要将My3DApp添加到任务栏，因为目前通过终端启动程序后，发现界面布局异常，所以当前采用的图像识别+鼠标点击的方式。

## 项目结构
- common ====>> 包含界面元素操作、图像识别、日志模块、鼠标操作、报告输出、屏幕截图、邮件发送、基本工具
- config ====>> 配置文件，用户名、密码信息
- image ====>> 图像识别的模板图片
- log ====>> 日志存储
- page ====>> 页面元素定位+元素操作
- reports ====>> 测试报告存储路径
- screenshot ====>> 失败用例截图存放路径
- testcase ====>>业务逻辑代码，根据不同界面，会有不同的test_xx.py文件
- pytest.ini ====>> pytest框架配置文件
- requirements.txt ====>> 相关依赖包文件
- features ====>>存放用例.feature文件和step执行步骤


