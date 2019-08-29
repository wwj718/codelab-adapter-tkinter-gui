'''
pip install guizero loguru
'''
import platform
import atexit
import webbrowser
import sys
import tkinter as tk  # todo 现代化的ui ttk
from tkinter.messagebox import showerror
from random import choice
from guizero import App, Text, Picture, PushButton, info, error, MenuBar, CheckBox, TextBox
from loguru import logger


class Gui:
    def handle_delete_window(self):
        self.exit()

    def __init__(self, logger=logger):

        if platform.system() != "Darwin":
            app_height = 300
        else:
            app_height = 200
        app = App(title="Codelab Adapter v2", width=300, height=app_height)
        self.app = app
        self.slogan = Text(self.app, height=5, text="Everything Is Message!")
        self.slogan.text_color = (108, 108, 108)
        self.slogan.text_size = 18
        self.app.tk.wm_protocol("WM_DELETE_WINDOW", self.handle_delete_window)
        self.logger = logger
        self.menubar = MenuBar(
            self.app,
            toplevel=[
                "language",
                "帮助",
                '插件',
                '关于',
                "日志",
            ],  # todo? "烧录固件"
            options=[
                [["简体中文", self.change_to_zh], ["english", self.change_to_en]],
                [
                    ["实验室(Lab)", self.help_open_lab],
                    # ["社区(Community)", self.help_open_community],
                    ["文档(Document)", self.help_open_docs],
                    ["调试(Debug)", self.help_open_message_browser],
                    ["view log", self.help_open_web_log_page],
                    ["https校验(verify)", self.ssl_help],
                ],
                [["更新插件(Update extensions)", self.update_extensions_dir],
                 ["查看目录(Directory)", self.show_extensions_dir],
                 ["下载(Download)", self.handle_download_extension]],
                [
                    ["about codelab_adapter", self.show_about],
                    ["license", self.show_license],
                    ["version", self.show_version],
                    ["why", self.show_why],
                    ["fun", self.show_fun],
                    ["changelog", self.show_changelog],
                    # ["python3 path",self.show_pip3_path]
                ],
                # [["日志目录", self.show_log_dir], ["查看日志", self.show_log]],
                [["目录(Directory)", self.show_log_dir]],
                # [ ["microbit",self.flash_microbit] ]
            ])
        self.button1 = PushButton(
            self.app,
            command=self.webui,
            text="Web UI",
            # height=5,
            # grid=[1, 0]
        )
        # mac os 10.14 bug
        self.button2 = PushButton(
            self.app,
            command=self.exit,
            text="退出",
            # width=10,
            # height=5,
            # grid=[1, 0]
        )

        self.app.tk.report_callback_exception = self.report_callback_exception

    def report_callback_exception(self, exc, val, tb):
        showerror("Error", message=str(val))

    def run(self):
        atexit.register(self.exit)
        self.app.display()

    def change_to_zh(self):
        self.button2.text = "退出"
        try:
            self.menubar.tk.entryconfigure(0, label="language")
            self.menubar.tk.entryconfigure(1, label="帮助")
            self.menubar.tk.entryconfigure(2, label="插件")
            self.menubar.tk.entryconfigure(3, label="关于")
            self.menubar.tk.entryconfigure(4, label="日志")
        except Exception as e:
            # windows下索引从1开始
            self.menubar.tk.entryconfigure(1, label="language")
            self.menubar.tk.entryconfigure(2, label="帮助")
            self.menubar.tk.entryconfigure(3, label="插件")
            self.menubar.tk.entryconfigure(4, label="关于")
            self.menubar.tk.entryconfigure(5, label="日志")

    def change_to_en(self):
        self.button2.text = "exit"
        try:
            self.menubar.tk.entryconfigure(0, label="language")
            self.menubar.tk.entryconfigure(1, label="help")
            self.menubar.tk.entryconfigure(2, label="extensions")
            self.menubar.tk.entryconfigure(3, label="about")
            self.menubar.tk.entryconfigure(4, label="log")
        except Exception as e:
            self.menubar.tk.entryconfigure(1, label="language")
            self.menubar.tk.entryconfigure(2, label="help")
            self.menubar.tk.entryconfigure(3, label="extensions")
            self.menubar.tk.entryconfigure(4, label="about")
            self.menubar.tk.entryconfigure(5, label="log")

    def ssl_help(self):
        self.logger.debug("open ssl_help")

    def help_open_docs(self):
        self.logger.debug("help_open_docs")
        webbrowser.open('https://codelab-adapter-docs.codelab.club')

    def help_open_message_browser(self):
        self.logger.debug("help_open_message_browser")

    def help_open_web_log_page(self):
        self.logger.debug("help_open_web_log_page")

    def help_open_lab(self):
        self.logger.debug("help_open_lab")

    def show_log_dir(self):
        self.logger.info("show_log_dir")

    def update_extensions_dir(self):
        self.logger.debug("update dir: {}、{}、{}".format(
            "extensions", "servers", "src"))

    def show_extensions_dir(self):
        self.logger.debug("show_extensions_dir")

    def show_about(self):
        self.logger.debug("show_about")

    def show_license(self):
        self.logger.debug("show_license")

    def show_version(self):
        self.logger.debug("show_version")

    def show_why(self):
        self.logger.debug("show_why")

    def show_fun(self):
        # 每天一句俏皮话/诗词/计算机
        funs = [
            "预测未来的最佳方式就是去创造它。 --Alan Curtis Kay",
            "What a computer is to me is it’s the most remarkable tool that we’ve ever come up with, and it’s the equivalent of a bicycle for our minds. --Young Steve Jobs",
            "学习编程能帮你组织、表达和分享你的想法，就像学习写作一样。 --Mitchel Resnick",
            "学习是必须亲力亲为的，教育则是外界加诸你身上的。 --Joi Ito"
        ]
        info("fun", choice(funs))

    def show_changelog(self):
        self.logger.debug("show_changelog")
        webbrowser.open('https://adapterv2.codelab.club/changelog/')

    def handle_download_extension(self):
        self.logger.debug("download_extension")

    def exit(self):
        self.logger.info("Exit Safely!")
        sys.exit(0)

    def webui(self):
        self.logger.debug("open webui")


if __name__ == '__main__':
    Gui().run()
