**Activate the virtual environment**

```
source blockchain-env/bin/activate
```

**Install all package**

```
pip install -r requirement.txt
```

**Install pip in linux**


**User must be root**


```
On Arch
pacman -S  python-pip  #python3
pacman -S python2-pip #python2

```
```
On debian/ubuntu
apt install python-pip #python2
apt install python3-pip #pyhton3
```

**Executing modules from blockchain-env**
```
python3 -m backend.blockchain.block

after -m is just the path of file
```