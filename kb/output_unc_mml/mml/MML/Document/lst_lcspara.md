# 查询LCS参数表记录(LST LCSPARA)

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用网元：SGSN、MME**

此命令用于查询LCS参数。

#### 注意事项

此命令执行后立即生效。

#### 本地用户权限

manage-ug；system-ug；monitor-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

无。

#### 使用实例

查询LCS参数设置：

LST LCSPARA:;

```
%%LST LCSPARA:;%%
RETCODE = 0  操作成功。

操作结果如下
--------------
          隐私验证定时器(s)  =  20
    EPC 等待Paging定时器(s)  =  50
      EPC 位置获取定时器(s)  =  20
     EPC Multi IMSI定位方式  =  拒绝
EPC 位置信息表老化时长(min)  =  60
       GU 位置报告定时器(s)  =  30
       GU GMLC响应定时器(s)  =  20
     GU MO继续流程定时器(s)  =  10
   GU GMLC是否限定属于HPLMN  =  不限定属于HPLMN
   EPC UE级的GMLC的鉴权方案  =  仅鉴权同UE相同PLMN的GMLC
             2G LCS定位策略  =  本地定位
             4G LCS定位策略  =  协议模式定位
          启用连接态LRC流程  =  否
       ECM-IDLE态触发Paging  =  是
      延迟定位超时时长(min)  =  720
(结果个数 = 1)

---    END
```

#### 输出结果说明

参见**SET LCSPARA**的参数说明。