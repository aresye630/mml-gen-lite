# 查询订阅组（LST SUBSCRIBERGRP）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询订阅组配置。

## 注意事项

无。

## 参数说明

| 参数标识       | 参数名称   | 参数说明                                                       |
|:-----------|:-------|:-----------------------------------------------------------|
| SUBERGRPID | 订阅组ID  | 用于指示系统按照哪个订阅组ID查询订阅组信息；若不输入，则表示所有的订阅组ID。 取值范围：1～255。 默认值：无 |
| SUBERID    | 订阅者ID  | 用于指示系统按照哪个订阅者ID查询订阅组信息；若不输入，则表示所有的订阅者ID。 取值范围：1～255。 默认值：无 |

## 使用实例

1. 查询订阅组中订阅者信息，指定“订阅组ID”为“1”，“订阅者ID”为“1”。

   ```
   LST SUBSCRIBERGRP: SUBERGRPID=1, SUBERID=1;
   ```

   ```
   %%LST SUBSCRIBERGRP: SUBERGRPID=1, SUBERID=1;%%
   RETCODE = 0  操作成功

   操作结果如下
   ------------
     订阅组ID  =  1
     订阅者ID  =  1
     发送模式  =  广播
       优先级  =  NULL
   订阅组描述  =  NULL
   (结果个数 = 1)

   ---    END
   ```
2. 查询订阅组中所有的订阅者信息，指定“订阅组ID”为“1”。

   ```
   LST SUBSCRIBERGRP: SUBERGRPID=1;
   ```

   ```
   %%LST SUBSCRIBERGRP: SUBERGRPID=1;%%
   RETCODE = 0  操作成功

   操作结果如下
   ------------
    订阅组ID  订阅者ID  发送模式  优先级  订阅组描述

    1         1         广播      NULL    NULL      
    1         2         广播      NULL    NULL      
   (结果个数 = 2)

   ---    END
   ```
3. 查询所有的订阅者信息。

   ```
   LST SUBSCRIBERGRP:;
   ```

   ```
   %%LST SUBSCRIBERGRP:;%%
   RETCODE = 0  操作成功

   操作结果如下
   ------------
    订阅组ID  订阅者ID  发送模式  优先级  订阅组描述

    1         1         广播      NULL    NULL      
    1         2         广播      NULL    NULL      
    2         3         广播      NULL    NULL      
    2         4         广播      NULL    NULL      
   (结果个数 = 4)

   ---    END
   ```

## 输出结果说明

请参见**ADD SUBSCRIBERGRP**命令的参数说明。