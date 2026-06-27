# 游戏用户行为数据分析系统

## 项目简介

本项目是一个基于 Python 的游戏用户行为数据分析系统。通过模拟生成 1000 名用户在 7 天内的登录与付费数据，对用户的活跃度、付费行为、留存率等关键指标进行多维度分析，并以图表形式直观展示分析结果。

## 功能模块

### 1. 模拟数据生成
- 使用 NumPy 随机生成 1000 名用户在 7 天内的行为数据
- 每位用户的活跃天数为 1~7 天随机分布
- 每日付费行为以 10% 的概率通过二项分布模拟
- 生成的数据包含字段：`user_id`（用户ID）、`day`（天数）、`login`（登录标记）、`pay`（付费标记）

### 2. DAU（日活跃用户数）分析
- 按天统计去重后的活跃用户数量
- 绘制 DAU 趋势折线图，直观展示日活变化

### 3. 付费率分析
- 计算整体付费率
- 按天统计每日付费率
- 支持百分比格式输出

### 4. 留存分析
- 计算相邻两天的次日留存率（如 Day1→Day2、Day2→Day3 等）
- 留存率 = 相邻两天共同活跃用户数 / 前一天活跃用户数
- 以柱状图展示各日留存率变化

### 5. 用户活跃度分析
- 统计每位用户的总登录天数
- 输出平均、最高、最低登录天数
- 以直方图展示用户活跃度分布

### 6. 用户分层
- **高活跃用户**：登录天数 ≥ 5 天
- **普通用户**：登录天数 3~4 天
- **低活跃用户（流失风险）**：登录天数 ≤ 2 天
- 输出各层级用户数量

### 7. 付费用户分析
- 识别付费用户与非付费用户
- 对比付费用户与免费用户群体的平均登录天数差异

### 8. 数据可视化

运行脚本后将在当前目录生成三张 PNG 图片：

#### DAU 趋势图 (`dau_trend.png`)
- 折线图，横轴为 Day 1~7，纵轴为去重活跃用户数
- 每日 DAU 稳定在 560~600 人之间，整体波动较小

#### 留存率柱状图 (`retention_rate.png`)
- 柱状图，展示 6 组相邻日次日留存率（1→2、2→3、...、6→7）
- 留存率 = 相邻两天共同活跃用户数 / 前一天活跃用户数
- 各日留存率稳定在 65%~69% 区间

#### 用户活跃度分布直方图 (`user_activity_distribution.png`)
- 直方图，横轴为登录天数（1~7），纵轴为用户人数
- 展示 1000 名用户登录天数的整体分布情况，7 天全勤用户占比最高

## 技术栈

| 技术        | 用途           |
| ----------- | -------------- |
| Python 3.x  | 编程语言       |
| Pandas      | 数据处理与分析 |
| NumPy       | 数值计算与模拟 |
| Matplotlib  | 数据可视化     |

## 快速开始

### 环境要求

- Python 3.7+
- pip

### 安装依赖

```bash
pip install pandas numpy matplotlib
```

### 运行

```bash
python game_user_analysis.py
```

### 输出说明

运行脚本后将依次在终端输出以下分析结果：

1. 数据预览（前 5 行）
2. DAU 统计
3. 整体与每日付费率
4. 逐日留存率
5. 用户活跃度统计
6. 用户分层数量
7. 付费用户统计及与活跃度的关联分析

同时将在当前目录生成三张 PNG 图表文件（`dau_trend.png`、`retention_rate.png`、`user_activity_distribution.png`）以及 `user_behavior_data.csv` 数据文件。

## 项目结构

```
.
├── game_user_analysis.py              # 主分析脚本
├── user_behavior_data.csv             # 生成的模拟数据文件
├── dau_trend.png                      # DAU 趋势折线图
├── retention_rate.png                 # 留存率柱状图
├── user_activity_distribution.png     # 用户活跃度分布直方图
├── venv/                              # Python 虚拟环境
└── README.md                          # 项目说明文档
```

## 应用场景

- 游戏运营数据分析入门学习
- 用户画像构建基础实践
- 付费转化与留存策略研究
- 数据分析与可视化教学演示

---

# Game User Behavior Data Analysis System

## Project Overview

This project is a Python-based game user behavior data analysis system. It simulates login and payment data for 1,000 users over 7 days, performs multi-dimensional analysis on key metrics such as user activity, payment behavior, and retention rate, and presents the results through intuitive visualizations.

## Feature Modules

### 1. Simulated Data Generation
- Randomly generates behavioral data for 1,000 users over 7 days using NumPy
- Each user's active days are randomly distributed between 1 and 7
- Daily payment behavior is simulated via binomial distribution with a 10% probability
- Generated data fields: `user_id`, `day`, `login` (login flag), `pay` (payment flag)

### 2. DAU (Daily Active Users) Analysis
- Counts unique active users per day
- Plots a DAU trend line chart to visually display daily active user changes

### 3. Payment Rate Analysis
- Calculates the overall payment rate
- Computes daily payment rates
- Outputs results in percentage format

### 4. Retention Analysis
- Calculates next-day retention rates between adjacent days (e.g., Day1→Day2, Day2→Day3)
- Retention Rate = Number of users active on both adjacent days / Number of users active on the previous day
- Displays retention rate changes via a bar chart

### 5. User Activity Analysis
- Counts total login days for each user
- Outputs average, maximum, and minimum login days
- Displays user activity distribution via a histogram

### 6. User Segmentation
- **High-Activity Users**: Login days ≥ 5
- **Normal Users**: Login days 3–4
- **Low-Activity Users (Churn Risk)**: Login days ≤ 2
- Outputs the count of users in each segment

### 7. Paying User Analysis
- Identifies paying users and non-paying users
- Compares the average login days between paying and free user groups

### 8. Data Visualization

Running the script will generate three PNG images in the current directory:

#### DAU Trend Chart (`dau_trend.png`)
- Line chart with Day 1~7 on the x-axis and unique active user count on the y-axis
- Daily DAU remains stable between 560 and 600 users with minimal fluctuation

#### Retention Rate Bar Chart (`retention_rate.png`)
- Bar chart displaying next-day retention rates for 6 adjacent day pairs (1→2, 2→3, ..., 6→7)
- Retention Rate = Users active on both adjacent days / Users active on the previous day
- Retention rates stay consistently within the 65%–69% range

#### User Activity Distribution Histogram (`user_activity_distribution.png`)
- Histogram with login days (1–7) on the x-axis and user count on the y-axis
- Displays the overall distribution of login days across all 1,000 users, with 7-day fully-active users comprising the largest share

## Tech Stack

| Technology   | Purpose                        |
| ------------ | ------------------------------ |
| Python 3.x   | Programming language           |
| Pandas       | Data processing and analysis   |
| NumPy        | Numerical computation and simulation |
| Matplotlib   | Data visualization             |

## Quick Start

### Requirements

- Python 3.7+
- pip

### Install Dependencies

```bash
pip install pandas numpy matplotlib
```

### Run

```bash
python game_user_analysis.py
```

### Output Description

After running the script, the following analysis results will be output to the terminal in sequence:

1. Data preview (first 5 rows)
2. DAU statistics
3. Overall and daily payment rates
4. Daily retention rates
5. User activity statistics
6. User segmentation counts
7. Paying user statistics and their correlation with activity

Three PNG chart files (`dau_trend.png`, `retention_rate.png`, `user_activity_distribution.png`) will also be saved in the current directory, along with a `user_behavior_data.csv` data file.

## Project Structure

```
.
├── game_user_analysis.py              # Main analysis script
├── user_behavior_data.csv             # Generated simulated data file
├── dau_trend.png                      # DAU trend line chart
├── retention_rate.png                 # Retention rate bar chart
├── user_activity_distribution.png     # User activity distribution histogram
├── venv/                              # Python virtual environment
└── README.md                          # Project documentation
```

## Use Cases

- Introductory learning of game operations data analysis
- Basic practice of user profiling
- Research on payment conversion and retention strategies
- Data analysis and visualization teaching demonstrations
