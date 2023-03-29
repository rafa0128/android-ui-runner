## 简介

https://github.com/openatx/uiautomator2

uiautomator2是一个python库，用于Android的UI自动化测试，其底层基于Google uiautomator，Google提供的
uiautomator库可以获取屏幕上任意一个APP的任意一个控件属性，并对其进行任意操作

python-uiautomator2主要分为两个部分，python客户端，移动设备
	
- python端: 运行脚本，并向移动设备发送HTTP请求
	
- 移动设备：移动设备上运行了封装了uiautomator2的HTTP服务，解析收到的请求，并转化成uiautomator2的代码。


执行过程
	
- 在移动设备上安装atx-agent(守护进程), 随后atx-agent启动uiautomator2服务(默认7912端口)进行监听
	
- 在PC上编写测试脚本并执行（相当于发送HTTP请求到移动设备的server端）
	
- 移动设备通过WIFI或USB接收到PC上发来的HTTP请求，执行制定的操作

## 环境
```
python 3.10+
安装依赖： pip install -r requirement
```

## 元素定位
```
python -m weditor
```

## 执行
```python
python -m uiautomator2 init # 第一次使用，要先初始化

python run.py
```

## 项目结构
```
u2-ui-runner
├─run.py # 执行入口
├─requirement.txt # 模块依赖 pip install -r requirement.txt
├─public
|  ├─Common.py # 公共类
|  ├─Decorator.py # 装饰器类
|  ├─Config.py # 配置读取类
|  ├─config.ini # 配置信息  
|  ├─Log.py # 日志类
|  ├─HTMLTestReport.py # 测试报告类
|  ├─chromedriver.py # webview处理类
|  ├─BasePage.py # 业务逻辑处理类
├─case
|   ├─case*.py # 各个场景的测试用例
|   ├─mask_case.py # 测试用例集合执行
├─report # 存放测试报告和截图文件
├─log # 存放logcat日志
├─apk # 存放测试用的apk文件
```

## Python API
```python
import uiautomator2 as u2

d = u2.connect()

# 定位
d(resourceId="xxx").click(timeout=5)
d(className="xxx").click(timeout=5)
d(text="xxx").click(timeout=5)
d(description="xxx").click(timeout=5)
d(text="xxx", className="xxx").click()
d.xpath("//android.widget.FrameLayout[@index='0']/android.widget.LinearLayout[@index='0']").click()
d.click(182, 1264) #坐标

d(text="xxx").click(timeout=10)  # 等待元素出现(最多10秒），出现后单击 
d(text='xxx').click_exists(timeout=10.0) # 在10秒时点击，默认的超时0
d(text="xxx").click_gone(maxretry=10, interval=1.0) # 单击直到元素消失，返回布尔 ，maxretry默认值10,interval默认值1.0 

d(text="xxx").wait(timeout=3.0) ## 等待ui对象出现，返回布尔值
d(text="xxx").wait_gone(timeout=1.0)  # 等待ui对象的消失

d(text="xxx").click(offset=(0.5, 0.5)) # 点击基准位置偏移 点击中心位置，同d(text="xxx").click()
d(text="xxx").click(offset=(0, 0)) # 点击左前位置
d(text="xxx").click(offset=(1, 1)) # 点击右下

# 双击
d(text="xxx").double_click() #双击特定ui对象的中心
d.double_click(x, y, 0.1)#两次单击之间的默认持续时间为0.1秒

# 长按
d(text="xxx").long_click() # 长按特定UI对象的中心
d.long_click(x, y, 0.5) # 长按坐标位置0.5s默认

# 左右
d(text="xxx").swipe("right")
d(text="xxx").swipe("left", steps=10)
d(text="xxx").swipe("up", steps=20) # 1步约为5ms, 20步约为0.1s
d(text="xxx").swipe("down", steps=20)
d(text="xxx").gesture((sx1, sy1), (sx2, sy2), (ex1, ey1), (ex2, ey2))

d.swipe_ext("right") # 手指右滑，4选1 "left", "right", "up", "down"
d.swipe_ext("right", scale=0.9) # 默认0.9, 滑动距离为屏幕宽度的90%
d.swipe_ext("right", box=(0, 0, 100, 100)) # 在 (0,0) -> (100, 100) 这个区域做滑动
d.swipe_ext("up", scale=0.8) # 实践发现上滑或下滑的时候，从中点开始滑动成功率会高一些

# 滚动
d(scrollable=True).fling() #向前投掷(默认)垂直(默认)
d(scrollable=True).fling.vert.forward()  #垂直向后滚动
d(scrollable=True).fling.vert.backward()
d(scrollable=True).fling.horiz.toBeginning(max_swipes=1000)
d(scrollable=True).fling.toEnd() #滚动到结束
d(scrollable=True).scroll(steps=10)  # 向前滚动(默认)垂直(默认)
d(scrollable=True).scroll.horiz.forward(steps=100)  # 水平向前滚动
d(scrollable=True).scroll.vert.backward()  #垂直向后滚动
d(scrollable=True).scroll.horiz.toBeginning(steps=100, max_swipes=1000)  #滚动到开始水平
d(scrollable=True).scroll.toEnd() # 滚动到垂直结束
d(scrollable=True).scroll.to(text="Security") #垂直向前滚动，直到出现特定的ui对象

# 拖动
d(text="xxx").drag_to(500, 500, duration=0.1)  #在0.1秒内拖动到坐标（x,y）
d(text="xxx").drag_to(text="安全中心", duration=0.2)

# 输入框
d(description="xxx").get_text()
d(description="xxx").set_text("1234")
d(description="xxx").clear_text()

# 打开链接
d.open_url("https://www.baidu.com")
d.open_url("taobao://taobao.com")    # open Taobao app
d.open_url("appname://appnamehost")

# 通知栏
d.open_notification（）#下拉打开通知栏
d.open_quick_settings（）#下拉打开快速设置栏

# 屏幕
d.info.get（' screenOn '）#需要 Android> = 4.4
d.screen_on（）#打开屏幕 
d.screen_off（）#关闭屏幕
d.unlock()  # 解锁屏幕（相当于 发射活动:com.github.uiautomator.ACTION_IDENTIFY， 按home键）
d.freeze_rotation() # 冻结旋转
d.freeze_rotation(False)# 开启旋转
d.screenshot("home.jpg") # 截图

#应用操作
d.app_install('http://some-domain.com/some.apk') #引号内为下载apk地址
d.app_start('com.ruguoapp.jike') #引号内为包名称
sess = d.session("com.netease.cloudmusic") # start 网易云音乐，Session表示应用程序的生命周期
d.app_stop('com.example.hello_world')  #相当于'am force-stop'强制停止应用
d.app_clear('com.example.hello_world') #相当于'pm clear' 清空App数据
d.app_stop_all() # 停止所有
d.app_stop_all(excludes=['com.examples.demo']) # 停止所有应用程序，除了com.examples.demo
sess.close() # 停止网易云音乐

# 推拉文件
d.push("foo.txt", "/sdcard/") # push文件夹
d.push("foo.txt", "/sdcard/bar.txt") # push和重命名

with open("foo.txt", 'rb') as f:
    d.push(f, "/sdcard/")

d.push("foo.sh", "/data/local/tmp/", mode=0o755) # 推动和更改文件访问模式
d.pull("/sdcard/tmp.txt", "tmp.txt") # 如果在设备上找不到文件，FileNotFoundError将引发
d.pull("/sdcard/some-file-not-exists.txt", "tmp.txt")

# 弹窗
d.disable_popups（）#自动跳过弹出窗口 
d.disable_popups（false）#禁用自动跳过弹出窗

# 检查崩溃
sess(text="xxx").click() # 崩溃时引发会话中断错误SessionBrokenError

# 获取应用信息
d.app_info("com.examples.demo") # 应用信息
img = d.app_icon("com.examples.demo").save("icon.png") #应用图标

# 键盘
d.press("home") # 点击home键
d.press("back") # 点击back键
d.press("left") # 点击左键
d.press("right") # 点击右键
d.press("up") # 点击上键
d.press("down") # 点击下键
d.press("center") # 点击选中
d.press("menu") # 点击menu按键
d.press("search") # 点击搜索按键
d.press("enter") # 点击enter键
d.press("delete") # 点击删除按键
d.press("recent") # 点击近期活动按键
d.press("volume_up") # 音量+
d.press("volume_down") # 音量-
d.press("volume_mute") # 静音
d.press("camera") # 相机
d.press("power") #电源键
```
## webview

#### Python API

```python
import uiautomator2 as u2
from public.chromedriver import ChromeDriver
d = u2.connect()
    
dri = ChromeDriver(d, 3456).driver()
dri.find_element_by_id('index-kw').send_keys('python')
dri.find_element_by_id('index-bn').click()
dri.quit()
ChromeDriver.kill()
```    

#### 元素定位

- edge://inspect/#devices （推荐）
- chrome://inspect (需要翻墙)
- appium-desktop

参考
- https://registry.npmmirror.com/binary.html?path=chromedriver/ (和chrome对应版本的chromedriver)
- https://www.shuzhiduo.com/A/o75N0DNDzW/
- https://testerhome.com/topics/7232
