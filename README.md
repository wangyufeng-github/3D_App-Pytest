## 项目说明
技术栈python+uiautomation+pytest+pytest-testreport+opencv
本项目为医学图像处理软件UI自动化测试方案，采用PO设计模式，将页面元素定位与操作进行分层设计，测试框架采用pytest框架，测试报告使用pytest-testreport，同时针对无法准确定位的元素，采用了opencv图像识别技术与pyautogui库结合，
达到了操作控件的目的。
目前测试报告采用的是pytest自动带的pytest-testreport报告插件，后面可修改为allure报告，可以与Jenkins很好的集成，同时支持报告定制化，效果比较美观。

## 项目部署
首先，下载项目源码后，在根目录下找到 ```requirements.txt``` 文件，然后通过 pip 工具安装 requirements.txt 依赖，执行命令：

```
pip3 install -r requirements.txt
```
目前本项目已通过批处理的形式进行执行，双击run.bat文件即可进行环境部署。
通过使用run_all.py入口文件对测试用例执行、测试报告发送进行了统一封装,后续可以配合jenkins完成自动化测试持续集成。
需要将My3DApp添加到任务栏，因为目前通过终端启动程序后，发现界面布局异常，所以当前采用的图像识别+鼠标点击的方式。

**注意**：目前run_all.py文件设置了固定延时时间，是为了保证用例能够执行结束，进而能够达到后面发送报告的目的，将来走持续集成流程后，需要进一步调整。

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

