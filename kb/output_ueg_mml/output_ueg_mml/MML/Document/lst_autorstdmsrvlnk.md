# 查询自动重置Diameter服务端链路(LST AUTORSTDMSRVLNK)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明
- 参考信息

## 命令功能

该命令为维护类命令，用于查询当前自动重置Diameter服务端链路的相关配置信息。

## 注意事项

无。

## 参数说明

无。

## 使用实例

1. 查询当前自动重置Diameter服务端链路的配置信息。

   ```
   LST AUTORSTDMSRVLNK:;
   ```

   ```
   %%LST AUTORSTDMSRVLNK:;%%
   RETCODE = 0  操作成功
   操作结果如下
   ------------
                自动重置开关  =  Disable
            自动重置时间间隔  =  10
                    对端类型  =  NULL
   (结果个数 = 1)
   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见**SET AUTORSTDMSRVLNK**命令的参数说明。

## 参考信息

无。