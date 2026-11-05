# 查询应用规则数量（DSP APPRULENUM）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：UPF、MPF**

该命令用于描述查询应用规则数量。

#### 注意事项

该命令执行后立即生效。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

无。

#### 使用实例

- 在UPF网元查询应用规则数量：

  ```
  DSP APPRULENUM:;
  ```

  ```
  RETCODE = 0  操作成功

  应用规则数量
  -----------------------
  Result  =  
         Application Name Number(Used/Max) = 0/1000
                 DNS Rule Number(Used/Max) = 0/10000
        DNS Redirect Rule Number(Used/Max) = 0/1000
             Traffic Rule Number(Used/Max) = 0/2000
           Bandwidth Rule Number(Used/Max) = 0/1000

  (结果个数 = 1)

  ---    END
  ```
- 在MPF网元查询应用规则数量：

  ```
  DSP APPRULENUM:;
  ```

  ```
  RETCODE = 0  操作成功

  应用规则数量
  -----------------------
  Result  =  
     Application Instance Number(Used/Max) = 0/1000
             Application Name Number(Used) = 0
                 DNS Rule Number(Used/Max) = 0/10000
             Traffic Rule Number(Used/Max) = 0/2000
           Bandwidth Rule Number(Used/Max) = 0/1000

  (结果个数 = 1)

  ---    END
  ```

#### 输出结果说明

| 输出项名称                       | 输出项解释                           |
|:----------------------------|:--------------------------------|
| Application Instance Number | App Instance资源(仅在MPF网元显示)。      |
| Application Name Number     | App Name资源。                     |
| DNS Rule Number             | DNS Rule资源。                     |
| DNS Redirect Rule Number    | DNS Redirect Rule资源(仅在UPF网元显示)。 |
| Traffic Rule Number         | Traffic Rule资源。                 |
| Bandwidth Rule Number       | BW Allocation Rule资源。           |