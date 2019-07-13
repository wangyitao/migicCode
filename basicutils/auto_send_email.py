# -*- coding: utf-8 -*-
# @Time    : 19-1-10 下午8:06
# @Author  : Felix Wang

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.utils import parseaddr, formataddr
from email.header import Header
import smtplib
from hashlib import md5


# 自动发邮件
class autoSendEmail:
    def __init__(self, sender, password, title, from_who, recever, smtp_server="smtp.qq.com", port=465):
        """
        :param sender: 邮件发送者
        :param password: 密码
        :param title: 邮件发送主题
        :param from_who: 邮件来自谁
        :param recever: 邮件接收者，可以是多个
        :param smtp_server: 邮件服务器，默认qq邮箱服务器
        :param port: 服务器端口qq邮箱默认端口为465
        """
        self.smtp_server = smtp_server  # 使用qq转发需要用到，可以在QQ邮箱设置中查看并开通此转发功能
        self.smtp_port = port  # smtp默认的端口是465
        # 接受者可以是多个，放在列表中
        self.recever = recever
        self.sender = sender
        self.password = password  # 该密码是配置qq邮箱的SMTP功能的授权码
        self.msg = MIMEMultipart()
        self.msg['Subject'] = title  # 邮件标题
        self.msg['From'] = self._format_addr(u'{} <{}>'.format(from_who, self.sender))

    # 添加文字信息
    def addTextMsg(self, text):
        text_plain = MIMEText(text, 'plain', 'utf-8')
        self.msg.attach(text_plain)

    # 添加图片
    def addImageMsg(self, imgPath):
        extend = imgPath.split('.')[-1]
        with open(imgPath, 'rb')as f:
            sendimagefile = f.read()
            filename = md5(sendimagefile).hexdigest() + '.' + extend
        image = MIMEImage(sendimagefile)
        image.add_header('Content-ID', '<image1>')
        image["Content-Disposition"] = u'attachment; filename={}'.format(filename)
        self.msg.attach(image)

    # 添加附件
    def addFile(self, filePath):
        extend = filePath.split('.')[-1]
        with open(filePath, 'rb')as f:
            sendfile = f.read()
            filename = md5(sendfile).hexdigest() + '.' + extend
        # 构造附件
        text_att = MIMEText(sendfile, 'base64', 'utf-8')
        text_att["Content-Type"] = 'application/octet-stream'
        text_att["Content-Disposition"] = u'attachment; filename="{}"'.format(filename)
        self.msg.attach(text_att)

    # 添加html格式
    def addHtml(self, html):
        # 构造html
        # 发送正文中的图片:由于包含未被许可的信息，网易邮箱定义为垃圾邮件，报554 DT:SPM ：<p><img src="cid:image1"></p>
        text_html = MIMEText(html, 'html', 'utf-8')
        self.msg.attach(text_html)

    # 格式化邮件地址
    def _format_addr(self, s):
        name, address = parseaddr(s)
        return formataddr((Header(name, 'utf-8').encode(), address))

    # 发送邮件
    def sendEmail(self):
        server = smtplib.SMTP_SSL(self.smtp_server, self.smtp_port)  # 链接服务器
        server.set_debuglevel(1)  # 打印出和SMTP服务器交互的信息
        server.login(self.sender, self.password)  # 登录
        server.sendmail(self.sender, self.recever, self.msg.as_string())  # 发送邮件
        server.quit()  # 退出
        print('邮件发送成功')


if __name__ == '__main__':
    smtp_server = "smtp.qq.com"  # smtp服务地址
    port = 465  # 端口号
    recever = ['xxx@qq.com']  # 接收人列表可以是多个
    sender = "xxx@qq.com"  # 发送人邮箱
    password = ""  # 如果是qq邮箱的话该密码是配置qq邮箱的SMTP功能的授权码
    title = '你好'
    from_who = 'felix'  # 发送人姓名

    # 实例化对象
    autoEmail = autoSendEmail(sender=sender, recever=recever, password=password, title=title, from_who=from_who,
                              smtp_server=smtp_server, port=port)
    # 单纯发送文字
    autoEmail.addTextMsg('你好啊')
    # 以附件的形式发送图片，这种方式可以直接用addfile代替
    autoEmail.addImageMsg('felix.jpeg')
    # 发送附件
    autoEmail.addFile('你好.py')
    autoEmail.addFile('felix.jpeg')
    html = """
        <html>  
          <head></head>  
          <body>  
            <p>Hi!<br>  
               How are you?<br>  
               Here is the <a href="http://www.baidu.com">link</a> you wanted.<br> 
            </p> 
            <img src="http://img.zcool.cn/community/01f09e577b85450000012e7e182cf0.jpg@1280w_1l_2o_100sh.jpg"></img>
          </body>  
        </html>  
        """
    # 以html的形式发送文字，推荐这个，因为可以添加图片等
    autoEmail.addHtml(html)
    # 发送邮件
    try:
        autoEmail.sendEmail()
    except Exception as e:
        print(e)
        print('邮件发送失败')
