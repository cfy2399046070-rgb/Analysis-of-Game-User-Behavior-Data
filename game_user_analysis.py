# ==========================================
# 游戏用户行为分析系统
# ==========================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# 1. 生成模拟数据
# ==========================================

np.random.seed(42)

n_users = 1000 #模拟1000个用户
n_days = 7 #模拟7天

data = []

for user in range(1, n_users + 1):

    active_days = np.random.randint(1, n_days + 1) #随机生成活跃天数

    active_day_list = np.random.choice(
        range(1, n_days + 1),
        active_days,
        replace=False
    )

    for day in active_day_list:

        login = 1   #标记登录为1

        pay = np.random.binomial(
            n=1,
            p=0.1
        )   #用二项分布模拟付费,10%概率付费

        data.append(
            [user, day, login, pay]
        )

df = pd.DataFrame(
    data,
    columns=[
        "user_id",
        "day",
        "login",
        "pay"
    ]
)

print("=" * 50)
print("数据预览")
print("=" * 50)
print(df.head())

# ==========================================
# 保存数据到CSV文件
# ==========================================

df.to_csv('user_behavior_data.csv', index=False)
print("\n数据已保存到 user_behavior_data.csv")

# ==========================================
# 2. DAU分析
# ==========================================

print("\n")
print("=" * 50)
print("DAU分析")
print("=" * 50)

dau = df.groupby("day")["user_id"].nunique()
print(dau)

# ==========================================
# 3. 付费率分析
# ==========================================

print("\n")
print("=" * 50)
print("付费率分析")
print("=" * 50)

overall_pay_rate = df["pay"].mean()

print(f"整体付费率: {overall_pay_rate:.2%}")
daily_pay_rate = (
    df.groupby("day")["pay"].mean()
)



print("\n每日付费率:")
print(
    daily_pay_rate.apply(
        lambda x: f"{x:.2%}"
    )
)

# ==========================================
# 4. 留存分析
# ==========================================

print("\n")
print("=" * 50)
print("留存分析")
print("=" * 50)

retention_result = {}

for day in range(1, n_days):

    current_users = set(
        df[df["day"] == day]["user_id"]
    )#取该日所有用户,set去重

    next_users = set(
        df[df["day"] == day + 1]["user_id"]
    )#取下一日所有用户,set去重

    if len(current_users) == 0:
        retention = 0
    else:
        retention = (
            len(current_users & next_users)
            / len(current_users)
        )#留存计算

    retention_result[
        f"{day}->{day+1}"
    ] = retention

for k, v in retention_result.items():
    print(
        f"{k} 留存率: {v:.2%}"
    )

# ==========================================
# 5. 用户活跃度分析
# ==========================================

print("\n")
print("=" * 50)
print("用户活跃度分析")
print("=" * 50)

user_activity = (
    df.groupby("user_id")["login"]
      .sum()
)

print(
    f"平均登录天数: {user_activity.mean():.2f}"
)

print(
    f"最高登录天数: {user_activity.max()}"
)

print(
    f"最低登录天数: {user_activity.min()}"
)

# ==========================================
# 6. 用户分层
# ==========================================

print("\n")
print("=" * 50)
print("用户分层")
print("=" * 50)

active_users = user_activity[
    user_activity >= 5
]

normal_users = user_activity[
    (user_activity >= 3)
    & (user_activity < 5)
]

churn_users = user_activity[
    user_activity <= 2
]

print(
    f"高活跃用户数量: {len(active_users)}"
)

print(
    f"普通用户数量: {len(normal_users)}"
)

print(
    f"低活跃用户数量: {len(churn_users)}"
)

# ==========================================
# 7. 付费用户分析
# ==========================================

print("\n")
print("=" * 50)
print("付费用户分析")
print("=" * 50)

pay_users = set(
    df[df["pay"] == 1]["user_id"]
)

non_pay_users = (
    set(df["user_id"])
    - pay_users
)

print(
    f"付费用户数量: {len(pay_users)}"
)

print(
    f"非付费用户数量: {len(non_pay_users)}"
)

# ==========================================
# 8. 活跃用户 VS 付费用户
# ==========================================

user_pay_count = (
    df.groupby("user_id")["pay"]
      .sum()
)#总付费次数

user_summary = pd.DataFrame({
    "login_days": user_activity,
    "pay_count": user_pay_count
})

user_summary["is_pay"] = (
    user_summary["pay_count"] > 0
)

result = (
    user_summary
    .groupby("is_pay")["login_days"]
    .mean()
)

print("\n付费用户平均登录天数")

print(result)

# ==========================================
# 9. DAU可视化
# ==========================================

plt.figure(figsize=(8, 5))

plt.plot(
    dau.index,
    dau.values,
    marker="o"
)

plt.title("DAU Trend")
plt.xlabel("Day")
plt.ylabel("Active Users")

plt.grid(True)

plt.show()

# ==========================================
# 10. 留存率可视化
# ==========================================

retention_values = list(
    retention_result.values()
)

retention_labels = list(
    retention_result.keys()
)

plt.figure(figsize=(8, 5))

plt.bar(
    retention_labels,
    retention_values
)

plt.title("Retention Rate")

plt.ylabel("Rate")

plt.show()

# ==========================================
# 11. 用户活跃度分布
# ==========================================

plt.figure(figsize=(8, 5))

plt.hist(
    user_activity,
    bins=7
)

plt.title(
    "User Activity Distribution"
)

plt.xlabel(
    "Login Days"
)

plt.ylabel(
    "User Count"
)

plt.show()

print("\n")
print("=" * 50)
print("分析完成")
print("=" * 50)