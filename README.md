An example use of python bindings to hkl

Use the python executable from apt
```bash
sudo apt install python3
```

# hkl
Compile hkl with the flag --enable-introspection (and, for now, --disable-gui)
```bash
./autogen
./configure --enable introspection
make
sudo make install
```

(when reinstalling, sudo is required for make install, needs sudo to replace ccan)

identify where the hkl typelib file was created, the file is named Hkl-5.0.typelib and is located in 
/usr/local/lib/girepository-1.0


export the path to the typelib file
```bash
export GI_TYPELIB_PATH=/usr/local/lib/girepository-1.0
```

run the example file
```bash
python3 example_binding_hkl.py
```


