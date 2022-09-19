# !/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time : 2022/8/23 10:00
# @Author : yufeng.wang@we-med.com
# @Site :
# @File : control_element.py
# @Software : PyCharm


import time
import subprocess
import uiautomation as auto


auto.uiautomation.DEBUG_SEARCH_TIME = True
auto.uiautomation.SetGlobalSearchTimeout(1)

class OperateWindow:
    """
    操作控件的相关方法
    """

    def __init__(self):
        pass

    def get_value_pattern(self, window):
        """
        获取控件文本信息
        :param window:
        :return:
        """
        return window.GetValuePattern().Value()

    def window_exists(self, window, max_search_seconds=5.0, search_interval_seconds=0.5):
        """
        判断控件是否存在
        :param window:窗口
        :param maxSearchSeconds:搜索时间
        :param searchIntervalSeconds: 搜索间隔
        :return:
        """
        try:
            result = window.Exists(window, max_search_seconds, search_interval_seconds)
        except TypeError as err:
            print(f"Element is not found")
            return False
        else:
            return result

    def show_desktop(self):
        """
        显示桌面
        :return:None
        """
        auto.ShowDesktop()

    def get_process_time(self):
        """
        获取uiautomation运行时间
        :return:
        """
        return auto.ProcessTime()

    def judge_same_element(self, window1, window2):
        """
        判断两个控件是否相同
        :param window1:
        :param window2:
        :return:
        """
        return auto.ControlsAreSame(window1, window2)

    def mouse_drag_move(self, x1, y1, x2, y2, move_speed):
        """
        鼠标拖拽
        :param x1:
        :param y1:
        :param x2:
        :param y2:
        :param moveSpeed:速度
        :return:
        """
        auto.DragDrop(x1, y1, x2, y2, move_speed)

    def get_current_mouse_window(self):
        """
        获取当前鼠标位置对应的窗口
        :return:
        """
        return auto.ControlFromCursor().GetTopLevelControl()

    def get_chirldren(self, window):
        """
        获取所有子控件
        :param window:
        :return:
        """
        return window.GetChildren()

    def get_first_child(self, control):
        """
        获取首个子控件
        :param control:
        :return:
        """
        return control.GetFirstChildControl()

    def get_last_child(self, control):
        """
        获取最后一个子控件
        :param control:
        :return:
        """
        return control.GetLastChildControl()

    def get_next_child(self,control):
        """
        获取下一个兄弟控件
        :param control:
        :return:
        """
        return control.GetNextSiblingControl()

    def get_previous_child(self,control):
        """
        获取前一个兄弟控件
        :param control:
        :return:
        """
        return control.GetPreviousSiblingControl()

    def get_parent_control(self,control):
        """
        获取父级控件
        :param control:
        :return:
        """
        return control.GetParentControl()

    def get_top_control(self,control):
        """
        获取顶层控件
        :param control:
        :return:
        """
        return control.GetTopLevelControl()

    def click(self,x,y):
        """
        鼠标左键点击x,y
        :param x: x坐标
        :param y: y坐标
        :return:
        """
        auto.Click(x,y)

    def right_click(self,x,y):
        """
        鼠标右键点击
        :param x:
        :param y:
        :return:
        """
        auto.RightClick(x,y)

    def get_root_control(self):
        """
        获取桌面对象
        :return:
        """
        return auto.GetRootControl()

    def get_consol_windows(self):
        """
        获取python控制台窗口对象
        :return:
        """
        return auto.GetConsoleWindow()

    def get_window_handle(self,win):
        """
        获取窗口句柄
        :param win:
        :return:
        """
        handle = win.NativeWindowHandle
        return handle

    def get_window_handle_element(self,handle):
        """
        根据窗口句柄获取窗口控件对象
        :param handle:
        :return:
        """
        return auto.ControlFromHandle(handle)

    def hide_window(self,win):
        """
        窗口隐藏
        :param win:
        :return:
        """
        win.Hide()

    def show_window(self,win):
        """
        窗口从隐藏变为显示
        :param win:
        :return:
        """
        win.Show()

    def min_window(self,win):
        """
        窗口最小化
        :param win:
        :return:
        """
        win.Minimize()

    def max_window(self,win):
        """
        窗口最大化
        :param win:
        :return:
        """
        win.Maximize()

    def is_iconic(self,handle):
        """
        通过窗口句柄判断窗口是否最小化
        :param handle:
        :return:
        """
        return auto.IsIconic(handle)

    def is_zoomed(self,handle):
        """
        通过窗口句柄判断窗口是否最大化
        :param handle:
        :return:
        """
        return auto.IsZoomed(handle)

    def move_center(self,win):
        """
        移动窗口至屏幕中心
        :param win:
        :return:
        """
        win.MoveToCenter()

    def set_top_most(self,win):
        """
        设置窗口置顶
        :param win:
        :return:
        """
        win.SetTopmost()

    def walk_tree(self,control,depth):
        """
        根据遍历深度对某个节点进行遍历
        :param control:
        :param depth:
        :return:
        """
        desktop = self.get_root_control()
        for control, depth in auto.WalkTree(desktop, getFirstChild=self.get_first_child(),
                                            getNextSibling=self.get_next_child(),
                                            includeTop=True, maxDepth=depth):
            if not control.Name:
                continue
            print(' ' * depth * 4, control.Name)

    def get_window_text(self,control):
        """
        返回控件文本信息
        :param control:
        :return:
        """
        return control.GetTextPattern().DocumentRange.GetText()


if __name__ == '__main__':
    # subprocess.Popen('notepad.exe')
    window = auto.WindowControl(searchDepth=1,ClassName='Notepad')
    obj = OperateWindow()
    print(obj.window_exists(window))
    # time.sleep(2)
    # window.Hide()
    # time.sleep(1)
    # window.Show()
    # window.Minimize()
    # obj.hide_window(window)
    # print(window.GetChildren()[0].ClassName)
    # print(obj.get_root_control())
    # print(obj.get_consol_windows())