## System Diagram
```mermaid
graph TD;
A[Laptop]-->B[VNC Viewer]
B-->A
A-->C[Putty-SSH / WinSCP - SCP]
C-->A
C-->D[Network Router]
D-->E[Raspberry Pi]
F[Keyboard / Mouse]-->E
E-->G[HDMI Monitor]
```