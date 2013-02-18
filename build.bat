@ECHO OFF
cd "C:\Program Files (x86)\Python33"
start python.exe Scripts\cxfreeze.py --target-dir C:\Users\Caleb\Documents\GitHub\RenderCalc\build  C:\Users\Caleb\Documents\GitHub\RenderCalc\CyclesRenderTimeCalculator.py
exit