# 查询特殊MNC配置(LST SPECMNC)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询特殊MNC配置。

## 注意事项

无。

## 参数说明

无。

## 使用实例

1. 查询特殊MNC配置描述。

   ```
   LST SPECMNC:;
   ```

   ```
   %%LST SPECMNC;%% 
   RETCODE = 0 SUCCESS0001:Operation is successful 
    
                MCC        MNC      DESC
                344        030      AntiguaandBarbudaimobileAPUA
                722        031      ArgentinaClaro
                722        070      huaweitest2
   Total count = 3
   There is together 1 report
   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见**ADD SPECMNC**命令的参数说明。