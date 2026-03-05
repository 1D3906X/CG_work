<div align="center">
  <h2><i>CG_work0:万有引力</i></h2> 
</div>

<div align="center">
  
>第一次计算机图形学作业:
>项目架构、代码逻辑及效果展示
</div>

**一、项目架构**

本次实验项目名称为Work0，严格按照src布局规范整理目录，实现代码分层解耦，具体目录结构如下：
```bash
CG-Lab/
├── .gitignore
├── README.md
├── src/
│   └── Work0/
│       ├── __init__.py
│       ├── config.py
│       ├── physics.py
│       └── main.py
└── .venv/
```

项目分为三层，分别是参数配置层（config.py）、底层计算层（physics.py）、前端视图层（main.py），各层功能独立，方便修改和维护。

**二、代码逻辑**

1.  config.py：集中定义窗口大小、粒子数量、物理参数等所有可配置信息，避免代码硬编码。

2.  physics.py：基于Taichi框架，初始化GPU后端，实现粒子初始化、万有引力计算、粒子速度和位置更新的并行逻辑。

3.  main.py：创建可视化窗口，调用physics.py中的计算逻辑，实现粒子渲染和GUI参数交互，完成整个仿真流程。

**三、效果展示**

