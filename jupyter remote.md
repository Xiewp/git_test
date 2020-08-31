# 如何在本地浏览器打开远程服务器下的docker的jupyter notebook。
##> 1.首先在相应的数组机服务器上，通过docker ps命令查看需要配置远程jupyter的用户名的PORTS，可以看到PORTS对应的类似信息6006/tcp, 8888/tcp, 0.0.0.0:3022->22/tcp, 0.0.0.0:3080->80/tcp, 0.0.0.0:8900->5900/tcp, 0.0.0.0:8901->5901/tcp, 0.0.0.0:8902->5902/tcp, 0.0.0.0:8903->5903/tcp, 0.0.0.0:8904->5904/tcp, 0.0.0.0:8905->5905/tcp，以0.0.0.0:8903->5903/tcp为例，前面的0.0.0.0表示任意ip，后面的8905表示的是宿主机的8905端口，映射到了docker里的5905端口。
##> 2.查看完数组机和docker的端口映射后，就可以配置jupyter的远程服务。在宿主机上输入以下命令：
`jupyter notebook --no-browser --port 5905 --ip=0.0.0.0 --allow-root`
##> 3.输入以上命令后，可以得到如下信息：
    [I 01:15:37.365 NotebookApp] jupyter_tensorboard extension loaded.
    [I 01:15:37.391 NotebookApp] JupyterLab extension loaded from /opt/conda/lib/python3.6/site-packages/jupyterlab
    [I 01:15:37.391 NotebookApp] JupyterLab application directory is /opt/conda/share/jupyter/lab
    [I 01:15:37.393 NotebookApp] [Jupytext Server Extension] NotebookApp.contents_manager_class is (a subclass of) jupytext.TextFileContentsManager already - OK
    [I 01:15:37.393 NotebookApp] Serving notebooks from local directory: /backup
    [I 01:15:37.393 NotebookApp] The Jupyter Notebook is running at:
    [I 01:15:37.393 NotebookApp] http://hostname:8888/?token=fd7c1c079e4a00940083891012d9539af672f1c79873a292
    [I 01:15:37.393 NotebookApp]  or http://127.0.0.1:5905/?token=fd7c1c079e4a00940083891012d9539af672f1c79873a292
    [I 01:15:37.393 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
    [C 01:15:37.397 NotebookApp] 
    
        To access the notebook, open this file in a browser:
            file:///root/.local/share/jupyter/runtime/nbserver-19267-open.html
        Or copy and paste one of these URLs:
            http://hostname:8888/?token=fd7c1c079e4a00940083891012d9539af672f1c79873a292
        or http://127.0.0.1:5905/?token=fd7c1c079e4a00940083891012d9539af672f1c79873a292
    [I 01:16:33.217 NotebookApp] 302 GET /?token=fd7c1c079e4a00940083891012d9539af672f1c79873a292 (172.16.115.195) 0.70ms`
##> 4.复制`http://127.0.0.1:5905/?token=fd7c1c079e4a00940083891012d9539af672f1c79873a292`到本地浏览器，并将`127.0.0.1`替换为宿主机的IP，同时将5905替换成宿主机对应的端口，这里为8905，回车即可打开远程jupyter notebook。
##> 5.如果想要远程jupyter一直能用，而终端关闭了也没有关系，就需要将原命令改成如下形式：
    jupyter notebook --no-browser --port 5905 --ip=0.0.0.0 --allow-root & disown