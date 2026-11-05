# 查询语音错误码映射（LST VOICETORXRCMAP）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令为维护类命令，用于查询N7/Gx接口的语音错误码映射记录。

## 注意事项

无。

## 参数说明

| 参数标识   | 参数名称       | 参数说明                                                                                                                     |
|:-------|:-----------|:-------------------------------------------------------------------------------------------------------------------------|
| N7RC   | N7/Gx接口结果码 | 可选必选说明：可选参数 参数含义：用于指定要进行转换的N7或Gx接口消息结果码。 取值范围： RC0(UpdateNotifyRspTimeOut-AARI)RC1(RAATimeOut-AARI) 默认值：无。 配置原则：无。       |
| RXRC   | Rx接口结果码    | 可选必选说明：可选参数 参数含义：用于指定N7或Gx接口消息结果码转换 Rx接口消息原因值。 取值范围： 5065(DIAMETER_REQUESTED_IPCAN_SESSION_NOT_AVAILABLE) 默认值：无。 配置原则：无。 |

## 使用实例

1. 查询所有的语音错误码映射。

   ```
   LST VOICETORXRCMAP:;
   ```

   ```
   %%LST VOICETORXRCMAP:;%% 
   RETCODE = 0  操作成功    

   操作结果如下 
   ------------ 
   N7/Gx接口结果码              Rx接口结果码                                    

   RAATimeOut-AARI              DIAMETER_REQUESTED_IPCAN_SESSION_NOT_AVAILABLE   
   UpdateNotifyRspTimeOut-AARI  DIAMETER_REQUESTED_IPCAN_SESSION_NOT_AVAILABLE   
   (结果个数 = 2)  

   ---    END
   ```
2. 查询一条语音错误码映射。“N7/Gx接口结果码”为“RC0”，“Rx接口结果码”为“5065”。

   ```
   %%LST VOICETORXRCMAP: N7RC=RC0, RXRC=5065;%% 
   RETCODE = 0  操作成功 

   操作结果如下 
   ------------
   N7/Gx接口结果码  =  UpdateNotifyRspTimeOut-AARI      
      Rx接口结果码  =  DIAMETER_REQUESTED_IPCAN_SESSION_NOT_AVAILABLE 
   (结果个数 = 1)  

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见ADD LDAPDEVADDR命令的参数说明。