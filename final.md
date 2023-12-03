# 一、计算机之间的连接方式
## 1.计算机之间的连接方式

- 网线直连
   - 需要用交叉线（不是直通线）
## 2.多台计算机的互联（旧式）

- 同轴电缆
   - 连接模型，左右扩散

![image.png](https://picbed1.lzaiz24.top/img/network/note2/image-0.png)

   - 连接特点：
      - 半双工通信、容易冲突
      - 不安全、一旦某段线路出现问题，整个通信网络都会瘫痪
## 3.多台计算机的互联 --- 集线器（Hub）
集线器有多个接口，接口的类型是RJ-45。一个接口收到数据后会发给其它的全部接口。集线器工作在物理层，类似于一个多接口的转发器，收到什么就转发什么，一个接口收到会转发给其它的全部接口。
![image.png](https://picbed1.lzaiz24.top/img/network/note2/image-1.png)

- 连接模型

![image.png](https://picbed1.lzaiz24.top/img/network/note2/image-2.png)
![image.png](https://picbed1.lzaiz24.top/img/network/note2/image-3.png)

- 通信流程（单一集线器）

![image.png](https://picbed1.lzaiz24.top/img/network/note2/image-4.png)

-  通信流程（多集线器） 

 ![image.png](https://picbed1.lzaiz24.top/img/network/note2/image-5.png)

- 连接特点
   - 半双工通信、容易发生冲突
   - 不安全，跟同轴电缆一样，没有记录存储能力，但某两个节点出现问题，不影响其他节点
- 缺点
   - 如果有1000台设备用多集线器连接，那么1台主机发送的数据，虽然最后只有一个主机来处理这个数据包，但会被发送到999台主机，对整个网络链路的占有率会非常高。

信源	信道	信宿
```html
设备									设备
发送端- - - T		- - - R	接收端（消息队列）管道
信号A端- - - T		- - - T信号B端
- - - - - -> - - - -（信道发送）
- - - - - -< - - - -（信道接收）
- - - R               - - - R
```
通信模型：

- `单工`	发送端和接收端 设备只具备一种能力	BP机
- `全双工`	发送端和接收端 设备都具备两种能力	信道有两根 同时可以满足收 发（电话）
- `半双工`	发送端和接收端 设备都具备两种能力，信道只有一根	同时只能满足一个通信过程（对讲机）

Q:
是不是只要mac地址改变了 就比如说 新的设备加入 就要ARP一次？
GPT-A:
`是的，当新设备加入网络时，通常会触发地址解析协议（ARP）请求。ARP用于将IP地址映射到物理硬件地址（例如MAC地址）。当一个设备需要与网络中的另一个设备通信时，它首先会检查目标设备的IP地址是否已经被映射到相应的MAC地址。如果尚未映射，设备将发送ARP请求，请求目标设备的MAC地址。当设备的MAC地址发生变化时（例如，新设备加入网络），其他设备可能需要更新其ARP缓存，以确保正确地将目标IP地址映射到新的MAC地址。ARP缓存是一个存储最近ARP请求响应的表格，用于加速将IP地址解析为MAC地址的过程。所以，确实可以说，当新设备加入网络并且具有新的MAC地址时，可能会触发ARP请求，以便其他设备能够获取新设备的MAC地址并更新其ARP缓存。`

## 4. 多台计算机的互联 --- 网桥（Bridge）  
网桥又叫做桥接器，工作在数据链路层,是一个二层设备。网桥能够互联两个采用不同传输介质与不同传输速率的网络，但是网桥需要互联网的网络在数据链路层以上采用相同的协议。网桥可以分隔两个网络之间的通信量，对收到的帧，根据其MAC帧的目的地址进行转发和过滤。  当网桥收到了一个帧时，并不是向所有的接口转发此帧，而是根据此帧的目的MAC地址，查找网桥中的地址表，然后确定将该帧转发到哪一个接口，或者是把它丢弃（即过滤）
![image.png](https://picbed1.lzaiz24.top/img/network/note2/image-6.png)
![image.png](https://picbed1.lzaiz24.top/img/network/note2/image-7.png)

- 通信流程

![image.png](https://picbed1.lzaiz24.top/img/network/note2/image-8.png)

- 特点
   - 网桥可以通过自学习得知每侧接口的MAC地址，从而起到隔绝冲突域的作用
## 5.多台计算机的互联 --- 交换机（Switch）
![image.png](https://picbed1.lzaiz24.top/img/network/note2/image-9.png)
相当于集线器+网桥，接口更多的网桥，全双工通信，比集线器安全。

- 通信流程

![image.png](https://picbed1.lzaiz24.top/img/network/note2/image-10.png)
##  6. 多台计算机的互联 --- 路由器（Router）
 ![image.png](https://picbed1.lzaiz24.top/img/network/note2/image-11.png)

- 之前的多台计算机互联，连接的设备必须在同一网段，处在同一广播域。
- 路由器的特点
   - 可以在不同网段之前转发数据
   - 隔绝广播域
> 主机发送数据之前，⾸先会判断⽬标主机的IP地址跟它是否在同一个网段： 
> -  同一个网段：ARP⼴播，查找MAC，通过交换机、集线器传递数据 
> - 不在同一个网段：通过路由器转发数据，主机向网关发送数据 


# 二、MAC地址
## MAC地址的格式特征

- 每一个网卡都有一个6字节（48bit）的MAC地址（Media Access Control Address），MAC 地址的结构如下：

![image.png](https://picbed1.lzaiz24.top/img/network/note2/image-12.png)

- 全球唯一，固化在网卡的ROM中，由IEEE802标准规定
前3字节：OUI，组织唯一标识符，由IEEE的注册管理机构分配给⼚商
   - 后3字节：网络接口标识符，由⼚商⾃⾏分配
- OUI查询
   - [https://standards-oui.ieee.org/oui/oui.txt](https://standards-oui.ieee.org/oui/oui.txt)
   - [https://mac.bmcx.com/](https://mac.bmcx.com/)
- MAC地址的表示格式
   - Windows：					40-55-82-0A-8C-6D
   - Linux、Android、Mac、iOS：	40:55:82:0A:8C:6D
   - Packet Tracer：				4055.820A.8C6D
   - 当48位全为1时，代表⼴播地址：	FF-FF-FF-FF-FF-FF
## MAC地址的获取

- 当不知道对⽅主机的MAC地址时，可以通过发送ARP⼴播获取对⽅的MAC地址
   - 获取成功后，会缓存IP地址、MAC地址的映射信息，俗称：ARP缓存
   - 通过ARP⼴播获取的MAC地址，属于动态（dynamic）缓
      - 存储时间⽐较短（默认是2分钟），过期就⾃动删除
- 相关命令
   - arp -a [主机地址]：	查询ARP缓存
   - arp -d [主机地址]：	删除ARP缓存
   - arp -s 主机地址 MAC地址：增加一条缓存信息（这是静态缓存，存储时间较久）
## ARP是什么
ARP 协议的全称是 Address Resolution Protocol(地址解析协议)，它是一个通过用于实现从 IP 地址到 MAC 地址的映射，即询问⽬标 IP 对应的 MAC 地址 的一种协议。ARP 协议在 IPv4 中极其重要。
	下⾯我们探讨一下 ARP 的⼯作机制是怎样的。假设 A 和 B 位于同一链路，不需要经过路由器的转换，主机 A 向主机 B 发送一个 IP 分组，主机 A 的地址是 192.168.1.2 ，主机 B 的地址是 192.168.1.3，它们都不知道对⽅的 MAC 地址是啥，主机 C 和 主机 D 是同一链路的其他主机。
![image.png](https://picbed1.lzaiz24.top/img/network/note2/image-13.png)
主机 A 想要获取主机 B 的 MAC 地址，通过主机 A 会通过⼴播 的⽅式向以太网上的所有主机发送一个 ARP 请求包，这个 ARP 请求包中包含了主机 A 想要知道的主机 B 的 IP 地址的 MAC 地址。
![image.png](https://picbed1.lzaiz24.top/img/network/note2/image-14.png)
主机 A 发送的 ARP 请求包会被同一链路上的所有主机/路由器接收并进⾏解析。每个主机/路由器都会检查 ARP 请求包中的信息，如果 ARP 请求包中的⽬标 IP 地址 和⾃⼰的相同，就会将⾃⼰主机的 MAC 地址写⼊响应包返回主机 A。
![image.png](https://picbed1.lzaiz24.top/img/network/note2/image-15.png)
由此，可以通过 ARP 从 IP 地址获取 MAC 地址，实现同一链路内的通信。
## ARP缓存
通过 ARP 缓存，降低了网络流量的使用，在一定程度上防⽌了 ARP 的⼤量⼴播。
![image.png](https://picbed1.lzaiz24.top/img/network/note2/image-16.png)
一般来说，发送过一次 ARP 请求后，再次发送相同请求的⼏率⽐较⼤，因此使用 ARP 缓存能够减少 ARP 包的发送，除此之外，不仅仅 ARP 请求的发送⽅能够缓存 ARP 接收⽅的 MAC 地址，接收⽅也能够缓存 ARP 请求⽅的 IP 和 MAC 地址，如下所示：
![image.png](https://picbed1.lzaiz24.top/img/network/note2/image-17.png)
不过，MAC  地址的缓存有一定期限，超过这个期限后，缓存的内容会被清除。
	我们可以在 Linux 或者 Windows 中使用 arp 命令查看 ARP 缓存。选项 -a 用于显示两个系统缓存中所有的缓存项。
在 Linux 中使用 arp 查询缓存：
![image.png](https://picbed1.lzaiz24.top/img/network/note2/image-18.png)
主要包含五项

- 主机名 --- 对应一个 IP 地址
- 硬件地址类型
- 硬件地址
- 标志
- 本地网络接口

标志主要分为三类: C 、M 或 P，C 表示的是由 ARP 协议动态学习。M 类可以通过 arp -s 增加一条。P 类表示的是发布，对于任何 P 类项⽬，主机对输⼊的 ARP 请求都返回一个 ARP 响应。这个选项用于配置代理 ARP。
	⽐如我们在 Windows 中进⾏ ARP 缓存查询（arp -a 用于查询计算机中的 ARP 缓存表）
![image.png](https://picbed1.lzaiz24.top/img/network/note2/image-19.png)
Windows 中的 ARP 程序显示了 IPv4 的地址，它的接口是⼗六进制数，Windows 版本还指出地址是手动输⼊还是 ARP 动态学习的。在上⾯的例⼦中，既有静态的也有动态的。48 位的 MAC 地址被显示为 6 个⼗六进制数，在 Linux 中使用 : 号，在 Windows 中使用 - 进⾏分隔。
## RARP
与 ARP 相对的，RARP(Reverse Address Resolution Protocol) 是将 ARP 反过来，从 MAC 地址定位 IP 地址的一种协议，将打印机服务器等⼩型嵌⼊式设备接⼊网络时会使用到。
![image.png](https://picbed1.lzaiz24.top/img/network/note2/image-20.png)
⽬前被BOOTP、DHCP所取代。

# 三、IP地址
## IP地址定义
现如今有两个版本的 IP 地址，IPv4 和 IPv6，我们⾸先探讨一下现如今还在⼴泛使用的 IPv4 地址，后⾯再考虑 IPv6 。
	IPv4 由 32 位正整数来表示，在计算机内部会转化为⼆进制来处理，但是⼆进制不符合⼈类阅读的习惯，所以我们根据易读性的原则把 32 位的 IP 地址以 8 位为一组，分成四组，每组之间以 . 进⾏分割，再将每组转换为⼗进制数。如下图所示：
![image.png](https://picbed1.lzaiz24.top/img/network/note2/image-21.png)
那么上⾯这个 32 位的 IP 地址就会被转换为⼗进制的 156.197.1.1。
除此之外，从图中我们还可以得到如下信息
	每个这样 8 位位一组的数字，⾃然是⾮负数，其取值范围是 [0,255]。
	IP 地址的总个数有 2^32 次幂个，这个数值算下来是 4294967296 ，⼤概能允许 43 亿台设备连接到网络。实际上真的如此吗？
	实际上 IP 不会以主机的个数来配置的，⽽是根据设备上的 网卡(NIC) 进⾏配置，每一块网卡都会设置一个或者多个 IP 地址，⽽且通常一台路由器会有⾄少两块网卡，所以可以设置两个以上的 IP 地址，所以主机的数量远远达不到 43 亿。
![image.png](https://picbed1.lzaiz24.top/img/network/note2/image-22.png)
## IPv4地址的表示⽅法

- IPv4地址由因特网名字和数字分配机构（Internet Corporation for Assigned Names and Numbers，ICANN）进⾏分配。
   - 我国用户可向亚太网络信息中⼼（Asia Pacific Network Information Center，APNIC）申请IP地址，需要缴纳相应的费用，一般不接受个⼈申请。
   - 2011年2⽉3⽇，因特网号码分配管理局（Internet Assigned Numbers Authority，IANA）（由 ICANN⾏使职能）宣布，IPv4地址已经分配完毕。
   - 我国在2014⾄2015年也逐步停⽌了向新用户和应用分配IPv4地址，同时全⾯开展商用部署  IPv6。
- IPv4地址的编址⽅法经历了三个历史阶段：

![image.png](https://picbed1.lzaiz24.top/img/network/note2/image-23.png)
2.1.	IPv4地址的分类编址⽅法

- 网络层如何识别一个设备的信息，就像⼈一样，有身份证那样。

![image.png](https://picbed1.lzaiz24.top/img/network/note2/image-24.png)

- 早期为了分类管理，采用了下表的固定⽅式进⾏分类管理

![image.png](https://picbed1.lzaiz24.top/img/network/note2/image-25.png)
A类、B类和C类地址都是单播地址，只有单播地址可以分配给网络中的主机（或路由器）的各接口。
主机号为“全0”的地址是网络地址，不能分配给主机（或路由器）的各接口。
主机号为“全1”的地址是⼴播地址，不能分配给主机（或路由器）的各接口。
![image.png](https://picbed1.lzaiz24.top/img/network/note2/image-26.png)

- 一般不使用的特殊IPv4地址

![image.png](https://picbed1.lzaiz24.top/img/network/note2/image-27.png)

- 练习题
1. 以下IPv4地址，按照默认分类编址⽅法，是否可以分配给主机或路由器？b、e、g
a. 0.1.2.3	b. 1.2.3.4	c. 126.255.255.255	d. 127.0.0.1		e. 166.16.18.255	f.192.0.0.255	g.223.255.255.252
2. 下列IP地址中，只能作为IP分组的源IP地址但不能作为⽬的IP地址的是（A）。 

A、0.0.0.0	 B、127.0.0.1  C、20.10.10.3  D、255.255.255.255

### 2.2.IPv4地址的划分⼦网编址⽅法
#### 2.2.1.为什么需要划分⼦网那？
案例分析
- 如果需要让200台主机在同一个网段内，可以分配一个C类网段，⽐如192.168.1.0/24
   - 共254个可用IP地址：192.168.1.1~192.168.1.254
   - 多出54个空闲的IP地址，这种情况并不算浪费资源
- 如果需要让500台主机在同一个网段内，那就分配一个B类网段，⽐如191.100.0.0/16
   - 共65534个可用IP地址：191.100.0.1~191.100.255.254
   - 多出65034个空闲的IP地址，这种情况属于极⼤的浪费资源

随着更多的中⼩网络加⼊因特网，IPv4分类编址⽅法不够灵活、容易造成⼤量IPv4地址资源浪费的缺点就暴露出来了。分类编址⽅法不够灵活且容易造成⼤量地址浪费，划分⼦网编址⽅法对其进⾏改进
（ 打补丁 ）。

- ⼦网掩码可以表明分类IPv4地址的主机号部分被借用了⼏个⽐特作为⼦网号。
- 与IPv4地址类似，⼦网掩码也是由32⽐特构成的。
   - 用左起多个连续的⽐特1对应IPv4地址中的网络号和⼦网号
   - 之后的多个连续的⽐特0对应IPv4地址中的主机号。
- 只要给定了一个分类的IPv4地址及其相应的⼦网掩码，就可以得出⼦网划分的全部细节。
#### 2.2.2.怎么划分⼦网？
将IP地址中的主机号部分再拿出某⼏位来作为网络号，剩下的部分作为主机号。
下⾯看一个例⼦：
现有一个C类网210.55.23.X。由于有四个不同的部⻔要使用这段IP，为了不让各个部⻔之间相互⼲扰，我们需要如何处理？
解答过程根据题意，我们需要将原来给出的一个网络划分为四个⼦网，以使得各个⼦网间互不影响。那么这个网段能够为⾃⼰使用的就是最后一个X，他代表8个bit。为了划分4个网段，需要2
个bit来标记，所以我们将IP地址的主机部分中（8位）拿出前⾯2位来作为我们的⼦网网络号部
分，因此用作主机的位数就只有剩下的6位。
210.55.23.xxxx xxxx
![image.png](https://picbed1.lzaiz24.top/img/network/note2/image-28.png)
由于我们将原来IP地址中主机号的前两位用来作为了网络号部分，因此，为了让计算机能知道这两位是网络号，所以我们需要将相应的⼦网掩码中对应的这两位设置为1。
	所以⼦网掩码应设置为255.255.255.192。
#### 2.2.3.总结

- 在线⼯具：[https://tool.chinaz.com/tools/subnetmask](https://tool.chinaz.com/tools/subnetmask)
- 根据⼦网ID借用的主机位数，我们可以计算出划分的⼦网数、掩码、每个⼦网主机数，以C类网络为例：

![image.png](https://picbed1.lzaiz24.top/img/network/note2/image-29.png)
练习题
1. 某主机的IP地址为180.80.77.55，⼦网掩码255.255.252.0，若该主机向其所在⼦网发送⼴播分组，则⽬的地址可以是（D）。
A、180.80.76.0	B、180.80.76.255	C、180.80.77.255	D、180.80.79.255
### 2.3.	IPv4地址的⽆分类编址⽅法

- IPv4地址的划分⼦网编址⽅法在一定程度上缓解了因特网在发展中遇到的困难，但是数量巨⼤的C类网(**𝟐****24-3****=𝟐𝟎𝟗𝟕𝟏𝟓𝟐**)由于其每个网络所包含的地址数量太⼩(**𝟐****8****=𝟐𝟓𝟔**)，因此并没有得到充分使用，⽽因特网的IPv4地址仍在加速消耗，整个IPv4地址空间⾯临全部耗尽的威胁。
- 因特网⼯程任务组IETF⼜提出了采用⽆分类编址的⽅法，来解决IPv4地址资源紧张的问题，同时还专⻔成⽴IPv6⼯作组负责研究新版本的IP，以彻底解决IPv4地址耗尽问题。
- 1993年，因特网⼯程任务组IETF发布了⽆分类域间路由选择（Classless Inter-Domain Routing， CIDR ）的RFC⽂档[RFC1517~1519，RFC1520]。
   - CIDR消除了传统A类	B类和C类地址以及划分⼦网的概念。
   - CIDR可以更加有效地分配IPv4地址资源，并且可以在IPv6使用之前允许因特网的规模继续增⻓。

![image.png](https://picbed1.lzaiz24.top/img/network/note2/image-30.png)

- 为了简便起⻅，可以不明确给出配套的地址掩码的点分⼗进制形式，⽽是在⽆分类编址的IPv4地址后⾯加上斜线"/"，在斜线之后写上网络前缀所占的⽐特数量（也就是地址掩码中左起连续⽐特1的数量），这种记法称为斜线记法。

![image.png](https://picbed1.lzaiz24.top/img/network/note2/image-31.png)
## 3.构造超网
### 3.1需求分析

-  原本有200台计算机使用192.168.0.0/24网段，现在希望增加200台设备到同一个网段。  
   -  200台在192.168.0.0/24网段，200台在192.168.1.0/24网段  
   -  合并192.168.0.0/24、192.168.1.0/24为一个网段：192.168.0.0/23（⼦网掩码往左移动1位）  

![image.png](https://picbed1.lzaiz24.top/img/network/note2/image-32.png)

-  ⼦网掩码向左移动2位，可以合并4个网段  
### 3.2路由聚合
![image.png](https://picbed1.lzaiz24.top/img/network/note2/image-33.png)

- 网络前缀越⻓，地址块越⼩，路由越具体； 
- 若路由器查表转发分组时发现有多条路由条⽬匹配，则选择网络前缀最⻓的那条路由条⽬， 这称为最⻓前缀匹配，因为这样的路由更具体。  

![image.png](https://picbed1.lzaiz24.top/img/network/note2/image-34.png)
### 3.3如何判断是子网还是超网

-  先判断该网段的类型，是A类、B类、C类网络  
   -  默认A类⼦网掩码的位数是8，B类⼦网掩码的位数是16，C类⼦网掩码的位数是24  
-  然后判断⼦网掩码的位数  
   -  ⽐默认⼦网掩码多，就是⼦网  
   -  ⽐默认⼦网掩码少，就是超网  

## 4.路由概述
### 1.路由的作用
### 2.多个不同网段的互联互通
### 3.数据包的传送过程

-  问题1：从H1到H2的数据包，数据包在网络层和网络接口层的传输过程  

![image.png](https://picbed1.lzaiz24.top/img/network/note2/image-35.png)

-  在数据包的传送过程中，数据包的源IP地址和⽬的IP地址保持不变；  
-  在数据包的传送过程中，数据包的源MAC地址和⽬的MAC地址逐链路（或逐网络）改变。  

![image.png](https://picbed1.lzaiz24.top/img/network/note2/image-36.png)
### 4. 因特网的公网和私网  
#### 4.1 因特网的接⼊⽅式  
##### 1. 电话线⼊户  
![image.png](https://picbed1.lzaiz24.top/img/network/note2/image-37.png)

- 平时说的ADSL电话拨号上网，⾮对称数字用户线路，提供上、下⾏不对称的传输带宽。 
- 需要提供猫（Modem）,调制解调器，进⾏数字信号和模拟信号的转换。  
##### 2.光纤入户
![image.png](https://picbed1.lzaiz24.top/img/network/note2/image-38.png)

- 光猫（optical modem），光调制解调器，进⾏数字信号和光信号的转换  
####  4.2. 公网和私网  

- 公网（public） 
   - Internet上路由器中只有到达公网的路由表，没有到达私网的路由表 
   - 公网IP由因特网信息中⼼（Internet Network Information Center，Inter NIC）统一分配和管理 
   - ISP需要向Inter NIC申请公网IP 
- 私网（private） 
   - 主要用于局域网 
   - A类：10.0.0.0/8，1个A类网络 
   - B类：172.16.0.0/16 ~ 172.31.0.0/16，16个B类网络 
   - C类：192.168.0.0/24 ~ 192.168.255.0/24，256个C类网络  
####  4.3. NAT技术  

- 私网IP访问Internet需要进⾏NAT转换为公网IP 
   - NAT（Network Address Translation） 
   - 这一步可以由路由器来完成  
-  NAT特点  
   -  可以节约公网IP资源  
   -  会隐藏内部真实IP  
-  NAT分类  
   -  静态转换，手动配置NAT映射表  
   -  动态转换，定义外部地址池，动态随机转换，一对一转换  
   -  PAT（Port Address Translation），多对一转换  
      -  采用端口多路复用技术  









