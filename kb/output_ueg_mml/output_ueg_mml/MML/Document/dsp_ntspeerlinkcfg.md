# 显示通知服务对端链路状态信息(DSP NTSPEERLINKCFG)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于在配置数据库中查询通知服务对端的链路状态信息。只能用于查询NTS作为客户端时的静态链路状态信息。

- 如果需要显示所有通知服务对端的链路状态信息，请不要输入任何参数。
- 如果需要显示指定通知服务对端的链路状态信息，请依据参数说明输入查询条件。

## 注意事项

无。

## 参数说明

| 参数标识   | 参数名称    | 参数说明                                                                                                                                               |
|:-------|:--------|:---------------------------------------------------------------------------------------------------------------------------------------------------|
| LINKID | 链路ID    | 可选必选说明：可选参数 参数含义：用于指示系统需要按照哪个链路ID来显示通知服务对端链路状态信息；若不输入，则表示所有的链路ID。 取值范围：1～255 默认值：无。 配置原则：无。                                                        |
| PEERID | 对端服务器ID | 可选必选说明：可选参数 参数含义：用于指示系统需要按照哪个对端服务器ID来显示通知服务对端链路状态信息；若不输入，则表示所有的对端服务器ID。用于标识通知任务服务对端服务器。该参数必须先由ADD NTSPEER命令定义，然后才能在此处使用。 取值范围：1～255 默认值：无。 配置原则：无。 |

## 使用实例

1. 显示所有的通知服务对端链路的状态信息。

   ```
   DSP NTSPEERLINKCFG:;
   ```

   ```
   %%DSP NTSPEERLINKCFG:;%%
   RETCODE = 0  操作成功

   操作结果如下
   ------------
   对端服务器ID    链路ID   POD名称                          链路状态   

   1               1        pcf-addn-pod217-5cb799b7f-gjc5f  离线    
   2               2        pcf-addn-pod217-5cb799b7f-gjc5f  在线      
   1               60039    pcf-addn-pod217-5cb799b7f-gjc5f  离线    
   1               60038    pcf-addn-pod217-5cb799b7f-gjc5f  离线    
   1               60049    pcf-addn-pod217-5cb799b7f-gjc5f  离线    
   1               60037    pcf-addn-pod217-5cb799b7f-gjc5f  离线    
   1               60048    pcf-addn-pod217-5cb799b7f-gjc5f  离线    
   1               60036    pcf-addn-pod217-5cb799b7f-gjc5f  离线    
   1               60047    pcf-addn-pod217-5cb799b7f-gjc5f  离线    
   1               60035    pcf-addn-pod217-5cb799b7f-gjc5f  离线    
   1               60046    pcf-addn-pod217-5cb799b7f-gjc5f  离线    
   1               60034    pcf-addn-pod217-5cb799b7f-gjc5f  离线    
   1               60045    pcf-addn-pod217-5cb799b7f-gjc5f  离线    
   1               60033    pcf-addn-pod217-5cb799b7f-gjc5f  离线    
   1               60044    pcf-addn-pod217-5cb799b7f-gjc5f  离线    
   1               60032    pcf-addn-pod217-5cb799b7f-gjc5f  离线    
   1               60043    pcf-addn-pod217-5cb799b7f-gjc5f  离线    
   1               60042    pcf-addn-pod217-5cb799b7f-gjc5f  离线    
   1               60041    pcf-addn-pod217-5cb799b7f-gjc5f  离线    
   1               60040    pcf-addn-pod217-5cb799b7f-gjc5f  离线    
   1               60050    pcf-addn-pod217-5cb799b7f-gjc5f  离线    
   1               1        pcf-addn-pod217-5cb799b7f-fxlst  离线    
   2               2        pcf-addn-pod217-5cb799b7f-fxlst  在线      
   1               60039    pcf-addn-pod217-5cb799b7f-fxlst  离线    
   1               60038    pcf-addn-pod217-5cb799b7f-fxlst  离线    
   1               60049    pcf-addn-pod217-5cb799b7f-fxlst  离线    
   1               60037    pcf-addn-pod217-5cb799b7f-fxlst  离线    
   1               60048    pcf-addn-pod217-5cb799b7f-fxlst  离线    
   1               60036    pcf-addn-pod217-5cb799b7f-fxlst  离线    
   1               60047    pcf-addn-pod217-5cb799b7f-fxlst  离线    
   1               60035    pcf-addn-pod217-5cb799b7f-fxlst  离线    
   1               60046    pcf-addn-pod217-5cb799b7f-fxlst  离线    
   1               60034    pcf-addn-pod217-5cb799b7f-fxlst  离线    
   1               60045    pcf-addn-pod217-5cb799b7f-fxlst  离线    
   1               60033    pcf-addn-pod217-5cb799b7f-fxlst  离线    
   1               60044    pcf-addn-pod217-5cb799b7f-fxlst  离线    
   1               60032    pcf-addn-pod217-5cb799b7f-fxlst  离线    
   1               60043    pcf-addn-pod217-5cb799b7f-fxlst  离线    
   1               60042    pcf-addn-pod217-5cb799b7f-fxlst  离线    
   1               60041    pcf-addn-pod217-5cb799b7f-fxlst  离线    
   1               60040    pcf-addn-pod217-5cb799b7f-fxlst  离线    
   1               60050    pcf-addn-pod217-5cb799b7f-fxlst  离线    
   (结果个数 = 42)

   ---    END
   ```
2. 显示一条通知服务对端链路的状态信息，“链路ID”为“1”。

   ```
   DSP NTSPEERLINKCFG: LINKID=1;
   ```

   ```
   %%DSP NTSPEERLINKCFG: LINKID=1;%%
   RETCODE = 0  操作成功

   操作结果如下
   ------------
   对端服务器ID    链路ID   POD名称                          链路状态  

   1               1        pcf-addn-pod217-5cb799b7f-gjc5f  离线    
   1               1        pcf-addn-pod217-5cb799b7f-fxlst  离线    
   (结果个数 = 2)

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见表1。

| 输出项名称   | 输出项解释                                                                                  |
|:--------|:---------------------------------------------------------------------------------------|
| 对端服务器ID | 用于显示CMPP、SMPP、SMTP和SOAP通知链路状态信息的对端ID。                                                  |
| 链路ID    | 用于显示CMPP、SMPP、SMTP和SOAP通知链路状态信息的链路ID。                                                  |
| POD名称   | 表示NTS服务所在的POD名称。                                                                       |
| 链路状态    | 用于显示CMPP、SMPP、SMTP和SOAP通知的链路状态。 UP(在线)：表示链路是连通的，可以进行信息交互。 DOWN(离线)：表示链路是不连通的，无法进行信息交互。 |