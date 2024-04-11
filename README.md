# osfinder
A small tool to find &lt;module 'os' (frozen)> import path in any given package to bypass some sandboxes or solve CTF challenges.

## Usage
```
python3 finder.py --package=pandas --target=os --maxl=5 --maxn=100
```

- package: the target package in which we want to find os.
- target: target module, default to be os.
- maxl: maximum length of import chain.
- maxn: maximum number of import chains.
