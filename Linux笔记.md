Linux笔记
第一章：Linux系统安装
	查看Linux系统内核信息
		uname -a
	Linux虚拟机安装，1G-2G内存，20G-30G硬盘存储
	查看Linux系统版本信息
	cat /etc/redhat-release
		/etc/CentOS-release
		/etc/SuSE-release
	查看Linux内存信息
	free -m
	cat /proc/meminfo
	查看CPU信息
	cat /proc/cpuinfo
	查看硬盘设备信息
	fdisk -l
	df -Th
	cat /proc/partitions

	VMware tools工具安装
		cd /media/cdrom（进入到虚拟光驱的文件夹里，cdrom的名称为VMware Tools）
		cd /run/media/username/cdrom（RHEL7）
		tar xf VMwareTools-10.1.5-5055693.tar.gz -C /tmp（将安装包解压到指定目录tmp）
		cd /tmp/vmware-tools-distrib（进入解压出来的文件夹里）
		./vmware-install.pl（执行安装文件）可使用‘-d’选项，表示所有的交互式问答都以默认作为回执

	关闭防火墙
	systemctl stop firewalld（关闭运行中的防火墙）
	systemctl disable firewalld（开机防火墙服务禁止自启动）
	systemctl status firewalld（查看当前防火墙状态） 

	关机
	systemctl poweroff
	poweroff／init 0／shutdown／halt
	重启
	systemctl reboot
	reboot／init 6 

第二章：目录文件结构与管理
	
	掌握常用目录的作用: 
	/bin：表示普通用户和系统用户，超级用户都可以调用的指令
	/sbin：系统用户和超级用户可以调用的指令
	/boot：系统启动引导相关的grub文件都在boot引导目录中
	/home：普通用户账户家目录的存放目录
	/root：超级用户的家目录
	/dev：存放系统硬件设备
	/etc：系统启动，用户权限，应用程序等配置文件的主目录
	/lib：32位库文件存放目录
	/lib64：64位库文件存放目录
	/media：RHEL6及之前的操作系统，外接设备默认存放路径 /media/kingston
	/run：RHEL7外接设备默认存放路径 /run/media/username/kingston
	/mnt：建议将磁盘设备挂载到当前目录的子目录中使用
	/proc：系统进程信息和系统设备信息存放目录（基于内存）
	/tmp：临时文件存放目录，主要针对普通用户
	/var/tmp：系统程序文件存放目录，主要针对系统用户
	/usr：用户自定义配置目录
	/var：业务数据存放目录
	命令 选项 参数
	ls   -l  /boot

	根据文件颜色识别文件属性
	蓝色 目录
	黑色 普通文件
	绿色 可执行文件
	红色 压缩文件
	紫色 图片或其他类型的文件
	浅蓝色 符号链接文件
	黑底黄字 设备文件

	常用快捷键
	 Tab键：自动补齐
	 Ctrl+U：清空至行首
	 Ctrl+K：清空至行尾
	 Ctrl+L：清屏
	 Ctrl+C：取消本次命令编辑
	 Ctrl+A：光标移动到最前
	 Ctrl+E：光标移动到最后
	 反斜杠“\”：强制换行
	 Ctrl+shift+t：在已经生成的终端中打开新的终端
	 Ctrl+d：在终端没有字符的状态下，结束当前终端（exit）
	 Ctrl+shift+“+”：增大字符显示
	 Ctrl+“-”：缩小字符显示
	 Ctrl+Page UP：多终端时，向前翻页
	 Ctrl+Page DOWN：多终端时，向后翻页
	 Alt+number：根据终端位置，快速切换到数字对应的终端
	 Ctrl+shift+c：复制
	 Ctrl+shift+v：粘贴

	ls	列出目录内容
	 	-l：以长格式形式查看文件或目录的详细信息（文件类型，权限，链接数，属主属组，文件大小，时间信息，文件名及路径）
	 	-h：以人性化方式计算文件或目录的大小
	 	-d：查看目录本身的属性，不加时查看的是目录中的子目录及子文件
	 	-a：查看所有文件和目录（包含隐藏和非隐藏）
	 		-R：递归式的查询目录中的子目录及子文件
	pwd 显示当前工作目录
	cd 切换工作目录
	 	cd ..：回到上一级目录（当前路径的父目录）
	 	cd -：回到上一次工作过的目录
	 	cd directory：切换到指定目录
	 		相对路径：只能在某个特定的环境或目录下才能执行的操作（不以“/”开始的路径）
	 		绝对路径：在任意位置都可调用并执行的操作（以“/”开始的路径）
	touch	创建文件，更新文件时间标记
 	mkdir	创建目录
 		-p 递归式创建目录及子目录
 	rm		删除文件
 		-r：递归式删除文件或目录
 		-f：强制删除
 		shred /boot/grub2/grub.cfg
 	rmdir	删除空目录
	mv		移动（mv 源文件路径 目标路径），为文件或目录重命名
 	cp		拷贝
 		cp 源文件 目标路径
 		cp时，如果目标路径没有指定，默认保存为源文件名称
 			如果在目标路径指定名称，则可以为复制文件重命名
 			同时复制多个文件时，重命名无效
 			复制目录可以使用“-r”选项，将目录复制到指定路径下
 	cat		查看文件内容
 	ln 		建立链接（默认建立为硬链接，-s选项表示创建软连接）
 		硬链接：源文件的副本，对于系统来说，文件始终是同一个文件
 			每创建一次，文件的链接数都会加一，文件的节点数始终不变
 			当用户对任意硬链接文件操作时，所有文件同时发生变化
 		软链接（符号连接）：源文件的快捷方式，此时创建的是新文件 -s
 			软链接生成后，源文件链接数不会变化，文件将被分配一个新的节点数
 			当用户对软连接文件操作时，被链接的文件及硬链接文件会同时发生变化
 		硬链接有两点限制：
 			1.硬链接创建不可以跨文件系统
 			2.硬链接不可以为目录创建
 	“.”     当前目录
 	“..”    上一级目录

第三章：常用指令与vim使用
	指令的分类：
	内部命令和外部指令
	内部指令：Shell自带的命令，比如cd、history，内部指令是不可删除的（系统默认解释器为bash）
	外部命令：一些软件安装后添加的命令，比如ls、cp，外部指令可根据安装包或指令的路径删除
	如何使用帮助：
	常见的指令帮助使用有man和help
	“man+指令”可以查看指令的帮助手册
	help的使用根据内部和外部，格式有差异
	内部指令：“help+内部指令”
	外部指令：“外部指令 --help”
	
	shell：终端内的指令‘翻译器’
	bash：shell解释器的版本，除此之外，还有csh，tcsh，zsh等
	终端：在图形化Linux配置中，给用户提供指令输入的编辑器

	more	分页查看文件内容
		空格向下翻页，直至文件结束，按q结束浏览
	less	逐行查看文件内容
		空格翻页查看，‘／+关键词’可以搜索，‘n’向下查找关键词‘N’向上查找关键词，按q结束浏览
	head	查看文件头10行（默认）
		head -n number file（head -number file）
	tail	查看文件后10行（默认）
		tail -n number file（tail -number file）
	grep	过滤文件内容
		-v  取反
		-n  显示关键词在文件中的行数
		-i  搜索时忽略被搜索词的大小写
		-AX X为数字，表示搜索时同时显示关键词后X行
		-BX X为数字，表示搜索时同时显示关键词前X行
	du		统计目录内容大小
		-s  显示汇总信息
		-h  以人性化方式显示大小
	wc		统计文件内容
		默认显示信息，依次为行数，关键词数，文件大小
		-l 统计行数
 	alias	命令别名建立，格式为：新指令=‘原指令 + 选项’
 		建立时有三种方式
 		1.在当前终端新建别名，只有当前终端生效，其他终端不生效，同时退出终端后失效
 		2.在当前用户的家目录中，找到隐藏文件bashrc(~/.bashrc)，在文件中添加alias，再次登陆生效，针对的是当前用户
 		3.在/etc/bashrc文件中，添加alias，全局生效，所有登陆用户都可调用
 		alias simple=‘ls -lh’
 			unalias
	find	实时查找
		根据文件名查找
			find /etc -name passwd
		根据文件大小查找
			find /etc -size -1k
		因为find对管道支持比较弱，所以可以借助exec扩展选项
			find /etc -size +1M -exec ls -lh {} \;
			注：‘-’表示小于，‘+’表示大于，-exec通常需要和‘空格\;’一起使用，格式不完整，则指令不可正确执行
	gzip 与 bzip2	压缩文件
 		压缩时，默认压缩比为6，压缩区间为1-9，9为最高压缩
 		解压缩时，对应指令为gunzip，bunzip2
 	file 查看文件类型
 	dd	复制
 		dd if=/dev/zero of=testfile bs=1M count=100生成100M的文件
 		dd if=/dev/sda of=/tmp/mbr.hex bs=512 count=1
 	tar		目录打包备份
 		-c 创建打包压缩的文件
 		-f 将指定的文件或目录打包为文件
 		-v 显示压缩或解压缩的进度
 		-j bzip2格式的文件压缩
 		-z gzip格式的文件压缩
 		-J xz格式的文件压缩
 		-C 解压缩时指定解压路径，默认为当前目录
 		-x 解压缩文件

 	VIM编辑器使用
		Vim编辑器的三种工作模式：
		命令模式（默认模式）：复制，粘贴，剪切，切换到其他模式
		输入模式（编辑模式）：a\i\o，针对每个字符进行编辑，删除
		末行模式（扩展模式）：保存，退出，保存并退出，字符替换等
		光标方向移动

	命令模式：
		向下翻页：Page Down或Ctrl+F
		向上翻页：Page Up或Ctrl+B
		行内快速跳转
		跳转至行首：Home键或者“^”、数字“0”
		跳转到行尾：End键或“$”键
		行间快速跳转
		跳转到文件首行：1G或者gg
		跳转到文件末行：G
			#G 其中#代表数字，#G表示跳转到文件中的第#行
		直接输入数字+回车
			表示从当前行开始计算，跳到文件位置的累加行
		操作类型

		剪切（删除）
		删除当前光标处单个字符：x或者Del
		剪切当前行：dd
		剪切从光标处开始的#行内容：#dd #表数字
		删除当前光标前到行首所有内容：d^
		删除当前光标到行尾所有内容：d$
		
		复制
		复制当前行：yy
		复制从光标开始处的#行内容：#yy
		
		粘贴
		粘贴到当前行下：p
		粘贴到当前行上：P
		
		撤销
		取消最近一次操作：u
		反撤销：ctrl+r
		
		查找
		从上而下在文件中查找字符串“word”：/word
		从下而上在文件中查找字符串“word”：?word
		定位下一个匹配的被查找字符串：n
		定位上一个匹配的被查找字符串：N

		保存
		保存并退出当前编辑：ZZ
		shift+‘；’   ：set number

	输入模式：
		a：在当前光标所在位置的后面输入字符
		i：在当前光标所在位置的前面输入字符
		o：在当前光标所在位置的下面重新开启一行输入字符
		A：跳转到当前光标所在行行尾输入字符
		I：跳转到当前光标所在行行首输入字符
		O：在当前光标所在位置的上面重新开启一行输入字符

	末行模式
		显示行号
		:set nu
		取消显示行号
		:set nonu
		  
		保存
		保存修改内容：‘:w’
		另存为：‘	:w /路径/文件’
		未修改退出：‘:q’
		放弃修改强制退出：‘:q!’
		保存并退出：‘:wq’

		打开新文件编辑
		:e /路径/文件
		读入文件内容到当前编辑
		:r /路径/文件 
		将当前行中查找到的第一个字符“old” 替换为“new”
		:s/old/new 
		将当前行中查找到的所有字符串“old” 替换为“new”
		:s/old/new/g
		在行号“#,#”范围内替换所有的字符串“old”为“new”
		:#,#s/old/new/g
		在整个文件范围内替换所有的字符串“old”为“new”
		:%s/old/new/g 

第四章：Linux软件安装
	常见的安装方式有三种：源码包安装，rpm指令安装，yum安装
	源码包安装：
	下载源代码安装包文件
	步骤1：tar包解压缩
	用途：解压并释放源代码包到指定的目录/usr/src/
	步骤2：./configure 配置
	用途：设置安装目录、安装模块等选项(/usr/src/httpd-2.4.6/)
	步骤3：make 编译
	用途：生成可执行的二进制文件Makefile
	步骤4：make install 安装
	用途：复制二进制文件到系统，配置应用环境并使用应用软件
	卸载：
		make uninstall/make clean
	
	进入安装目录后，找到bin目录（/usr/local/apache2/bin）
	执行./httpd，开启httpd程序
	监听指令为netstat
	netstat是网络信息监听指令
		-l listening，获取正在监听的状态
		-n 显示端口信息
		-t TCP
		-u UDP
		-p program／PID
	netstat -lntup | grep :80
	打开firefox或本地用curl指令访问127.0.0.1，即可看到站点信息
	需要修改主机页面，可以编辑/usr/local/apache2/htdocs/index.html
	刷新firefox即可

	rpm指令管理
	针对已安装软件
	rpm -qa：查询所有已安装软件的rpm包信息，列出包的版本
	rpm -qi 软件名：列出已安装软件的详细信息
	根据指令搜索包的名称
	which vim（which搜索指令在系统中的路径）
	rpm -qf 文件/目录/指令 查看该文件是由哪个rpm包所提供
	针对未安装软件
	rpm -qpl 包.rpm  选项p表示package，后面需要写包的完整路径信息
		qpl表示列出这个包在安装之后生成哪些文件和目录
	rpm -qpi 包.rpm  查询未安装包的详细信息
	安装与卸载
	rpm -ivh 包.rpm
		i表示安装，v表示显示安装过程，h表示以‘#’作为进度，显示安装进度
	rpm -e 包的名称
		移除指定的rpm包

	yum软件管理
	首先，仓库源需要满足两点要求
	1.仓库文件必须存放在/etc/yum.repos.d/目录中
	2.仓库源文件的后缀必须以‘.repo’结尾

	repo文件格式：
	[base]
		中括号的名称为仓库源名称，通常为字母和数字
	name=my new repo cdrom
		name表示对yum源的描述，方便管理当前yum
	baseurl=file:///mnt/cdrom
		baseurl=http://10.0.0.1/packages
		baseurl表示声明yum可以管理并使用的rpm包路径，可以基于本地，也可以基于网络
	enabled=1
		enabled表示当前仓库是否开启，1为开启，0为关闭，此项不写默认为开启
	gpgcheck=0
		gpgcheck表示安装rpm包时，是否基于公私钥对匹配包的安全信息，1表示开启，0表示关闭，此项不写默认为验证

	yum clean all	     清空缓存信息
	yum list [包的名称]   列出所有[指定]包的信息
	yum info 包的名称     显示包的详细信息
	yum install 包的名称  安装指定的rpm包
	yum remove 包的名称	 移除指定的rpm包
	yum search 关键词     根据关键词，在已发现的repo源中搜索包含关键词的rpm包
	yum provides 命令     根据命令，在已发现的repo源中搜索安装指令的rpm包
	yum history	list/info/undo/redo number
			history可以列出，查看，重装，反安装对应的包，但是是以yum指令的操作顺序为依据的，所以需要加指定的数字执行

第五章：账号与权限管理
	用户账户分类
	超级用户：UID=0
	程序用户：RHEL5/6，UID=1-499；RHEL7，UID=1-999
	普通用户：RHEL5/6，UID=500-65535；RHEL7，UID=1000-60000

	passwd文件
	simplexue:x:500:500:www.simplexue.com:/home/simplexue:/bin/bash
	字段1：用户名
	字段2：密码占位符
	字段3：uid
	字段4：gid
	字段5：用户描述信息
	字段6：家目录
	字段7：登录shell（用户登陆shell为/bin/bash表示当前用户可以登陆，/sbin/nologin表示当前用户不被授权登陆）

	shadow文件
	字段1：用户名
	字段2：通过sha-512加密过得密码
	字段3：最后一次修改密码距离1970年1月1日的天数间隔
	字段4：密码最短有效期 （至少多久）
	字段5：密码最长有效期
	字段6：密码过期前7天警告
	字段7：账户过期后，被锁定的天数
	字段8：账号失效时间距离1970年1月1日的天数间隔
	字段9：未分配功能

	group文件
	字段1：组名称
	字段2：组密码占位符
	字段3：GID
	字段4：组成员

	用户与组管理
	useradd指令：
		1.新建用户时，系统会将/etc/skel中的目录及文件拷贝到新建用户的家目录中
		2.在/var/spool/mail中，新建用户名的邮箱
		3.在passwd和shadow文件中，增加用户信息
	userdel [-r] username
		不加-r选项，只删除passwd和shadow文件中的用户信息
		加-r选项，删除passwd和shadow文件中的用户信息，同时删除用户的家目录和邮箱

	usermod
		对已存在的账户做属性修改
		-s 修改用户的登陆shell
		-L 账户锁定
		-U 解锁账户

	passwd密码修改
		root：
		1.不需要知道当前的密码
		2.设置新密码时，不需要遵循密码要求（1.不能少于8个字符，2.满足复杂度要求）
		普通用户：
		1.需要知道当前密码
		2.设置新密码时，必须遵循密码要求

	groupadd
		增加新组，组创建时可以指定组的GID等属性
	groupmod
		修改组的属性，比如名称，GID等
	groupdel
		删除组，但是只能针对附加组，主组无法删除

		用户创建时，默认的属性（比如UID，GID，是否创建家目录，创建邮箱等）都是通过/etc/login.defs文件控制的，修改此文件的属性，会影响以后创建的所有用户
	如果需要对现存账户的属性做修改，可以借助chage指令，修改用户的密码策略，也可通过编辑/etc/shadow
	文件修改（不推荐）
	比如：chage -l username，查看用户的密码策略
		chage -M 90 username，将用户的密码有效期修改为90天

	文件和目录的权限为rwx
		针对文件：
		r表示可以读取文件
		w表示可以对文件内容做修改
		x表示文件可执行
		针对目录：
		r表示可以列出目录内容
		w表示可以在目录中增删改查
		x表示可以进入目录，同时可以查看目录中文件的详细信息

		rwx对应的数字为421，所以文件或目录的最大权限为777
		修改文件权限的指令为chmod
		u表示user，属主权限位
		g表示group，属组权限位
		o表示other，其他用户权限位
		a表示所有，等于ugo
		所以设置权限时，可以使用chmod ugo（a） +／- rwx
			比如：chmod u-r file／chmod a+x file等
			也可使用数字代表权限，对应的三个数字即为属主、属组、其他用户
			比如：chmod 640 file

		文件属性分为10个字段
		第一字段为文件属性
		第二至四字段为属主权限
		第五至七字段为属组权限
		第八至十字段为其他用户权限
		文件属性中，‘-’表示文件，‘d’表示目录，‘l’表示符号链接，‘b’表示块设备，‘c’表示特殊字符设备

		修改文件的属主属组，可以使用chown和chgrp指令
		chown即可单独修改属主，也可单独修改属组，也能同时修改属主属组
		chgrp只能修改属组
		chown 属主：属组 file／directory   
		chown 属主.属组 file／directory
		chgrp 属组 file／directory

	扩展权限控制
		因为默认的属主属组只能控制一个用户和一个组，无法针对每个用户做权限控制
		所以借助acl属性，完善权限控制
		设置：setfacl（-m设置acl，针对用户，关键词为‘u’，针对组，关键词为‘g’，设置时，权限不能为空）
		获取：getfacl
			setfacl -m u:tom:rw- /file
			setfacl -m u:jerry:- /file
			setfacl -m g:IT:rw- /file
			getfacl /file 
		移除权限（-x移除acl，移除权限时，无需指定权限，针对用户或组即可）
			setfacl -x u:jerry /file

		SUID：针对特殊指令，做提权，不建议随意更改默认指令属性
			chmod u+s 指令后，表示用户在使用指令时，借助的是管理员的身份
			chmod 4755
		SGID：主要针对目录，方便同组成员可以互相编辑文件
			chmod g+s 目录后，组成员创建的文件或目录，属主为自己，属组自动继承父目录
			chmod 2770
		粘滞位：针对other用户，彼此可以看到创建的文件，但是不可以修改删除
			chmod o+t 目录后，所有的other用户在目录中都拥有对自己文件的完全控制权限
			chmod 1777 
第六章：文件系统建立与磁盘配额
	创建磁盘分区的步骤：
	1.添加并识别硬件设备
		fdisk -l可以看到新加的设备
		ls -l /dev/sda
	2.创建分区并识别分区
		fdisk /dev/sdb
		partprobe /dev/sdb
		（rhel5和rhel7识别新分区通过partprobe识别，rhel6识别新分区通过partx识别）
		刷新后，可以查看文件是否识别新分区cat /proc/partitions 
		fdisk /dev/sdb时，常用的选项 
			n 创建新的磁盘分区
			d 删除已存在的磁盘分区
			l 查看支持的磁盘分区类型
			t 转换分区类型
			p 查看磁盘的分区信息
			w 保存修改并退出
			q 不保存直接退出
	3.制作文件系统
		mkfs.ext4 /dev/sdb1
	4.制作磁盘标签（option）
		e2label /dev/sdb1 newpart
	5.创建挂载点
		mkdir /mnt/ext
	6.将分区信息写入文件系统分区表
		vim /etc/fstab 
		LABEL=newpart     /mnt/ext     ext4    defaults        0 0
		第一列表示待挂载的文件系统，挂载方式可以是设备路径（/dev/sdb1），可以是LABEL，可以是UUID
		第二列是挂载点，表示设备使用后，从那个接入点使用磁盘空间
		第三列是文件系统类型，制作文件系统时的格式写在这个位置
		第四列是挂载时的磁盘参数，默认包含可读可写等
		第五列是是否对磁盘做dump备份
		第六列是是否对磁盘做fsck检查
		查看设备信息使用blkid指令
	7.挂载文件系统
		首先查看已存在的磁盘挂载信息
		df -Th
		然后执行mount -a，表示读取fstab文件，将未挂载的文件系统参数包含挂载上

	创建windows格式的磁盘分区，在以上操作步骤中，第2步，建好分区，按‘t’修改磁盘分区类型
	windows的system ID建议修改为‘b’
	保存退出后，刷新磁盘分区，再创建挂载点，制作文件系统

	swap虚拟内存创建，在以上操作步骤中，第2步，建好分区，按‘t’修改磁盘分区类型
	swap的system ID修改为‘82’
	制作虚拟内存的指令为mkswap
	swap在永久挂载时，没有挂载点，fstab文件格式如下
		/dev/sdb3	swap  swap   defaults   0 0
	开启虚拟内存的指令为swapon -a，将开启所有fstab文件中的swap分区
	关闭使用swapoff，如果只是关闭一个分区，swapoff /dev/sdb3，关闭所有swapoff -a
	查看虚拟内存空间变化可以使用free -m

		磁盘配额
		管理员可以为用户所能使用的磁盘空间进行配额限制，每一用户只能使用最大配额范围内的磁盘空间。
		即可对用户存储文件数量做限制，也可对用户存储文件大小做限制
	磁盘配额建立及测试验证
	1.挂载的同时需要为文件系统添加支持配额的选项
	/dev/sdb1 /mnt/ext ext4 defaults,usrquota,grpquota 0 0
		配额限制即可通过mount指令，一次性添加，也可写入fstab，永久使用
		设备启用配额，需要将文件系统重载
		umount /mnt/ext；mount -a（或mount -o remount /mnt/ext）
		验证参数识别
		mount | grep sdb1
	2.在分区中生成配额文件quota.user和quota.group
		quotacheck -augcv
		-a 扫描所有支持配额的分区
		-u 扫描磁盘计算用户所占用的文件数
		-g 扫描磁盘计算组所占用的文件数
		-c 创建配额文件aquota.user和aquota.group
		-v 显示详细信息
	执行后，会检查所有支持磁盘配额的分区，如果分区之前有配置配额，开启又关闭，再次开启会有配置文件被更新
	如果是第一次创建磁盘配额，那么会提示之前没有任何配额文件
	3.为用户建立配额信息
		edquota -u user1 编辑用户user1的配额
		一共有六个字段
		Filesystem                   blocks       soft       hard     inodes     soft     hard
		/dev/sdb1                   	0         40960      51200       0        8        10
		前三个字段表示针对文件空间限制，后三个字段表示针对文件数量限制
		第一个字段表示用户在文件系统中已占用的空间统计
		第二个字段表示用户创建文件时，文件空间的警告阈值，超过数值则提示（软限制一般为提醒，小于硬限制即可，不设置或者超过硬限制都无意义）
		第三个字段表示用户的空间限制，最大使用的磁盘空间
		第四个字段表示用户已创建文件的数量统计
		第五个字段表示用户在文件系统中创建文件的数量警告阈值，超过数量则提示
		第六个字段表示用户创建文件的数量限制，最大创建文件数量
		以上六个字段，主要针对2，3，5，6做设置
	4.开启/关闭配额功能
		quotaon/quotaoff
		quotaon -a
		-a 表示开启支持配额功能所有分区
	切换用户，进入指定目录，做测试，同时记得修改被测试分区的文件系统权限，比如chmod 777 directory或setfacl
	5.查看配额信息
		查看配额信息的方式有两种。
		quota -u 用户名 只查看用户的配额信息
		quota -g 组名 只查看组的配额信息
		repquota 设备 查看设备内的配额信息
第七章：LVM和RAID
	LVM创建及使用
	LVM底层文件系统标签为‘8e’
	创建逻辑卷，首先满足前面实验的7个步骤，那么在第二步，创建并转换完分区，识别后
	将磁盘分区初始化为物理卷，pvcreate /dev/sdb5   查询pvs
	将初始化的物理卷加入卷组，vgcreate myvg /dev/sdb5
	在已有的卷组中，创建逻辑卷，lvcreate -L 300M -n mylv myvg  查询lvs
		vgcreate和lvcreate时，必须指定卷组和逻辑卷名称，逻辑卷需指定大小

	拉伸及缩小
		当卷组空间足够分配给逻辑卷时，拉伸LVM分为两步：
		1.拉伸逻辑卷；2.通知文件系统
		EXT文件系统：
			lvextend -L +300M /dev/myvg/mylv   或者lvresize
			resize2fs /dev/myvg/mylv 	通知文件系统
		XFS文件系统：
			lvextend -L 600M /dev/myvg/mylv
			xfs_growfs /dev/myvg/mylv
			注，XFS文件系统不支持缩小 
		
		当卷组空间不够分配给逻辑卷时，拉伸LVM分为五步：
		1.新建磁盘分区或磁盘；2.将新建磁盘或分区初始化为物理卷
		3.拉伸卷组；4.拉伸逻辑卷；5.通知文件系统
			fdisk /dev/sdb
				创建新的磁盘分区（8e）
			pvcreate /dev/sdb6
				将分区初始化为物理卷
			vgextend myvg /dev/sdb6
				将新的物理卷空间融入卷组
			后面4，5拉伸和通知文件系统的指令同上

		缩小LVM分为四步：
		1.将挂载的文件系统下线
		2.强制磁盘检查
		3.通知文件系统缩小
		4.缩小逻辑卷
			umount /mnt/lvm
			e2fsck -f /dev/myvg/mylv
			resize2fs /dev/myvg/mylv 100M
			lvresize -L 100M /dev/myvg/mylv   或者lvreduce

		删除LVM
		1.删除或注释磁盘挂载信息
			vim /etc/fstab
		2.将挂载的文件系统下线(设备下线前记得备份)
			umount /mnt/lvm
		3.删除逻辑卷
			lvremove /dev/myvg/mylv
		4.删除卷组
			vgremove myvg
		5.删除卷组底层的物理卷
			pvremove /dev/sdb5 /dev/sdb6
		6.删除磁盘分区
			fdisk /dev/sdb
			d->6    d->5
		7.刷新磁盘分区，如果报错，在确保主机其他文件系统正常的情况下，重启主机	

	RAID
		利用3块硬盘组建RAID5
		mdadm -C /dev/md0 -n3 -l5 /dev/sd[bcd]
		-C 创建阵列存储设备
		-n 添加磁盘的数量
		-l RAID的等级
		查看RAID状态
		mdadm -D /dev/md0 查看uuid   cat /proc/mdstat（查看RAID硬盘状态）
		由于md0设备文件属于临时创建，重启系统后会失效，需要建立阵列的配置文件使其永久生效
		vim /etc/mdadm.conf
		ARRAY /dev/md0 UUID=xxxxxxxxxxxxxxxxxxxxxxx
			pvcreate /dev/md0
			vgcreate raid-vg /dev/md0
			lvcreate -L 100M -n raid-lv raid-vg 
			mkfs.xfs /dev/raid-vg/raid-lv 
			mount /dev/raid-vg/raid-lv /mnt/lvm/
			然后在挂载点写入数据，做测试
		RAID5的故障处理
			mdadm --manage /dev/md0 --fail /dev/sdb
			--fail		将设备设定为出错状态
			--remove	将设备从阵列中移除
			--add		添加设备进入阵列
				（加硬盘后，可立即执行mdadm -D /dev/md0，可以看到重建硬盘数据的过程）
		RAID阵列停用
			1.umount /dev/raid5	卸载设备
			2.取消设备开机挂载LVM
			vim /etc/fstab
			#/dev/vg_raid/lv_raid 	/mnt/raid5	ext4	defaults	0 0	注释有效内容
			3.注释后，需要lvremove，vgremove，pvremove删除阵列中创建的逻辑卷，卷组，物理卷
			4.取消设备开机加载阵列
			vim /etc/mdadm.conf
			# ARRAY /dev/md0 UUID=xxxxxxxxxxxxxxxxxxxxxxx		                                 
			    注释有效内容或者删除文件，但删除文件适用于没有其他阵列的情况下
			5.mdadm -S /dev/md0	停止md0
			6.验证
			cat /proc/mdstat
			mdadm -D /dev/md0

	1.3块硬盘组成的raid5，使用md0全部空间制作LVM，配置RAID永久生效，配置LVM永久挂载
		（文件系统类型位xfs 测试拉伸）
	2.模拟sdc故障，RAID测试移除硬盘和加新硬盘时，数据是否存在，移除所有RAID和LVM，正常重启
	3.使用主分区（500M）和逻辑分区（1G）建立LVM并永久挂载（文件系统类型为ext3，初始大小为200M，测试拉伸到1G和缩小到400M）
	4.删除所有LVM及分区，正常重启

第八章：启动流程与服务管理
	运行设置及查看
		rhel6:init 3 切换为文本模式
			  init 5 切换为图形模式
			  vim /etc/inittab
			  	文件中，id后面的数字，为3时，开机默认为文本模式，为5时，开机默认为图形模式
			  	执行指令为临时设置，修改文件为永久设置
		rhel7:systemctl isolate multi-user.target 切换为文本模式
			  systemctl isolate graphical.target  切换为图形模式  
			  以上为临时修改模式
			  systemctl set-default multi-user.target	开机默认为文本模式
			  systemctl set-default graphical.target	开机默认为图形模式
			  以上为永久修改模式
		获取当前运行级别的方法
			rhel6:runlevel
			rhel7:systemctl get-default

	修改语言设置的三种方式：
		1.yum install system-config-language
			system-config-language
		2.找到右上角用户，设置，区域和语言，修改语言
		3.vim /etc/locale.conf
			英文格式为LANG=en_US.UTF-8
			中文格式为LANG=zh_CN.UTF-8

	服务控制：
		运行状态下服务控制：
		rhel6:service 服务名称 服务控制
				service network restart/stop/start/status
		rhel7:systemctl 服务控制  服务名称
				systemctl stop/start/restart/status network
		开机自启动服务控制：
		rhel6:chkconfig 服务名称 on/off
			chkconfig vsftpd on
		rhel7:systemctl enable/disable 服务名称
			systemctl enable vsftpd
	
第九章：进程管理与计划任务
	进程管理
	ps：查看静态进程信息
		a选项表示查看所有进程信息
		u选项表示显示进程所属的用户信息
		x选项表示显示默认信息以外的信息
		STAT：
		S：当前状态为睡眠状态
		s：当前进程有多个子进程
		l：当前进程可能会开启多个子进程
		R：当前进程正在运行中
		+：表示这个进程在前台运行
		Z：表示僵尸进程
		<：表示当前进程优先级高
	top：动态查看进程信息（默认每3秒刷新一次，可以按q退出）
		M：按M表示按照内存使用量从大到小排序
		P：按P表示按照CPU使用量从大到小排序
			-d
			nice
			renice
	pgrep：表示查看指定服务的PID（进程ID值）
		-u表示查看指定程序用户的进程信息
		比如：pgrep -u named named
		第一个named为named用户，在passwd文件中，第二个进程名称named，可以通过
		ps aux | grep named获取
	pstree：以树状结构显示进程的关联信息

	Ctrl+z	前台进程调入后台
	Ctrl+c	结束进程
	jobs	查看后台进程
	fg #	将后台第#个进程在前台运行（不加数字时，jobs程序上为‘+’的程序优先被调回）
	bg #	将后台第#个进程在后台运行（不加数字时，jobs程序上为‘+’的程序优先被调回）
	&		直接将进程放在后台运行
	kill、killall	结束进程
		kill后面直接写数字时，表示是ps过滤出来的进程信息
		kill后面加%加数字时，表示结束jobs后台进程中的对应进程
		如果默认进程结束不掉，可以使用kill -9 PID强制结束进程
		killall表示同时结束多个相同程序发起的进程
			killall -9 xeyes

	at 一次性定制任务
		设置格式
		at [HH:MM] [yyyy-mm-dd]
		at>ctrl+d 结束编辑
		查询与删减
		atq（at -l）
		atrm
		at –c # 查看指定计划任务内容

	crontab 任务计划，可以在指定时间重复执行
		查看指令写入格式，可以通过cat /etc/crontab获取（分／时／日／月／周）
		用户定义的配置文件位于 /var/spool/cron/用户名
		crontab -e [-u 用户名]	编辑计划任务
		crontab -l [-u 用户名]	查看计划任务
		crontab -r [-u 用户名]	删除计划任务
			crontab -u
	date 获取或修改时间
		date 月日时分年
		date -d '+90days'

	hwclock 获取或修改BIOS时间
		-r 表示读取BIOS时间
		-w 表示将当前时间写入BIOS

	watch 根据需求执行刷新操作
		-n 3表示每3秒刷新一次

第十章：服务器加固与引导修复
	kernel升级
		确认当前系统的内核版本:
		查看当前kernel: uname -r
		查看可升级kernel: yum list kernel
		升级kernel:
		yum update kernel（需要提供可更新yum源）
		rpm -ivh kernel-3.10.0-123.1.2.el7.x86_64.rpm
		yum localinstall kernel-3.10.0-123.1.2.el7.x86_64.rpm

	查看已安装kernel版本：
		cat /boot/grub2/grub.cfg | grep -i 'red hat'
	设置kernel启动版本：（修改后重启生效）
		grub2-set-default number
		（数字按照上面文件的顺序设置，如果有3个核心，设置区间为0-2，如果设置为3的话则循环为0）
	查看设置的启动版本：
		grub2-editenv list（/boot/grub2/grubenv）
	修改grub菜单的超时时间：
		vim /etc/default/grub中GRUB_TIMEOUT=10
		grub2-mkconfig -o /boot/grub2/grub.cfg

	RHEL7密码破解
		1.添加内核参数rd.break
		2.内核加载引导系统时，根分区为只读模式挂载，修改模式为读写
		mount -o remount,rw /sysroot
			mount | grep sysroot验证是否修改成功
		3.切换到根目录chroot /sysroot
		4.修改密码passwd root
		5.修改SELinux的relabel模式
		touch /.autorelabel
		执行2次exit
		（rhel6操作 1  enter  b  passwd(getenforce enforcing setenforce 0) ）
		LANG=en

	grub2引导菜单加密
		通过命令grub2-mkpasswd-pbkdf2生成加密密码
		修改/etc/grub.d/00_header，在末尾追加（用户名与密码设置无关）
		cat << EOF
		set superusers="user1"
		password_pbkdf2 user1 Encrypted Password Of User1
		EOF
		更新配置文件以生效
		grub2-mkconfig -o /boot/grub2/grub.cfg

	修复grub
		故障原因
			grub.cfg文件丢失    shred /boot/grub2/grub.cfg   mv grub.cfg.bak
		故障现象
			grub>
		解决办法
			进行手动引导
			set root=(hd0,msdos1) 设定根为第一个硬盘的第一个分区
			linux /vmlinuz-*.el7.x86_64 root=/dev/mapper/rhel-root 	
				指定内核将根的位置交给文件系统（此处需要留意根分区的底层，是物理分区还是逻辑卷）
				注：如果系统分区不是LVM，boot目录没有独立创建，那么linux后面的路径格式为：
					linux /boot/vmlinuz-*.el7.x86_64 root=/dev/sda1
			initrd /initramfs-*.el7.x86_64.img 
				加载初始化镜像盘为硬件加载驱动（*表示核心版本和镜像版本需一致）
				注：如果系统分区不是LVM，boot目录没有独立创建，那么linux后面的路径格式为：
					initrd /boot/initramfs-*.el7.x86_64.img
			boot 引导进入系统

	grub引导故障，文件损坏或丢失
		解决办法
			在硬盘sda上安装grub2，重新覆盖原来的引导
			grub2-install /dev/sda
			让grub2自己识别不同的系统，然后按照脚本自己创建引导，并更新配置文件/boot/grub2/grub.cfg
			grub2-mkconfig -o /boot/grub2/grub.cfg

	diff 文件对比
		diff 源文件 目标文件

	救援模式管理
		关闭虚拟机，编辑虚拟机设置，选中光驱，勾选启动时链接，同时，在开启前点击进入虚拟机时
		打开固件，将CD或网卡调至最上面，F10保存退出

		选continue，继续，根分区被挂载到了/mnt/sysimages路径下

		fsck -f 磁盘分区 强制检查ext文件系统磁盘分区
		xfs_repair -L 磁盘分区 强制检查XFS文件系统磁盘分区

第十一章：网络配置与日志分析
	查看网络接口信息
		查看所有活动网络接口信息
			ifconfig（ip address）
		查看指定网络接口信息
			ifconfig 网络接口名（ifconfig eth0）

	hostname	查看主机名
		直接cat在后面加新的主机名表示临时设置主机名
	route		查看路由表
		route -n 将默认路由条目的网段信息以地址形式显示
	netstat		查看接口统计信息等
		-lntup 
	ping		测试网络连通性，后接主机名或IP
		-c 持续ping的次数，默认为持续ping
		-s ping时发送的数据包数量
	traceroute	测试主机到主机之间经过的网络节点
	nslookup	测试DNS域名解析
		可以直接加主机名或IP，也可回车后分别解析

	临时配置
		使用命令配置，简单、快速，之间修改运行中的网络参数
		适合在调试网络的过程中使用
		系统重启以后，所做的修改会失效
	固定配置
		修改配置文件实现网络参数修改
		对服务器设定固定参数时使用
		需要重载网络服务或者重启系统后生效

	Linux网络接口表示方法
		eth0 eth表示以太网卡0表示第一块网卡
		lo0	表示本地回环网卡
	设置网络接口ip以及子网掩码
		ifconfig eth0 ip地址 [netmask 子网掩码]
		ifconfig eth0 ip地址[/掩码长度]
	禁用或者重新激活网卡
		ifconfig eth0 up	或者	ifup eth0
		ifconfig eth0 down	或者	ifdown eth0
	设置虚拟网络接口
		Ifconfig eth0:0 ip地址

	添加默认网关记录
		route add default gw IP地址
	删除路由表中默认网关记录
		route del default gw IP地址
	
	以上指令都为临时设置，永久设置需要修改配置文件，或借助指令写入配置文件
	网卡配置文件的路径为/etc/sysconfig/network-scripts中
	网卡配置文件中的重要内容
		DEVICE=eth0    				设备名称
		ONBOOT=yes|no   			开机是否启用网卡
		BOOTPROTO=static|none|dhcp	网卡运行模式（前两种为手动配置固定IP，DHCP为动态获取）
		IPADDR=						IP地址
		NETMASK=  或者prefix=掩码位   子网掩码
		GATEWAY=					网关
	路由条目文件的路径与网卡一致，只是路由条目针对不同的网卡，名称要以route开始
		比如route-eth0
		10.0.0.0/8 via 192.168.1.1
		需要注意的是后面要转发的IP本机必须能通讯，否则重启网卡服务会失败

	RHEL7网卡信息查看
		查看网卡链接
		nmcli con show "static-eth0"
		查看网卡物理状态
		nmcli dev status
			ethtool eth0
		查看网卡信息
		nmcli dev show eth0
			ifconfig
		网卡配置生效
		systemctl restart network.service
			service network restart
		nmcli con reload

		网卡配置
		为网卡增加新的链接
		nmcli con add con-name "Simple" ifname eth0 type ethernet ip4 172.25.0.1/24 gw4 172.25.0.254
		为网卡设置DNS
		nmcli con modify " Simple" ipv4.dns 172.25.254.254
		如果需要启用新的链接，需要禁用之前的链接
		nmcli con modify " Simple" connection.autoconnect yes
		nmcli con modify "System eth0" connection.autoconnect no
		修改IP地址		
		nmcli con modify " Simple" ipv4.addresses 172.25.0.100/24
		增加网卡的从IP
		nmcli con modify "System eth0" +ipv4.addresses 10.0.0.1/24
		以上配置修改后，需重启网卡服务

		修改网卡名称
		1.vim /etc/default/grub
		找到GRUB_CMDLINE_LINUX行，直接到最后添加，net.ifnames=0 biosdevname=0
		2.grub2-mkconfig -o /boot/grub2/grub.cfg
		更新配置文件
		3.cd /etc/sysconfig/network-scripts/
		将网卡名称修改为ifcfg-eth0
		mv ifcfg-eno16777736 ifcfg-eth0
		vim ifcfg-eth0     NAME=eth0
		4.reboot
		重启，使网卡名称恢复为eth命名

	常用网络配置
		主机名修改的三种方式：
			hostname abc.example.com
		1.vim /etc/hostname	主机名称配置文件
		2.hostnamectl set-hostname 主机名
		3.nmtui
		DNS服务器地址保存位置
		/etc/resolv.conf
		nameserver 8.8.8.8
		主机与IP地址映射记录
		/etc/hosts
		ip地址	主机名

	team网卡绑定
	bond
		1. 创建一个team设备，名称为team0，且使用主备模式
		nmcli con add type team con-name st0 ifname team0 config '{"runner":{"name": "loadbalance"}}'
		2.设置 team0 组的 IP（V4、V6） 、网关等信息，同时设置ip 地址的获取方式
		nmcli con mod st0 ipv4.addresses '192.168.0.100/24'
		nmcli con mod st0 ipv4.method manual
		3.将指定以太网网卡设备加入team0组成网路组
		nmcli con add type team-slave con-name team0-port1 ifname eth1 master team0
		nmcli con add type team-slave con-name team0-port2 ifname eth2 master team0
		4. 查看 team0 设备连接是否已经创建
		nmcli con up team0
		teamdctl team0 state

		测试：
		ping -I team0 -c 4 192.168.0.254

		修改网卡模式
		建议修改文件，重启网卡后应用新的模式
		vim /etc/sysconfig/network-scripts/ifcfg-st0
			修改关键词为activebackup
		team网卡测试
			断开链接或停用网卡测试热备模式（两个指令的意义相同）
			nmcli dev dis eno1
			nmcli con down team0-port1
			重启链接或启用网卡测试热备模式
			nmcli dev con eno1
			nmcli con up team0-port1

	日志
		日志文件默认存放在/var/log目录中
		常用日志文件：（rsyslog监听）
		内核、公共消息日志
		/var/log/messages
		计划任务日志
		/var/log/cron
		系统引导日志
		/var/log/dmesg
		邮件系统日志
		/var/log/maillog
		用户登录日志
		/var/log/secure

		RHEL7日志监听在rsyslog基础上，新增journal监听，日志文件默认存放在/run/log/journal目录中
		常用指令：
		journalctl
		journalctl -n 10
		journalctl -p err
		journalctl -f

		日志实时监听：
		tail -f logfile / journalctl -f

第十二章：SElinux与防火墙
	SElinux
		selinux类型: Enforcing, Permissive, or Disabled
		Enforcing：既阻止用户的违规行为，同时对违规行为作日志记录
		Permissive：不对违规行为作阻止，只记录日志
		Disabled：SElinux不开启，不记录日志
		配置文件
		/etc/sysconfig/selinux（重启生效）
		图形工具
		yum install policycoreutils-gui
		system-config-selinux
		在不重启状态下，如果当前的模式为enforcing或permissive，可以通过以下指令修改为另一种，但是不可以修改为disabled

		获取当前SElinux工作状态
			getenforce
		运行时修改
		 	setenforce 0 | 1
		kernel参数的修改
		当系统启动时，需要在kernel层对SElinux做控制时，可以使用以下参数：
		selinux=0|1，如果设置为0时，开机后getenforce获取的状态为disabled
		enforcing=0|1，如果设置为0时，开机后getenforce获取的状态为permissive

		每个文件和进程都有上下文，查看的指令为：
		ls -lZ 文件或目录（-d）
		ps auxZ | less
		SElinux的用户类型分为三种：超级用户，系统用户，普通用户
		文件或目录的SElinux权限控制主要设置的是第三列字段，type类型

		修改文件标签的方法：
		chcon -R -t public_content_t /srv/www
			chcon表示运行状态下的修改，修改完立即生效，restorecon可以将之前的修改还原
			在修复模式等特殊环境下，chcon做的修改会被重置还原
		semanage fcontext -a -t httpd_sys_content_t '/srv/www(/.*)?'
			semanage表示系统层的修改，修改完不会立即生效，需要通过重启或restorecon触发更新，更改之后的标签类型，restorecon无法还原，只能通过semanage设置新的标签类型
			restorecon -Rv /srv/www
			表示还原或触发系统默认标签类型
			-R表示递归式还原，-v表示显示还原标签的变化信息

	布尔值：
		主要是通过应用规则，保护服务器的文件目录不被破坏
		获取布尔值的方法：
			getsebool -a
			可以通过grep过滤需要设置的服务关键词，对布尔值作修改
		修改布尔值的方法：
			setsebool [-P] httpd_enable_cgi off/on
			-P表示规则永久生效，不加-P时，规则在不重启的情况下生效
		端口SElinux标签查看方法：
			semanage port -l

	SElinux日志机制：
		如果SElinux的监听服务开启，setroubleshootd（RHEL5/6）/auditd（RHEL7）
		SElinux相关的日志存放在/var/log/audit/audit.log文件中
		如果SElinux的监听服务没有开启，则日志机制会被rsyslog代理监听
		SElinux相关的日志会被存放在/var/log/messages文件中

 	使用ftp协议配置的端口是21；而Xshell登录默认用的是22端口，ssh协议，也就是sftp

 	netfilter
	位于Linux内核中的包过滤功能体系，基于内核控制，实现防火墙的相关策略
	iptables
	位于/sbin/iptables，用来管理防火墙规则的工具
	 
	iptables默认包括5种规则链
	INPUT：处理入站数据包
	OUTPUT：处理出站数据包
	FORWARD：处理转发数据包
	POSTROUTING链：在进行路由选择后处理数据包
	PREROUTING链：在进行路由选择前处理数据包
	 
	iptables默认包括4个规则表
	raw表：确定是否对该数据包进行状态跟踪  （kernel 2.6）
	mangle表：为数据包设置标记
	nat表：修改数据包中的源、目标IP地址或端口（网络地址转换）
	filter表：确定是否放行该数据包（过滤）
	 
	表与链的关联：
	raw：prerouting链   output链
	mangle：prerouting链  input链   forward链   output链    postrouting链
	nat：prerouting链  output链   postrouting链
	filter：input链   forward链   output链
	 
	语法构成
	iptables  [-t 表名]  选项  [链名]  [条件]  [-j 控制类型]
	[root@localhost ~]# iptables -t filter -I INPUT -p icmp -j REJECT
	几个注意事项
	不指定表名时，默认指filter表
	不指定链名时，默认指表内的所有链
	除非设置链的默认策略，否则必须指定匹配条件
	选项、链名、控制类型使用大写字母，其余均为小写
	 
	数据包的常见控制类型
	ACCEPT：允许通过
	DROP：直接丢弃，不给出任何回应
	REJECT：拒绝通过，必要时会给出提示
	LOG：记录日志信息，然后传给下一条规则继续匹配
	 
	启用iptables的方法
	首先需要安装iptables的服务包
	yum install iptables-services
	因为RHEL7默认使用防火墙工具为firewalld，所以需要关闭firewalld才能开启iptables
	systemctl stop firewalld.service
	systemctl disable firewalld.service
	关闭firewalld后打开iptables
	systemctl start iptables.service
	systemctl enable iptables.service
	systemctl start ip6tables.service
	systemctl enable ip6tables.service
	查看iptables状态
	systemctl status iptables.service
	确认firewalld关闭
	systemctl status firewalld.service
	 
	iptables规则管理
	添加新的规则
	-A：在链的末尾追加一条规则
	-I：在链的开头（或指定序号）插入一条规则
	查看规则列表
	-L：列出所有的规则条目
	-n：以数字形式显示地址、端口等信息
	-v：以更详细的方式显示规则信息
	--line-numbers：查看规则时，显示规则的序号
	删除、清空规则
	-D：删除链内指定序号（或内容）的一条规则
	-F：清空所有的规则
	-X：清空缓存信息
	 
	 
	iptables管理
	-P：为指定的链设置默认规则（ACCEPT／DROP）
	 
	查看网卡已存在的链接
	nmcli connection show
	删除跟配置不相关的链接文件
	nmcli connection delete simple
	删除链接创建是的本地配置文件
	cd /etc/sysconfig/network-scripts/
	rm -rf ifcfg-simple
	重启网卡，重新加载网卡配置
	systemctl restart network
	增加新的链接
	nmcli connection add con-name simple ifname eth0 type ethernet ip4 10.0.0.1/24 gw4 10.0.0.254
	因为网卡配置只是指向254的IP，但是地址并不存在，所以需要设置网关地址
	nmcli connection modify simple +ipv4.addresses 10.0.0.254
	 
	iptables设置规则增加或删除时，测试会生效
	永久配置生效的方法需要通过
	service iptables save
	将防火墙的规则保存到配置文件 /etc/sysconfig/iptables（重启或开机默认加载的防火墙规则文件）
	加载防火墙配置文件默认规则的方法：
	systemctl restart iptables.service
	 
	虚拟机的克隆：
	带链接的克隆：占用空间比较小，但是开启的时需保证被克隆的主机是运行状态
	完整克隆：跟被克隆虚拟机完全一致，需要开机后修改MAC地址，IP地址
	 
	firewalld
	动态链接防火墙，所做的配置可以实时生效，firewalld有两种配置状态：运行时和永久配置
	当规则被增加时，默认添加的位置为运行状态
	firewall-cmd --add-service=mysql
	查看当前运行状态下，firewalld开启的服务
	firewall-cmd --list-services 
	如果想要一个规则永久生效，需要增加选项“--permanent”
	firewall-cmd --permanent --add-service=mysql
	查看配置文件中，firewalld开启的服务
	firewall-cmd --list-services --permanent
	获取当前主机中firewalld的激活区域
	firewall-cmd --get-active-zones
	firewalld默认的激活区域为public，所以在配置防火墙规则时，如果不做“--zone=”区域的制定，默认的防火墙规则都会被写入到public区域中
	 
	根据网络地址，协议，端口同时对firewalld设置，可以使用富规则
	通过指定协议增加防火墙的限制
	firewall-cmd --add-rich-rule='rule family=ipv4 source address=172.25.0.11/24 service name=ssh accept'
	通过指定端口增加防火墙的限制
	     firewall-cmd --add-rich-rule='rule family=ipv4 source address=172.25.0.11/24 port protocol=tcp port=22 accept'
	 
	备份和还原（iptables）
	导出（备份）规则
	iptables-save工具
	[root@localhost ~]# iptables-save > /opt/iprules_all.txt（“>”表示输出重定向，将指令的输出结果保存到指定文件）
	导入（还原）规则
	iptables-restore工具
	[root@localhost ~]# iptables-restore < /opt/iprules_all.txt（“<”表示输入重定向，将文件信息通过指令还原到配置文件）
	 
	端口转发：
	firewall-cmd --permanent --add-rich-rule='rule family=ipv4 source address=172.25.X.10/32 forward-port port=443 protocol=tcp to-port=22'
	forward-port表示待转发的端口，protocol表示协议，to-port表示要转发的指定端口
	测试时，需要指定端口，ssh调用的选项为“-p”
	ssh -p 443 主机名
	 
	防火墙规则设置时，如果没有加--permanent，表示当前生效，重启主机或重启firewalld，规则失效（firewall-cmd --reload）
	防火墙规则设置时，如果增加了--permanent，规则不会立即生效，可以通过firewall-cmd --reload，重新加载配置文件，使设置的规则生效
	 
	实验：
	server：
	firewall-cmd --permanent --add-rich-rule='rule family=ipv4 source address=10.0.0.2/24 forward-port port=443 protocol=tcp to-port=22'
	client：
	ssh -p 443 主机名（连接失败）
	server：
	firewall-cmd --reload
	client：
	ssh -p 443 主机名（可以输入服务器密码，连接成功）