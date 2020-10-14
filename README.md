# AI_lesson_labs
hitsz 2020年人工智能实验题目 

# 实验一

pass

# 实验二

来源于UC Berkeley的题

我们需要编辑的文件为`search.py`和`searchAgents.py`。

需要参考的文件为`pacman.py`, `game.py`, `util.py`, 因此我们先了解一下文件关系。

如果是linux,例如ubuntu,则需要安装依赖库: `sudo apt-get install python3-tk`

## 文件内容

### `search.py`

![image-20201008145228754](README.assets/image-20201008145228754.png)

这个文件里我们要完成的是这几个搜索算法。

### `searchAgents.py`

说明了一些命令:

`-p`用于选择一个agent

`-a`用于传递参数

例如以下命令:

`python pacman.py -p SearchAgent -a fn=dfs`

该部分的代码只需要修改一小部分

### `pacman.py`

该文件被注释划分成了三个部分, 在pycharm中的侧边栏打开structure视图, 对照代码中的注释可以看到他的划分

![image-20201008133726272](README.assets/image-20201008133726272.png)

代码中的注释也对这三部分是否要看标注了重要度: 第一部分有一部分要看; 第二部分可看可不看; 第三部分必须要看。

下面看一下`GameState`类中有什么方法:

![image-20201008134133860](README.assets/image-20201008134133860.png)

看函数名字可以知道这些函数多为获取某些状态的函数。

通过观察运行命令可以发现, 首先调用的是`pacman.py`文件。

```shell
/pacman.py   runGames( **args)
	
```

```python
def runGames( 
    layout, 
    pacman, 
    ghosts, 
    display, 
    numGames, 
    record, 
    numTraining = 0, 
    catchExceptions=False, 
    timeout=30 )
```

### `game.py`

### `util.py`





## 命令

`python3 pacman.py -l mediumMaze -p SearchAgent -a fn=ucs`

`python3 pacman.py -l mediumDottedMaze -p StayEastSearchAgent`

`python3 pacman.py -l mediumScaryMaze -p StayWestSearchAgent`

`python3 pacman.py -l bigSearch -p ClosestDotSearchAgent -z .5`