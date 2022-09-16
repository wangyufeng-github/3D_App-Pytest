Feature: Test Login

    Scenario: Enter the username and password to log in using the admini       
        Given open the application      #打开软件
        When input username and password    #输入用户名和密码
        And click login button     #点击登录按钮 
        Then assert login status and close application
        
    