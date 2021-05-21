# VSCode QQ 快捷图片插入脚本
用于在Linux中用VSCode QQ中快速插入发送图片命令的脚本\\
用法：
1. **用Linux包管理器安装`xclip`**
2. 下载Python脚本[qq_image.py](https://github.com/Microwave-WYB/vscodeqq-image-shortcut/blob/main/qq_image.py)，修改`img_dir`变量为本地图片目录，注意必须在目录后加上`/*`以表示目录下所有文件
3. 在终端（VSCode终端也可以，更方便）运行脚本，会提示输入图片路径，此时有三种方法插入图片：
    - 直接回车：插入图片目录下最新的文件
    - 手动输入图片绝对路径
    - 从文件管理器中直接拖动文件到终端，然后回车
4. 此时图片发送命令已经复制到了剪贴板，在VSCode QQ中直接粘贴并发送即可
