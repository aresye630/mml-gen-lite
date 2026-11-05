# 查询Voice Centric终端接入接口地址（LST VCFUNCIP）

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用网元：MME、AMF**

查询Voice Centric终端接入接口地址。

#### 注意事项

无。

#### 本地用户权限

manage-ug；system-ug；monitor-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

无。

#### 使用实例

- 查询一条Voice Centric终端接入接口地址：

  ```
  %%LST VCFUNCIP:;%%
  RETCODE = 0  操作成功

  输出结果如下
  ------------------------
    IP Version  =  IPv4
  IPv4 address  =  192.168.53.52
  IPv6 address  =  ::
      VPN Name  =  NULL
  (结果个数 = 1)

  ---    END
  ```

- 查询多条Voice Centric终端接入接口地址：

  ```
  %%LST VCFUNCIP:;%% 
  RETCODE = 0  操作成功  
  输出结果如下 
  ------------------------ 
  IP Version  IPv4 address   IPv6 address                          VPN Name    
  IPv4        192.168.53.52  ::                                    NULL       
  IPv6        0.0.0.0        fc00::1                               NULL       
  (结果个数 = 2)  
  ---    END
  ```

#### 输出结果说明

请参考**ADD VCFUNCIP**的参数标识。