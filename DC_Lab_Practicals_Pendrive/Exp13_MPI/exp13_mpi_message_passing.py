from mpi4py import MPI


def main():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    if size < 2:
        if rank == 0:
            print("This program requires at least 2 processes.")
        return

    if rank == 0:
        message = "Hello from process 0"
        comm.send(message, dest=1, tag=0)
        print(f"Process {rank} sent: {message}")
    elif rank == 1:
        message = comm.recv(source=0, tag=0)
        print(f"Process {rank} received: {message}")


if __name__ == "__main__":
    main()
