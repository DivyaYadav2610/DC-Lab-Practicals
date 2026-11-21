DC LAB PRACTICALS - PENDRIVE PACK
=================================

13 experiments are covered as per the uploaded DC Lab Manual.

HOW TO USE
1. Open the experiment folder.
2. Open the code file in IDLE / VS Code / Notepad / IDE.
3. Copy-paste into the practical system.
4. Save using the filename shown below.

LANGUAGE / RUN COMMANDS
- Python: python filename.py
- Java: javac ClassName.java   then   java ClassName
- C: gcc filename.c -o program   then   ./program (Windows: program.exe)
- MPI: install mpi4py and an MPI implementation, then:
       mpiexec -n 2 python exp13_mpi_message_passing.py

IMPORTANT
- Experiment 3 RPC: run server first in one terminal, then client in another.
- Experiment 4 IPC Java: run server first, then client.
- Experiment 10 Group Communication: run server, then start Client 1 and Client 2.
- Experiment 11 CORBA: the manual contains theory only; no program is provided.
- Experiment 13 MPI requires mpi4py + MPI runtime (e.g. MPICH / Microsoft MPI).

NOTES
Some errors in the printed manual were corrected so the code can run:
- Exp 3 subtraction and multiplication functions.
- Exp 6 line-wrapped print strings.
- Exp 9 uses portable standard C instead of Turbo C-only conio/dos functions.
- Exp 10 client 2 is completed from the same client structure as client 1.

Keep the original DC_Lab_Experiments.pdf on the pendrive too.
