## 策略资金管理方法
本方法包括两个逻辑部分,**求得止损,进而得到下单量**
其中的下单量的确定才是正统的***资金管理***用到的.  
放到一个大的框架上来说,一个有利的交易系统包括两个大的组成部分
1. 具有正期望的交易信号(注意我说的是交易信号)
2. ***资金管理***  

这里涉及到的点有**交易信号**,**正期望**,**止盈止损**,**下单量**,**资金管理策略**  
从先后顺序来说
先有交易信号后,要通过分析让该交易信号成为具有正期望的交易策略.  
再有根据分析获得止盈止损得到下单量,再配合例如固定百分比这样的资金管理策略.  
*所以说有个交易信号只是第一步,第二步是要让该信号成为有正期望的信号,
在正期望信号的基础上再配合上资金管理的策略*.  这才是全面的交易系统  
本程序是处于第二步.
---
#### 执行的命令是
`python3 main.py EOSUSDT_30m`

---
**本程序在本地执行,同步到服务器的redis中,不需要部署程序到服务器**
