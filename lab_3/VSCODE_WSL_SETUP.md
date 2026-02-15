# Using WSL with VS Code for C++ Compilation

## ✅ Setup Complete!

Your VS Code is now configured to use WSL's g++ compiler instead of Windows MSYS2/MinGW.

---

## What I Configured:

### 1. **IntelliSense Configuration** (`.vscode/c_cpp_properties.json`)
- Points to WSL's C++ headers at `/usr/include/c++/11/`
- Uses WSL's g++ compiler at `/usr/bin/g++`
- Enables OpenMP support
- **Result**: No more red squiggly lines for `#include <cmath>`, `<omp.h>`, etc.

### 2. **Build Tasks** (`.vscode/tasks.json`)
- Build: `Ctrl+Shift+B` → Runs `make` in WSL
- Run: Custom task to build and run the program
- Clean: Removes compiled files

### 3. **Terminal Settings** (`.vscode/settings.json`)
- Default terminal set to WSL Ubuntu
- Press `` Ctrl+` `` to open integrated terminal

---

## How to Use:

### Option 1: Build with Keyboard Shortcut
Press **`Ctrl+Shift+B`** to build the project in WSL

### Option 2: Build from Terminal
1. Open WSL terminal: `` Ctrl+` ``
2. Make sure you're in the lab_3 directory
3. Run:
   ```bash
   make clean && make
   ```

### Option 3: Run from VS Code
1. Press `Ctrl+Shift+P`
2. Type "Run Task"
3. Select "Run in WSL"

---

## Quick Commands (WSL Terminal):

```bash
# Build
make clean && make

# Run with 500x500 matrix
./correlate 500 500

# Run with 1000x1000 matrix
./correlate 1000 1000

# Run with performance stats
/usr/bin/time -v ./correlate 500 500

# Clean build files
make clean
```

---

## Fixing IntelliSense Errors:

If you still see red squiggles after this setup:

### 1. Reload VS Code Window
- Press `Ctrl+Shift+P`
- Type "Reload Window"
- Press Enter

### 2. Select IntelliSense Configuration
- Press `Ctrl+Shift+P`
- Type "C/C++: Select IntelliSense Configuration"
- Choose "WSL"

### 3. Restart VS Code
- Close and reopen VS Code completely

---

## File Structure:

```
lab_3/
├── .vscode/
│   ├── c_cpp_properties.json    # IntelliSense config (WSL paths)
│   ├── tasks.json               # Build/Run tasks
│   └── settings.json            # Editor settings
├── correlate.cpp                # Implementation
├── correlate.h                  # Header file
├── main.cpp                     # Main program
├── Makefile                     # Build configuration
└── correlate                    # Compiled binary (in WSL)
```

---

## Benefits of Using WSL:

✅ **Native Linux tools**: Use g++, make, perf, gprof directly  
✅ **Better OpenMP support**: Full OpenMP implementation  
✅ **No MSYS2 needed**: Works with just WSL  
✅ **Fast compilation**: Native Linux compiler speeds  
✅ **Easy profiling**: Access to Linux performance tools  

---

## Troubleshooting:

### Error: "cannot open source file"
**Fix**: Reload VS Code window (`Ctrl+Shift+P` → "Reload Window")

### Error: "g++ not found"
**Fix**: Make sure g++ is installed in WSL:
```bash
wsl sudo apt install build-essential
```

### Build fails with "Permission denied"
**Fix**: Make sure files aren't read-only:
```bash
wsl chmod +x correlate
```

### Terminal doesn't open WSL
**Fix**: 
1. Press `` Ctrl+` ``
2. Click the `+` dropdown
3. Select "Ubuntu (WSL)"

---

## Testing Your Setup:

Run this command to verify everything works:

```bash
wsl bash -c "cd '/mnt/c/Users/Sudhanshu raj/OneDrive/Documents/TIET subjects/Tiet 6th sem/prallel computing/lab_3' && make clean && make && ./correlate 100 100"
```

You should see the performance benchmark output!

---

## Next Steps:

1. **Reload VS Code**: `Ctrl+Shift+P` → "Reload Window"
2. **Open a file**: Open `correlate.cpp` - red squiggles should be gone!
3. **Build**: Press `Ctrl+Shift+B`
4. **Run**: Use the terminal commands above

Your code is now using WSL's compiler! 🎉
