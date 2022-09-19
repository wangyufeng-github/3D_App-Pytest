Feature: 登录模块测试

    测试管理员、普通用户、技服账号登录功能

    Scenario Outline: 管理员用户登录功能测试
      Given 点击管理员按钮
      When 点击用户名输入框
      And 输入用户名<username>
      And 点击密码输入框
      And 输入密码<password>
      And 点击登录按钮
      Then 判断病例管理界面是否显示<status_value>
    Examples:
        | username | password | status_value |
        | admin  | 123  |  True |    
        | admin  | 111  |  False |  
        | Admin  | 123  |  False |  
        | Admin  | 111  |  False |  
